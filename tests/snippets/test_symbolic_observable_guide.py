
def test_symbolic_observable_snippet():
    # [symbolic_obs_init]
    from pyrauli import SymbolicObservable, SymbolicPauliTerm

    # From a single Pauli string with a symbolic coefficient
    obs1 = SymbolicObservable("X", "a")
    print(obs1)

    # From a list of Pauli strings (default coefficient is 1.0)
    obs2 = SymbolicObservable(["XX", "YY"])
    print(obs2)

    # From a list of PauliTerms with symbolic coefficients
    obs3 = SymbolicObservable([
        SymbolicPauliTerm("X", "a"),
        SymbolicPauliTerm("Y", "b")
    ])
    print(obs3)
    # [symbolic_obs_init]

    # [symbolic_obs_simplify]
    from pyrauli import SymbolicObservable, SymbolicPauliTerm

    # Create an observable with redundant terms
    obs = SymbolicObservable(["X", "X", "Y"])
    obs.merge() # ['2.000 * X', '1.000 * Y']

    # Add another term with a symbolic coefficient
    obs = SymbolicObservable([
        SymbolicPauliTerm("X", 2.0),
        SymbolicPauliTerm("Y", 1.0),
        SymbolicPauliTerm("X", "a")
    ])

    obs.merge()
    print(f"Merged observable: {obs}")

    # Simplify the coefficients
    obs.simplify()
    print(f"Simplified observable: {obs}")

    # Simplify and substitute a variable
    obs.simplify({"a": 3.0})
    print(f"Simplified and substituted observable: {obs}")
    # [symbolic_obs_simplify]
