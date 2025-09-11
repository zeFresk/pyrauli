import pytest
from pyrauli import SymbolicObservable, SymbolicCircuit

def rzz(qc, q1, q2, v):
    qc.add_operation("cx", q1, q2)
    qc.add_operation("rz", q2, v)
    qc.add_operation("cx", q1, q2)

def rx(qc, q, v):
    qc.add_operation("h", q)
    qc.add_operation("rz", q, v)
    qc.add_operation("h", q)
    
@pytest.fixture(scope="module")
def maxcut_qaoa_N4P1():
    """Fixture"""
    obs = SymbolicObservable(["ZZII", "ZIZI", "IZZI", "ZIIZ", "IZIZ", "IIZZ"])
    qc = SymbolicCircuit(4)

    for i in range(4):
        qc.add_operation("h", i)

    rzz(qc, 0, 1, "tz")
    rzz(qc, 0, 3, "tz")
    rzz(qc, 0, 2, "tz")

    rx(qc, 0, "tx")

    rzz(qc, 1, 2, "tz")
    rzz(qc, 1, 3, "tz")

    rx(qc, 1, "tx")
    rzz(qc, 2, 3, "tz")

    rx(qc, 2, "tx")
    rx(qc, 3, "tx")

    return qc, obs

def test_qaoa_N4P1_run(maxcut_qaoa_N4P1, benchmark):
    qc, obs = maxcut_qaoa_N4P1

    benchmark(qc.run, obs)
