#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>
#include <pybind11/functional.h>

#include <sstream>
#include <memory>
#include <vector>

#include "circuit.hpp"
#include "noise_model.hpp"
#include "observable.hpp"
#include "pauli.hpp"
#include "pauli_term.hpp"
#include "scheduler.hpp"
#include "truncate.hpp"

namespace py = pybind11;

// Define alias for our holder types for clarity
using TruncatorPtr = std::shared_ptr<Truncator<coeff_t>>;
using SchedulingPolicyPtr = std::shared_ptr<SchedulingPolicy>;

// Concrete holder types
using CoeffTruncatorPtr = std::shared_ptr<CoefficientTruncator<coeff_t>>;
using WeightTruncatorPtr = std::shared_ptr<WeightTruncator>;
using NeverTruncatorPtr = std::shared_ptr<NeverTruncator>;
using NeverPolicyPtr = std::shared_ptr<NeverPolicy>;
using AlwaysBeforePolicyPtr = std::shared_ptr<AlwaysBeforeSplittingPolicy>;
using AlwaysAfterPolicyPtr = std::shared_ptr<AlwaysAfterSplittingPolicy>;

using LambdaPredicate_t = std::function<bool(PauliTerm<coeff_t> const&)>;
using LambdaTruncator = PredicateTruncator<LambdaPredicate_t>;
using LambdaTruncatorPtr = std::shared_ptr<LambdaTruncator>;

