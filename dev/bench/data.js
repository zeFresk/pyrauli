window.BENCHMARK_DATA = {
  "lastUpdate": 1755363213254,
  "repoUrl": "https://github.com/zeFresk/pyrauli",
  "entries": {
    "Pytest benchmarks": [
      {
        "commit": {
          "author": {
            "email": "8807862+zeFresk@users.noreply.github.com",
            "name": "zeFresk",
            "username": "zeFresk"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "c637112aab3d82e724a4ac669c3b25984adbe21e",
          "message": "Added CI, tests, documentation and benchmarks",
          "timestamp": "2025-08-16T18:51:57+02:00",
          "tree_id": "e6d0359d5392b12110f4a0bc12dcefc822e7ae72",
          "url": "https://github.com/zeFresk/pyrauli/commit/c637112aab3d82e724a4ac669c3b25984adbe21e"
        },
        "date": 1755363212631,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 67.32814385884858,
            "unit": "iter/sec",
            "range": "stddev: 0.0006952463486425621",
            "extra": "mean: 14.852629861540068 msec\nrounds: 65"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 53069.00467376373,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014007465738889685",
            "extra": "mean: 18.84339090486806 usec\nrounds: 21000"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 55345.96523622479,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014686780957706933",
            "extra": "mean: 18.0681644223179 usec\nrounds: 30969"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4923.396535558841,
            "unit": "iter/sec",
            "range": "stddev: 0.000010666360380703473",
            "extra": "mean: 203.11181371997554 usec\nrounds: 3892"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1384.8521876774366,
            "unit": "iter/sec",
            "range": "stddev: 0.00004335393292609789",
            "extra": "mean: 722.0987256965814 usec\nrounds: 1327"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1323.7802109678585,
            "unit": "iter/sec",
            "range": "stddev: 0.000012137314272997477",
            "extra": "mean: 755.412410394674 usec\nrounds: 1116"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1265.746991692301,
            "unit": "iter/sec",
            "range": "stddev: 0.000025087145480885675",
            "extra": "mean: 790.0473053173148 usec\nrounds: 1166"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1371.2294185732555,
            "unit": "iter/sec",
            "range": "stddev: 0.000010236504211010837",
            "extra": "mean: 729.2725684375163 usec\nrounds: 1337"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 46796.815473227995,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016468283120250064",
            "extra": "mean: 21.368975428938967 usec\nrounds: 16320"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 152192.24003922872,
            "unit": "iter/sec",
            "range": "stddev: 8.297212560570048e-7",
            "extra": "mean: 6.570637239732081 usec\nrounds: 28534"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1743825.4677129132,
            "unit": "iter/sec",
            "range": "stddev: 2.0928363608421245e-7",
            "extra": "mean: 573.4518840991204 nsec\nrounds: 181489"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2785678.4595507225,
            "unit": "iter/sec",
            "range": "stddev: 3.829714635330936e-8",
            "extra": "mean: 358.97897568597386 nsec\nrounds: 88645"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 780357.397888855,
            "unit": "iter/sec",
            "range": "stddev: 3.847452850168498e-7",
            "extra": "mean: 1.2814641120919166 usec\nrounds: 101441"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 687.2031127722431,
            "unit": "iter/sec",
            "range": "stddev: 0.00003429907286638593",
            "extra": "mean: 1.4551738509534746 msec\nrounds: 577"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 426.9797748383327,
            "unit": "iter/sec",
            "range": "stddev: 0.000027469862152486722",
            "extra": "mean: 2.3420313067021263 msec\nrounds: 388"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.1586219502997943,
            "unit": "iter/sec",
            "range": "stddev: 0.056698186722869595",
            "extra": "mean: 863.094298999988 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.5713329824581782,
            "unit": "iter/sec",
            "range": "stddev: 0.13434518015286517",
            "extra": "mean: 1.7502927901999783 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}