#include "pauli_term_container.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>
#include <pybind11/functional.h>

#include <sstream>
#include <memory>
#include <string>
#include <vector>

#include "circuit.hpp"
#include "noise_model.hpp"
#include "observable.hpp"
#include "pauli.hpp"
#include "pauli_term.hpp"
#include "scheduler.hpp"
#include "truncate.hpp"

namespace py = pybind11;

using PTC = PauliTermContainer<coeff_t>;

// Define alias for our holder types for clarity
using TruncatorPtr = std::shared_ptr<Truncator<coeff_t>>;
using SchedulingPolicyPtr = std::shared_ptr<SchedulingPolicy>;

// Concrete holder types
using CoeffTruncatorPtr = std::shared_ptr<CoefficientTruncator<coeff_t>>;
using WeightTruncatorPtr = std::shared_ptr<WeightTruncator>;
using NeverTruncatorPtr = std::shared_ptr<NeverTruncator>;
using KeepNTruncatorPtr = std::shared_ptr<KeepNTruncator<coeff_t>>;
using NeverPolicyPtr = std::shared_ptr<NeverPolicy>;
using AlwaysBeforePolicyPtr = std::shared_ptr<AlwaysBeforeSplittingPolicy>;
using AlwaysAfterPolicyPtr = std::shared_ptr<AlwaysAfterSplittingPolicy>;

using LambdaPredicate_t = std::function<bool(PauliTermContainer<coeff_t>::NonOwningPauliTermPacked const&)>;
using LambdaTruncator = PredicateTruncator<LambdaPredicate_t>;
using LambdaTruncatorPtr = std::shared_ptr<LambdaTruncator>;

struct LambdaPolicy : public SchedulingPolicy {
    public:
	using predicate_t = std::function<bool(SimulationState const&, OperationType, Timing)>;
	LambdaPolicy(predicate_t const& pred) : predicate{ pred } {}
	~LambdaPolicy() override {}
	bool should_apply(SimulationState const& state, OperationType op_type, Timing timing) override {
		return predicate(state, op_type, timing);
	}

    private:
	predicate_t predicate;
};

