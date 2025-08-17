.. _explanation_theory:

Core Concepts
=============

This section explains the theoretical foundations of ``pyrauli``. Understanding
these concepts will help you use the library more effectively and decide when
it is the right tool for your problem.

The Heisenberg Picture vs. The Schrödinger Picture
---------------------------------------------------

Most quantum circuit simulators operate in the **Schrödinger picture**. In this
view, the quantum state (a state vector :math:`|\psi\rangle` of size
:math:`2^N`) evolves in time, while the operators (like observables :math:`O`)
are typically fixed.

- **Schrödinger Picture**: State evolves, operator is fixed.
  - State evolution: :math:`|\psi(t)\rangle = U(t) |\psi(0)\rangle`
  - Expectation value: :math:`\langle \psi(t) | O | \psi(t) \rangle`

``pyrauli`` operates in the **Heisenberg picture**. Here, the roles are
reversed: the state is considered fixed at its initial value
(:math:`|\psi(0)\rangle`), and the operators evolve instead.

- **Heisenberg Picture**: State is fixed, operator evolves.
  - Operator evolution: :math:`O(t) = U^\dagger(t) O U(t)`
  - Expectation value: :math:`\langle \psi(0) | O(t) | \psi(0) \rangle`

The two pictures are mathematically equivalent, but they can have vastly
different computational costs. ``pyrauli`` is optimized for the common case
where the initial state is :math:`|0\rangle^{\otimes N}`, making the
Heisenberg calculation particularly efficient.

Pauli Back-Propagation
----------------------

``pyrauli`` implements the Heisenberg evolution using a technique called
**Pauli back-propagation**.

An observable :math:`O` is represented as a linear combination of Pauli strings
(e.g., :math:`c_1 IXYZ + c_2 ZIZI + \dots`). A circuit :math:`U` is a sequence
of gates :math:`U = G_k \dots G_2 G_1`.

The evolved observable is :math:`O' = U^\dagger O U = G_1^\dagger G_2^\dagger \dots G_k^\dagger O G_k \dots G_2 G_1`.

``pyrauli`` calculates this by starting with the initial observable :math:`O`
and successively applying the conjugation for each gate **in reverse order**
(hence "back-propagation"):

1.  Start with :math:`O_k = O`.
2.  Compute :math:`O_{k-1} = G_k^\dagger O_k G_k`.
3.  Compute :math:`O_{k-2} = G_{k-1}^\dagger O_{k-1} G_{k-1}`.
4. ...and so on, until...
5.  The final observable is :math:`O_0 = G_1^\dagger O_1 G_1`.

The key insight is that if :math:`O_i` is a Pauli string, then for many common
quantum gates :math:`G_{i+1}`, the result
:math:`G_{i+1}^\dagger O_i G_{i+1}` is also a simple combination of one or two
Pauli strings. ``pyrauli``'s C++ backend, `ProPauli`_, is highly optimized to
perform these Pauli algebra transformations very quickly.

Without any merge or truncation, the number terms in the observable can grow exponentially with the number of `Rz` gates, which is
why complexity management via truncators is an important feature.

The `pyrauli` + `ProPauli` Architecture
---------------------------------------

The library is composed of two distinct parts that work together:

- `pyrauli`_ **(Python Frontend)**: This is the library you interact with. It
  provides the user-facing API (:py:class:`~pyrauli.Circuit`, :py:class:`~pyrauli.Observable`), handles
  integration with the Python ecosystem (e.g., Qiskit), and orchestrates the
  simulation logic.

- `ProPauli`_ **(C++ Backend)**: This is the high-performance engine. It
  implements the core data structures for representing Pauli strings
  efficiently, contains the optimized C++ routines for applying gate
  conjugations, and manages the computationally intensive work.

This separation of concerns allows `pyrauli`_ to offer both a high-level,
easy-to-use Python interface and the raw performance of compiled C++ code.

.. _ProPauli: https://github.com/zeFresk/ProPauli
.. _pyrauli: https://github.com/zeFresk/pyrauli
