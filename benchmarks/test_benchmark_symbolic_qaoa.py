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


def test_qaoa_N4P1_ev_evaluate_optimized(maxcut_qaoa_N4P1, benchmark):
    qc, obs = maxcut_qaoa_N4P1
    ev_opt = qc.run(obs).expectation_value().optimize()

    def eval_fn(opt):
        return opt.evaluate({"tz": 0.616, "tx": 0.393})

    benchmark(eval_fn, ev_opt)


@pytest.fixture(scope="module")
def maxcut_qaoa_N4P3():
    """Fixture"""
    obs = SymbolicObservable(["ZZII", "ZIZI", "IZZI", "ZIIZ", "IZIZ", "IIZZ"])
    qc = SymbolicCircuit(4)
    qc.add_operation("h", 0)
    qc.add_operation("h", 1)
    qc.add_operation("h", 2)
    qc.add_operation("h", 3)
    rzz(qc, 0, 1, "g0")
    rzz(qc, 0, 3, "g0")
    rzz(qc, 0, 2, "g0")
    rzz(qc, 1, 2, "g0")
    rzz(qc, 1, 3, "g0")
    rzz(qc, 2, 3, "g0")
    rx(qc, 0, "b0")
    rx(qc, 1, "b0")
    rx(qc, 2, "b0")
    rx(qc, 3, "b0")
    rzz(qc, 0, 1, "g1")
    rzz(qc, 0, 3, "g1")
    rzz(qc, 0, 2, "g1")
    rzz(qc, 1, 2, "g1")
    rzz(qc, 1, 3, "g1")
    rzz(qc, 2, 3, "g1")
    rx(qc, 0, "b1")
    rx(qc, 1, "b1")
    rx(qc, 2, "b1")
    rx(qc, 3, "b1")
    rzz(qc, 0, 1, "g2")
    rzz(qc, 0, 3, "g2")
    rzz(qc, 0, 2, "g2")
    rzz(qc, 1, 2, "g2")
    rzz(qc, 1, 3, "g2")
    rzz(qc, 2, 3, "g2")
    rx(qc, 0, "b2")
    rx(qc, 1, "b2")
    rx(qc, 2, "b2")
    rx(qc, 3, "b2")
    return qc, obs


def test_HARD_qaoa_N4P3_run(maxcut_qaoa_N4P3, benchmark):
    qc, obs = maxcut_qaoa_N4P3

    benchmark(qc.run, obs)


def test_HARD_qaoa_N4P3_ev_evaluate_optimized(maxcut_qaoa_N4P3, benchmark):
    qc, obs = maxcut_qaoa_N4P3
    ev_opt = qc.run(obs).expectation_value().optimize()

    def eval_fn(opt):
        return opt.evaluate(
            {
                "g0": 0.422,
                "g1": 0.798,
                "g2": 0.937,
                "b0": 0.609,
                "b1": 0.459,
                "b2": 0.235,
            }
        )

    benchmark(eval_fn, ev_opt)