PYBIND11_MODULE(_core, m) {
	m.doc() = "Core C++ functionality for pyrauli, wrapped with pybind11";

	// Enums
	py::enum_<Pauli_enum>(m, "PauliEnum", "Enumeration for single Pauli operators (I, X, Y, Z).")
		.value("I", Pauli_enum::I)
		.value("X", Pauli_enum::X)
		.value("Y", Pauli_enum::Y)
		.value("Z", Pauli_enum::Z);
	py::enum_<Pauli_gates>(m, "PauliGate", "Enumeration for single-qubit Pauli gates (I, X, Y, Z).")
		.value("I", Pauli_gates::I)
		.value("X", Pauli_gates::X)
		.value("Y", Pauli_gates::Y)
		.value("Z", Pauli_gates::Z);
	py::enum_<Clifford_Gates_1Q>(m, "CliffordGate", "Enumeration for single-qubit Clifford gates.")
		.value("H", Clifford_Gates_1Q::H, "Hadamard gate.");
	py::enum_<UnitalNoise>(m, "UnitalNoise", "Enumeration for unital noise channels.")
		.value("Depolarizing", UnitalNoise::Depolarizing, "Depolarizing noise channel.")
		.value("Dephasing", UnitalNoise::Dephasing, "Dephasing noise channel.");
	py::enum_<QGate>(m, "QGate", "Enumeration for all supported quantum gates and noise channels.")
		.value("I", QGate::I)
		.value("X", QGate::X)
		.value("Y", QGate::Y)
		.value("Z", QGate::Z)
		.value("H", QGate::H)
		.value("Rz", QGate::Rz)
		.value("Cx", QGate::Cx)
		.value("AmplitudeDamping", QGate::AmplitudeDamping)
		.value("Depolarizing", QGate::Depolarizing)
		.value("Dephasing", QGate::Dephasing);

	// Pauli class
	py::class_<Pauli>(m, "Pauli", "Represents a single Pauli operator (I, X, Y, or Z).")
		.def(py::init<Pauli_enum>(), "Constructs from a PauliEnum.")
		.def(py::init<char>(), "Constructs from a character ('I', 'X', 'Y', or 'Z').")
		.def(py::init<std::string_view>(), "Constructs from a single-character string.")
		.def("commutes_with", &Pauli::commutes_with, "Checks if this Pauli operator commutes with another.")
		.def("weight", &Pauli::weight, "Calculates the Pauli weight (1 if not Identity, 0 otherwise).")
		.def("apply_pauli", &Pauli::apply_pauli,
		     "Applies a Pauli gate to this operator (in the Heisenberg picture).")
		.def("apply_unital_noise", &Pauli::apply_unital_noise,
		     "Applies a unital noise channel to this operator.")
		.def("apply_clifford", &Pauli::apply_clifford,
		     "Applies a single-qubit Clifford gate to this operator, modifying it in place.")
		.def("apply_cx", &Pauli::apply_cx,
		     "Applies the control part of a CNOT gate to this operator, modifying it and the target in place.")
		.def(py::self == py::self)
		.def(py::self != py::self)
		.def("__repr__", [](const Pauli& p) {
			std::stringstream ss;
			ss << p;
			return ss.str();
		});

	// PauliTerm class
	py::class_<PauliTerm<coeff_t>>(
		m, "PauliTerm",
		"Represents a single term in an observable, consisting of a Pauli string and a coefficient.")
		.def(py::init<std::string_view, coeff_t>(), py::arg("pauli_string"), py::arg("coefficient") = 1.0,
		     "Constructs from a string representation and a coefficient.")
		.def("apply_pauli", &PauliTerm<coeff_t>::apply_pauli,
		     "Applies a Pauli gate to a specific qubit of the term.")
		.def("apply_clifford", &PauliTerm<coeff_t>::apply_clifford,
		     "Applies a Clifford gate to a specific qubit of the term.")
		.def("apply_unital_noise", &PauliTerm<coeff_t>::apply_unital_noise,
		     "Applies a unital noise channel to a specific qubit of the term.")
		.def("apply_cx", &PauliTerm<coeff_t>::apply_cx, "Applies a CNOT gate to the term.")
		.def("apply_rz", &PauliTerm<coeff_t>::apply_rz, "Applies an Rz gate, potentially splitting the term.")
		.def("apply_amplitude_damping_xy", &PauliTerm<coeff_t>::apply_amplitude_damping_xy,
		     "Applies the X/Y part of the amplitude damping channel.")
		.def("apply_amplitude_damping_z", &PauliTerm<coeff_t>::apply_amplitude_damping_z,
		     "Applies the Z part of the amplitude damping channel, splitting the term.")
		.def("expectation_value", &PauliTerm<coeff_t>::expectation_value,
		     "Calculates the expectation value of this single term.")
		.def("pauli_weight", &PauliTerm<coeff_t>::pauli_weight,
		     "Calculates the Pauli weight (number of non-identity operators).")
		.def_property_readonly("coefficient", &PauliTerm<coeff_t>::coefficient, "The coefficient of the term.")
		.def("__getitem__", [](const PauliTerm<coeff_t>& pt, size_t i) { return pt[i]; })
		.def("__setitem__", [](PauliTerm<coeff_t>& pt, size_t i, const Pauli& p) { pt[i] = p; })
		.def("__len__", &PauliTerm<coeff_t>::size)
		.def(py::self == py::self)
		.def(py::self != py::self)
		.def("__repr__", [](const PauliTerm<coeff_t>& pt) {
			std::stringstream ss;
			ss << pt;
			return ss.str();
		});

	// Observable class
	py::class_<Observable<coeff_t>>(m, "Observable",
					"Represents a quantum observable as a linear combination of Pauli strings.")
		.def(py::init<std::string_view, coeff_t>(), py::arg("pauli_string"), py::arg("coeff") = 1.0,
		     "Constructs an observable from a single Pauli string.")
		.def(py::init<std::initializer_list<std::string_view>>(),
		     "Constructs an observable from an initializer_list of Pauli strings.")
		// Use a lambda to correctly initialize from a list of PauliTerm objects
		.def(py::init([](const std::vector<PauliTerm<coeff_t>>& paulis) {
			     return Observable<coeff_t>(paulis.begin(), paulis.end());
		     }),
		     "Constructs an observable from a list of PauliTerm objects.")
		.def(py::init([](const std::vector<std::string>& paulis) {
			     return Observable<coeff_t>(paulis.begin(), paulis.end());
		     }),
		     "Constructs an observable from a list of Pauli strings.")
		.def("apply_pauli", &Observable<coeff_t>::apply_pauli,
		     "Applies a single-qubit Pauli gate to the observable.")
		.def("apply_clifford", &Observable<coeff_t>::apply_clifford,
		     "Applies a single-qubit Clifford gate to the observable.")
		.def("apply_unital_noise", &Observable<coeff_t>::apply_unital_noise,
		     "Applies a single-qubit unital noise channel.")
		.def("apply_cx", &Observable<coeff_t>::apply_cx, "Applies a CNOT (CX) gate to the observable.")
		.def("apply_rz", &Observable<coeff_t>::apply_rz,
		     "Applies a single-qubit Rz rotation gate to the observable.")
		.def("apply_amplitude_damping", &Observable<coeff_t>::apply_amplitude_damping,
		     "Applies an amplitude damping noise channel.")
		.def("expectation_value", &Observable<coeff_t>::expectation_value,
		     "Calculates the expectation value of the observable.")
		.def("merge", &Observable<coeff_t>::merge, "Merges Pauli terms with identical Pauli strings.")
		.def("size", &Observable<coeff_t>::size, "Gets the number of Pauli terms in the observable.")
		.def(
			"truncate", [](Observable<coeff_t>& obs, TruncatorPtr ptr) { return obs.truncate(*ptr); },
			"Truncates the observable based on a given truncation strategy.")
		.def(py::self == py::self)
		.def(py::self != py::self)
		.def("__getitem__", [](const Observable<coeff_t>& obs, size_t i) { return obs[i]; })
		.def("__len__", &Observable<coeff_t>::size)
		.def(
			"__iter__",
			[](const Observable<coeff_t>& obs) { return py::make_iterator(obs.begin(), obs.end()); },
			py::keep_alive<0, 1>())
		.def("__repr__", [](const Observable<coeff_t>& obs) {
			std::stringstream ss;
			ss << obs;
			return ss.str();
		});

	// NoiseModel class
	py::class_<Noise<coeff_t>>(m, "Noise", "Defines the strengths of different noise channels.")
		.def(py::init<>())
		.def_readwrite("depolarizing_strength", &Noise<coeff_t>::depolarizing_strength)
		.def_readwrite("dephasing_strength", &Noise<coeff_t>::dephasing_strength)
		.def_readwrite("amplitude_damping_strength", &Noise<coeff_t>::amplitude_damping_strength);
	py::class_<NoiseModel<coeff_t>>(m, "NoiseModel", "A model for applying noise to quantum gates.")
		.def(py::init<>())
		.def("add_unital_noise_on_gate", &NoiseModel<coeff_t>::add_unital_noise_on_gate,
		     "Adds a unital noise channel to be applied after a specific gate type.")
		.def("add_amplitude_damping_on_gate", &NoiseModel<coeff_t>::add_amplitude_damping_on_gate,
		     "Adds an amplitude damping channel to be applied after a specific gate type.");

	// Truncators (using shared_ptr holder for polymorphism)
	py::class_<Truncator<coeff_t>, TruncatorPtr>(m, "Truncator",
						     "Abstract base class for defining truncation strategies.");
	py::class_<CoefficientTruncator<coeff_t>, Truncator<coeff_t>, CoeffTruncatorPtr>(
		m, "CoefficientTruncator", "Truncator that removes Pauli terms with small coefficients.")
		.def(py::init<coeff_t>());
	py::class_<WeightTruncator, Truncator<coeff_t>, WeightTruncatorPtr>(
		m, "WeightTruncator", "Truncator that removes Pauli terms with high Pauli weight.")
		.def(py::init<size_t>());
	py::class_<NeverTruncator, Truncator<coeff_t>, NeverTruncatorPtr>(m, "NeverTruncator",
									  "A truncator that never removes any terms.")
		.def(py::init<>());
	py::class_<KeepNTruncator<coeff_t>, Truncator<coeff_t>, KeepNTruncatorPtr>(
		m, "KeepNTruncator",
		"A truncator that removes least significant Pauli Terms, when their numbers is above a threshold.")
		.def(py::init<std::size_t>());
	py::class_<LambdaTruncator, Truncator<coeff_t>, LambdaTruncatorPtr>(
		m, "LambdaTruncator", "A truncator that uses a Python function as a predicate.")
		.def(py::init<LambdaPredicate_t>());
	py::class_<RuntimeMultiTruncators<coeff_t>, Truncator<coeff_t>,
		   std::shared_ptr<RuntimeMultiTruncators<coeff_t>>>(
		m, "MultiTruncator", "A truncator that combines multiple truncators at runtime.")
		.def(py::init<const std::vector<TruncatorPtr>&>());

	py::enum_<OperationType>(m, "OperationType", "Type of operation in the simulation.")
		.value("BasicGate", OperationType::BasicGate)
		.value("SplittingGate", OperationType::SplittingGate)
		.value("Merge", OperationType::Merge)
		.value("Truncate", OperationType::Truncate);

	py::enum_<Timing>(m, "Timing", "Timing of a policy application relative to an operation.")
		.value("Before", Timing::Before)
		.value("After", Timing::After);

	py::class_<CompressionResult>(m, "CompressionResult",
				      "Stores the result of a compression (merge or truncate) operation.")
		.def_readonly("nb_terms_before", &CompressionResult::nb_terms_before,
			      "Number of terms before compression.")
		.def_readonly("nb_terms_merged", &CompressionResult::nb_terms_merged, "Number of terms removed/merged.")
		.def("nb_terms_after", &CompressionResult::nb_terms_after, "Number of terms after compression.")
		.def("__repr__", [](const CompressionResult& cr) {
			return "<CompressionResult: " + std::to_string(cr.nb_terms_before) + " -> " +
			       std::to_string(cr.nb_terms_after()) + ">";
		});

	py::class_<SimulationState>(m, "SimulationState", "Holds the state of the simulation at a given point in time.")
		.def_property_readonly("nb_gates_applied", &SimulationState::get_nb_gates_applied,
				       "Total number of gates applied so far.")
		.def_property_readonly("nb_splitting_gates_applied", &SimulationState::get_nb_splitting_gates_applied,
				       "Number of splitting gates applied so far.")
		.def_property_readonly("nb_splitting_gates_left", &SimulationState::get_nb_splitting_gates_left,
				       "Number of splitting gates remaining in the circuit.")
		// Add the history getters
		.def_property_readonly("terms_history", &SimulationState::get_terms_history,
				       "History of observable sizes after each operation.")
		.def_property_readonly("merge_history", &SimulationState::get_merge_history,
				       "History of merge operations.")
		.def_property_readonly("truncate_history", &SimulationState::get_truncate_history,
				       "History of truncate operations.")
		.def("__repr__", [](const SimulationState& s) {
			return "<SimulationState: " + std::to_string(s.get_nb_gates_applied()) + " gates applied>";
		});
	// Scheduling Policies (using shared_ptr holder for polymorphism)
	py::class_<SchedulingPolicy, SchedulingPolicyPtr>(m, "SchedulingPolicy",
							  "Abstract base class for defining scheduling policies.");
	py::class_<NeverPolicy, SchedulingPolicy, NeverPolicyPtr>(m, "NeverPolicy",
								  "A policy that never applies an optimization.")
		.def(py::init<>());
	py::class_<AlwaysBeforeSplittingPolicy, SchedulingPolicy, AlwaysBeforePolicyPtr>(
		m, "AlwaysBeforeSplittingPolicy",
		"A policy that applies an optimization just before every splitting gate.")
		.def(py::init<>());
	py::class_<AlwaysAfterSplittingPolicy, SchedulingPolicy, AlwaysAfterPolicyPtr>(
		m, "AlwaysAfterSplittingPolicy",
		"A policy that applies an optimization just after every splitting gate.")
		.def(py::init<>());
	py::class_<LambdaPolicy, SchedulingPolicy, std::shared_ptr<LambdaPolicy>>(
		m, "LambdaPolicy", "A policy that uses a Python function to determine when to apply optimizations.")
		.def(py::init<LambdaPolicy::predicate_t>());

	// Circuit class
	py::class_<Circuit<coeff_t>>(m, "Circuit",
				     "Represents a quantum circuit and provides a high-level simulation interface.")
		.def(py::init<unsigned, std::shared_ptr<Truncator<coeff_t>>, const NoiseModel<coeff_t>&,
			      std::shared_ptr<SchedulingPolicy>, std::shared_ptr<SchedulingPolicy>>(),
		     py::arg("nb_qubits"), py::arg("truncator") = std::make_shared<NeverTruncator>(),
		     py::arg("noise_model") = NoiseModel<coeff_t>(),
		     py::arg("merge_policy") = std::make_shared<AlwaysAfterSplittingPolicy>(),
		     py::arg("truncate_policy") = std::make_shared<AlwaysAfterSplittingPolicy>())
		.def("nb_qubits", &Circuit<coeff_t>::nb_qubits, "Gets the number of qubits in the circuit.")
		// Use lambdas to resolve templated overloads
		.def(
			"add_operation",
			[](Circuit<coeff_t>& self, std::string op, unsigned q1) { self.add_operation(op, q1); },
			"Adds a single-qubit gate.", py::arg("op"), py::arg("qubit"))
		.def(
			"add_operation",
			[](Circuit<coeff_t>& self, std::string op, unsigned q1, coeff_t p) {
				self.add_operation(op, q1, p);
			},
			"Adds a single-qubit gate with a parameter.", py::arg("op"), py::arg("qubit"), py::arg("param"))
		.def(
			"add_operation",
			[](Circuit<coeff_t>& self, std::string op, unsigned q1, unsigned q2) {
				self.add_operation(op, q1, q2);
			},
			"Adds a two-qubit gate.", py::arg("op"), py::arg("control"), py::arg("target"))
		.def("run", &Circuit<coeff_t>::run, "Runs the simulation on the circuit.")
		.def("reset", &Circuit<coeff_t>::reset, "Clears all operations from the circuit.")
		.def("set_truncator", &Circuit<coeff_t>::set_truncator, "Sets a new truncator for the circuit.")
		.def("set_merge_policy", &Circuit<coeff_t>::set_merge_policy,
		     "Sets a new policy for when to merge Pauli terms.")
		.def("set_truncate_policy", &Circuit<coeff_t>::set_truncate_policy,
		     "Sets a new policy for when to truncate the observable.");

	py::class_<PTC::ReadOnlyNonOwningPauliTermPacked>(m, "ReadOnlyPackedPauliTermView",
							  "A read-only, non-owning view of a packed Pauli term.")
		.def_property_readonly("coefficient", &PTC::ReadOnlyNonOwningPauliTermPacked::coefficient,
				       "The coefficient of the term.")
		.def_property_readonly("nb_qubits", &PTC::ReadOnlyNonOwningPauliTermPacked::size,
				       "The number of qubits in the term.")
		.def("pauli_weight", &PTC::ReadOnlyNonOwningPauliTermPacked::pauli_weight,
		     "Calculates the Pauli weight (number of non-identity operators).")
		.def("expectation_value", &PTC::ReadOnlyNonOwningPauliTermPacked::expectation_value,
		     "Calculates the expectation value of this single term.")
		.def(
			"to_pauli_term",
			[](const PTC::ReadOnlyNonOwningPauliTermPacked& self) {
				return static_cast<PauliTerm<coeff_t>>(self);
			},
			"Creates an owning PauliTerm copy from this view.")
		.def("__len__", &PTC::ReadOnlyNonOwningPauliTermPacked::size)
		.def("__getitem__", &PTC::ReadOnlyNonOwningPauliTermPacked::get_pauli,
		     "Gets the Pauli operator at a specific qubit index.")
		.def(py::self == py::self)
		.def(
			"__eq__",
			[](const PTC::ReadOnlyNonOwningPauliTermPacked& self, const PauliTerm<coeff_t>& other) {
				return self == other;
			},
			"Compares this view with an owning PauliTerm object.")
		.def("__repr__", [](const PTC::ReadOnlyNonOwningPauliTermPacked& pt) {
			std::stringstream ss;
			ss << pt;
			return ss.str();
		});

	py::class_<PTC::NonOwningPauliTermPacked>(m, "PackedPauliTermView",
						  "A mutable, non-owning view of a packed Pauli term.")
		.def_property("coefficient", &PTC::NonOwningPauliTermPacked::coefficient,
			      &PTC::NonOwningPauliTermPacked::set_coefficient,
			      "The coefficient of the term (read/write).")
		.def_property_readonly("nb_qubits", &PTC::NonOwningPauliTermPacked::size,
				       "The number of qubits in the term.")
		.def("pauli_weight", &PTC::NonOwningPauliTermPacked::pauli_weight,
		     "Calculates the Pauli weight (number of non-identity operators).")
		.def("expectation_value", &PTC::NonOwningPauliTermPacked::expectation_value,
		     "Calculates the expectation value of this single term.")
		.def(
			"to_pauli_term",
			[](const PTC::NonOwningPauliTermPacked& self) { return static_cast<PauliTerm<coeff_t>>(self); },
			"Creates an owning PauliTerm copy from this view.")
		.def("add_coeff", &PTC::NonOwningPauliTermPacked::add_coeff, "Adds a value to the term's coefficient.")
		.def("__len__", &PTC::NonOwningPauliTermPacked::size)
		.def("__getitem__", &PTC::NonOwningPauliTermPacked::get_pauli,
		     "Gets the Pauli operator at a specific qubit index.")
		.def("__setitem__", &PTC::NonOwningPauliTermPacked::set_pauli,
		     "Sets the Pauli operator at a specific qubit index.")
		.def(py::self == py::self)
		.def(
			"__eq__",
			[](const PTC::NonOwningPauliTermPacked& self, const PauliTerm<coeff_t>& other) {
				return self == other;
			},
			"Compares this view with an owning PauliTerm object.")
		.def("__repr__", [](const PTC::NonOwningPauliTermPacked& pt) {
			std::stringstream ss;
			ss << pt;
			return ss.str();
		});
}