PYBIND11_MODULE(_core, m) {
	m.doc() = "Core C++ functionality for pyrauli, wrapped with pybind11";

	// Enums
	py::enum_<Pauli_enum>(m, "PauliEnum")
		.value("I", Pauli_enum::I)
		.value("X", Pauli_enum::X)
		.value("Y", Pauli_enum::Y)
		.value("Z", Pauli_enum::Z);
	py::enum_<Pauli_gates>(m, "PauliGate")
		.value("I", Pauli_gates::I)
		.value("X", Pauli_gates::X)
		.value("Y", Pauli_gates::Y)
		.value("Z", Pauli_gates::Z);
	py::enum_<Clifford_Gates_1Q>(m, "CliffordGate").value("H", Clifford_Gates_1Q::H);
	py::enum_<UnitalNoise>(m, "UnitalNoise")
		.value("Depolarizing", UnitalNoise::Depolarizing)
		.value("Dephasing", UnitalNoise::Dephasing);
	py::enum_<QGate>(m, "QGate")
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
	py::class_<Pauli>(m, "Pauli")
		.def(py::init<Pauli_enum>())
		.def(py::init<char>())
		.def(py::init<std::string_view>())
		.def("commutes_with", &Pauli::commutes_with)
		.def("weight", &Pauli::weight)
		.def("apply_pauli", &Pauli::apply_pauli)
		.def("apply_unital_noise", &Pauli::apply_unital_noise)
		.def("apply_clifford", &Pauli::apply_clifford)
		.def("apply_cx", &Pauli::apply_cx)
		.def(py::self == py::self)
		.def(py::self != py::self)
		.def("__repr__", [](const Pauli& p) {
			std::stringstream ss;
			ss << p;
			return ss.str();
		});

	// PauliTerm class
	py::class_<PauliTerm<coeff_t>>(m, "PauliTerm")
		.def(py::init<std::string_view, coeff_t>(), py::arg("pauli_string"), py::arg("coefficient") = 1.0)
		.def("apply_pauli", &PauliTerm<coeff_t>::apply_pauli)
		.def("apply_clifford", &PauliTerm<coeff_t>::apply_clifford)
		.def("apply_unital_noise", &PauliTerm<coeff_t>::apply_unital_noise)
		.def("apply_cx", &PauliTerm<coeff_t>::apply_cx)
		.def("apply_rz", &PauliTerm<coeff_t>::apply_rz)
		.def("apply_amplitude_damping_xy", &PauliTerm<coeff_t>::apply_amplitude_damping_xy)
		.def("apply_amplitude_damping_z", &PauliTerm<coeff_t>::apply_amplitude_damping_z)
		.def("expectation_value", &PauliTerm<coeff_t>::expectation_value)
		.def("pauli_weight", &PauliTerm<coeff_t>::pauli_weight)
		.def_property_readonly("coefficient", &PauliTerm<coeff_t>::coefficient)
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
	py::class_<Observable<coeff_t>>(m, "Observable")
		.def(py::init<std::string_view, coeff_t>(), py::arg("pauli_string"), py::arg("coeff") = 1.0)
		.def(py::init<std::initializer_list<std::string_view>>())
		// Use a lambda to correctly initialize from a list of PauliTerm objects
		.def(py::init([](const std::vector<PauliTerm<coeff_t>>& paulis) {
			return Observable<coeff_t>(paulis.begin(), paulis.end());
		}))
		.def(py::init([](const std::vector<std::string>& paulis) {
			return Observable<coeff_t>(paulis.begin(), paulis.end());
		}))
		.def("apply_pauli", &Observable<coeff_t>::apply_pauli)
		.def("apply_clifford", &Observable<coeff_t>::apply_clifford)
		.def("apply_unital_noise", &Observable<coeff_t>::apply_unital_noise)
		.def("apply_cx", &Observable<coeff_t>::apply_cx)
		.def("apply_rz", &Observable<coeff_t>::apply_rz)
		.def("apply_amplitude_damping", &Observable<coeff_t>::apply_amplitude_damping)
		.def("expectation_value", &Observable<coeff_t>::expectation_value)
		.def("merge", &Observable<coeff_t>::merge)
		.def("size", &Observable<coeff_t>::size)
		.def("truncate", [](Observable<coeff_t>& obs, TruncatorPtr ptr) { return obs.truncate(*ptr); })
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
	py::class_<Noise<coeff_t>>(m, "Noise")
		.def(py::init<>())
		.def_readwrite("depolarizing_strength", &Noise<coeff_t>::depolarizing_strength)
		.def_readwrite("dephasing_strength", &Noise<coeff_t>::dephasing_strength)
		.def_readwrite("amplitude_damping_strength", &Noise<coeff_t>::amplitude_damping_strength);
	py::class_<NoiseModel<coeff_t>>(m, "NoiseModel")
		.def(py::init<>())
		.def("add_unital_noise_on_gate", &NoiseModel<coeff_t>::add_unital_noise_on_gate)
		.def("add_amplitude_damping_on_gate", &NoiseModel<coeff_t>::add_amplitude_damping_on_gate);

	// Truncators (using shared_ptr holder for polymorphism)
	py::class_<Truncator<coeff_t>, TruncatorPtr>(m, "Truncator");
	py::class_<CoefficientTruncator<coeff_t>, Truncator<coeff_t>, CoeffTruncatorPtr>(m, "CoefficientTruncator")
		.def(py::init<coeff_t>());
	py::class_<WeightTruncator, Truncator<coeff_t>, WeightTruncatorPtr>(m, "WeightTruncator")
		.def(py::init<size_t>());
	py::class_<NeverTruncator, Truncator<coeff_t>, NeverTruncatorPtr>(m, "NeverTruncator").def(py::init<>());
	py::class_<LambdaTruncator, Truncator<coeff_t>, LambdaTruncatorPtr>(m, "LambdaTruncator")
		.def(py::init<LambdaPredicate_t>());
	py::class_<RuntimeMultiTruncators<coeff_t>, Truncator<coeff_t>, std::shared_ptr<RuntimeMultiTruncators<coeff_t>>>(
		m, "MultiTruncator")
		.def(py::init<const std::vector<TruncatorPtr>&>());

	// Scheduling Policies (using shared_ptr holder for polymorphism)
	py::class_<SchedulingPolicy, SchedulingPolicyPtr>(m, "SchedulingPolicy");
	py::class_<NeverPolicy, SchedulingPolicy, NeverPolicyPtr>(m, "NeverPolicy").def(py::init<>());
	py::class_<AlwaysBeforeSplittingPolicy, SchedulingPolicy, AlwaysBeforePolicyPtr>(m,
											 "AlwaysBeforeSplittingPolicy")
		.def(py::init<>());
	py::class_<AlwaysAfterSplittingPolicy, SchedulingPolicy, AlwaysAfterPolicyPtr>(m, "AlwaysAfterSplittingPolicy")
		.def(py::init<>());

	// Circuit class
	py::class_<Circuit<coeff_t>>(m, "Circuit")
		.def(py::init<unsigned, std::shared_ptr<Truncator<coeff_t>>, const NoiseModel<coeff_t>&,
			      std::shared_ptr<SchedulingPolicy>, std::shared_ptr<SchedulingPolicy>>(),
		     py::arg("nb_qubits"), py::arg("truncator") = std::make_shared<NeverTruncator>(),
		     py::arg("noise_model") = NoiseModel<coeff_t>(),
		     py::arg("merge_policy") = std::make_shared<AlwaysAfterSplittingPolicy>(),
		     py::arg("truncate_policy") = std::make_shared<AlwaysAfterSplittingPolicy>())
		.def("nb_qubits", &Circuit<coeff_t>::nb_qubits)
		// Use lambdas to resolve templated overloads
		.def(
			"add_operation",
			[](Circuit<coeff_t>& self, std::string op, unsigned q1) { self.add_operation(op, q1); },
			py::arg("op"), py::arg("qubit"))
		.def(
			"add_operation",
			[](Circuit<coeff_t>& self, std::string op, unsigned q1, coeff_t p) {
				self.add_operation(op, q1, p);
			},
			py::arg("op"), py::arg("qubit"), py::arg("param"))
		.def(
			"add_operation",
			[](Circuit<coeff_t>& self, std::string op, unsigned q1, unsigned q2) {
				self.add_operation(op, q1, q2);
			},
			py::arg("op"), py::arg("control"), py::arg("target"))
		.def("run", &Circuit<coeff_t>::run)
		.def("reset", &Circuit<coeff_t>::reset)
		.def("set_truncator", &Circuit<coeff_t>::set_truncator)
		.def("set_merge_policy", &Circuit<coeff_t>::set_merge_policy)
		.def("set_truncate_policy", &Circuit<coeff_t>::set_truncate_policy);
}
