window.BENCHMARK_DATA = {
  "lastUpdate": 1755453459956,
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
      },
      {
        "commit": {
          "author": {
            "email": "8807862+zeFresk@users.noreply.github.com",
            "name": "zeFresk",
            "username": "zeFresk"
          },
          "committer": {
            "email": "8807862+zeFresk@users.noreply.github.com",
            "name": "zeFresk",
            "username": "zeFresk"
          },
          "distinct": true,
          "id": "7c7d9671f25b72c1c62cd9f2d86083f5d605f4fc",
          "message": "README",
          "timestamp": "2025-08-16T18:56:38+02:00",
          "tree_id": "5eb8638eb8d65d50e15c157c71068c2fc6fc3752",
          "url": "https://github.com/zeFresk/pyrauli/commit/7c7d9671f25b72c1c62cd9f2d86083f5d605f4fc"
        },
        "date": 1755363493325,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 66.28300143896303,
            "unit": "iter/sec",
            "range": "stddev: 0.00017836688665334027",
            "extra": "mean: 15.086824348484793 msec\nrounds: 66"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 53525.43027866411,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013715623897739028",
            "extra": "mean: 18.6827082901305 usec\nrounds: 22231"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 55488.593319008156,
            "unit": "iter/sec",
            "range": "stddev: 0.000007084970895334331",
            "extra": "mean: 18.02172194654357 usec\nrounds: 32652"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4991.609382082887,
            "unit": "iter/sec",
            "range": "stddev: 0.000005227543209325097",
            "extra": "mean: 200.33618888317784 usec\nrounds: 4246"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1380.9712430209393,
            "unit": "iter/sec",
            "range": "stddev: 0.000010634675586538913",
            "extra": "mean: 724.1280403583592 usec\nrounds: 1338"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1337.5118229169395,
            "unit": "iter/sec",
            "range": "stddev: 0.000009697450933744242",
            "extra": "mean: 747.6569424404263 usec\nrounds: 1303"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1243.5162482297462,
            "unit": "iter/sec",
            "range": "stddev: 0.000026632946343306116",
            "extra": "mean: 804.1712373469886 usec\nrounds: 1146"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1350.6215681063952,
            "unit": "iter/sec",
            "range": "stddev: 0.000014182234447677053",
            "extra": "mean: 740.3998452372005 usec\nrounds: 1344"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 46583.43224935987,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015947077556938433",
            "extra": "mean: 21.466859604655724 usec\nrounds: 18512"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 152903.62166941736,
            "unit": "iter/sec",
            "range": "stddev: 7.364138311511492e-7",
            "extra": "mean: 6.540067456100109 usec\nrounds: 67214"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 2545867.247493498,
            "unit": "iter/sec",
            "range": "stddev: 4.162158711107257e-8",
            "extra": "mean: 392.7934580974469 nsec\nrounds: 111038"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2769600.915674147,
            "unit": "iter/sec",
            "range": "stddev: 3.726061636582202e-8",
            "extra": "mean: 361.0628500086954 nsec\nrounds: 111533"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 787034.4268300282,
            "unit": "iter/sec",
            "range": "stddev: 3.1811038539571987e-7",
            "extra": "mean: 1.2705924492118372 usec\nrounds: 116199"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 660.5917562556862,
            "unit": "iter/sec",
            "range": "stddev: 0.00015189061962449406",
            "extra": "mean: 1.5137942466435257 msec\nrounds: 596"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 429.8674502764858,
            "unit": "iter/sec",
            "range": "stddev: 0.00012642483808648024",
            "extra": "mean: 2.3262984888872404 msec\nrounds: 405"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.2733513304531792,
            "unit": "iter/sec",
            "range": "stddev: 0.08948689710114119",
            "extra": "mean: 785.3292144000079 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.6087278082680164,
            "unit": "iter/sec",
            "range": "stddev: 0.2213941680746774",
            "extra": "mean: 1.6427703588000213 sec\nrounds: 5"
          }
        ]
      },
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
          "id": "14b60ddd400f2b9bbb04bc41d26e74516e9c4f19",
          "message": "coverage CI & badges",
          "timestamp": "2025-08-16T19:54:11+02:00",
          "tree_id": "77e4f003a34897a7c7c5a01a9799ca6224d1e9db",
          "url": "https://github.com/zeFresk/pyrauli/commit/14b60ddd400f2b9bbb04bc41d26e74516e9c4f19"
        },
        "date": 1755366957135,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 63.58380494206816,
            "unit": "iter/sec",
            "range": "stddev: 0.00013866076881179475",
            "extra": "mean: 15.727275222222229 msec\nrounds: 63"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 52803.21745236025,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013675853692215576",
            "extra": "mean: 18.938239907486942 usec\nrounds: 21179"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 54990.354408928026,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013909823781683005",
            "extra": "mean: 18.185007366267197 usec\nrounds: 30816"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4943.7582440872075,
            "unit": "iter/sec",
            "range": "stddev: 0.00000557862276647217",
            "extra": "mean: 202.27526319597277 usec\nrounds: 4149"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1338.2439553008444,
            "unit": "iter/sec",
            "range": "stddev: 0.00003581810078993421",
            "extra": "mean: 747.247910994819 usec\nrounds: 1337"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1276.9561116971638,
            "unit": "iter/sec",
            "range": "stddev: 0.000010627652883408046",
            "extra": "mean: 783.1122705313107 usec\nrounds: 1242"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1210.4910541705112,
            "unit": "iter/sec",
            "range": "stddev: 0.000008628736822152116",
            "extra": "mean: 826.1110204447151 usec\nrounds: 1125"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1338.0247404828779,
            "unit": "iter/sec",
            "range": "stddev: 0.000026516884237046754",
            "extra": "mean: 747.3703360964098 usec\nrounds: 1327"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 44617.07808979885,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016082565238106275",
            "extra": "mean: 22.41294237124501 usec\nrounds: 16641"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 151307.6411832985,
            "unit": "iter/sec",
            "range": "stddev: 7.457276059620699e-7",
            "extra": "mean: 6.609051546766041 usec\nrounds: 57928"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1712912.1058415514,
            "unit": "iter/sec",
            "range": "stddev: 1.9848246796875763e-7",
            "extra": "mean: 583.8011165836798 nsec\nrounds: 193088"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 1830279.457824995,
            "unit": "iter/sec",
            "range": "stddev: 1.747338561734603e-7",
            "extra": "mean: 546.3646525259842 nsec\nrounds: 49831"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 778391.4759947527,
            "unit": "iter/sec",
            "range": "stddev: 3.1154920102563605e-7",
            "extra": "mean: 1.2847006048236083 usec\nrounds: 116064"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 660.9527396477712,
            "unit": "iter/sec",
            "range": "stddev: 0.0000754585615039705",
            "extra": "mean: 1.5129674786323009 msec\nrounds: 585"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 426.62231850425877,
            "unit": "iter/sec",
            "range": "stddev: 0.00002024949083870402",
            "extra": "mean: 2.3439936370558576 msec\nrounds: 394"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.3032136386905842,
            "unit": "iter/sec",
            "range": "stddev: 0.004151720726471601",
            "extra": "mean: 767.3338970000032 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.700066231319961,
            "unit": "iter/sec",
            "range": "stddev: 0.01449233158372339",
            "extra": "mean: 1.4284362754 sec\nrounds: 5"
          }
        ]
      },
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
          "id": "b731c86b8cd001941dc1154a279beef6026a739c",
          "message": "Added truncator + policy options for backend and estimator + per job options",
          "timestamp": "2025-08-16T20:58:55+02:00",
          "tree_id": "7802862fb2964d946878dd7a464956a2ae153eab",
          "url": "https://github.com/zeFresk/pyrauli/commit/b731c86b8cd001941dc1154a279beef6026a739c"
        },
        "date": 1755370824379,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 66.0311118500877,
            "unit": "iter/sec",
            "range": "stddev: 0.00016102548788727084",
            "extra": "mean: 15.144376218748645 msec\nrounds: 64"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 52934.44493415849,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013920473069610189",
            "extra": "mean: 18.8912909400265 usec\nrounds: 19382"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 54993.33453290504,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018714112360562801",
            "extra": "mean: 18.184021909085253 usec\nrounds: 31859"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4914.951634543067,
            "unit": "iter/sec",
            "range": "stddev: 0.000005210983771540115",
            "extra": "mean: 203.46080172424078 usec\nrounds: 4176"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1402.9442789031268,
            "unit": "iter/sec",
            "range": "stddev: 0.000012340729347762009",
            "extra": "mean: 712.7866837176431 usec\nrounds: 1388"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1344.5794468186637,
            "unit": "iter/sec",
            "range": "stddev: 0.000009508705990038341",
            "extra": "mean: 743.7269715568282 usec\nrounds: 1336"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1275.8019028637964,
            "unit": "iter/sec",
            "range": "stddev: 0.000017763478431134722",
            "extra": "mean: 783.8207465871442 usec\nrounds: 1172"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1388.0124231402353,
            "unit": "iter/sec",
            "range": "stddev: 0.000017214297855219457",
            "extra": "mean: 720.4546467513618 usec\nrounds: 1339"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 47382.486742289926,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015068370465153637",
            "extra": "mean: 21.10484418935061 usec\nrounds: 19344"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 153416.18653433875,
            "unit": "iter/sec",
            "range": "stddev: 9.055512399123677e-7",
            "extra": "mean: 6.518217031657038 usec\nrounds: 56812"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1782052.0110121113,
            "unit": "iter/sec",
            "range": "stddev: 2.3579177724368856e-7",
            "extra": "mean: 561.15084959392 nsec\nrounds: 187266"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2835489.608689773,
            "unit": "iter/sec",
            "range": "stddev: 4.192924594363512e-8",
            "extra": "mean: 352.67277895688756 nsec\nrounds: 135612"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 774514.2150033158,
            "unit": "iter/sec",
            "range": "stddev: 3.180654346409982e-7",
            "extra": "mean: 1.2911318870961186 usec\nrounds: 106758"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 681.0497365736512,
            "unit": "iter/sec",
            "range": "stddev: 0.00002753601806581493",
            "extra": "mean: 1.4683215429037264 msec\nrounds: 606"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 422.16827715769034,
            "unit": "iter/sec",
            "range": "stddev: 0.00005618129511411179",
            "extra": "mean: 2.3687236917293886 msec\nrounds: 399"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.2788965103052516,
            "unit": "iter/sec",
            "range": "stddev: 0.0031613912193512598",
            "extra": "mean: 781.9240977999982 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.6735784180900971,
            "unit": "iter/sec",
            "range": "stddev: 0.00990149153861304",
            "extra": "mean: 1.4846081364000014 sec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 363.953697697295,
            "unit": "iter/sec",
            "range": "stddev: 0.00013677897907015977",
            "extra": "mean: 2.7476022536023605 msec\nrounds: 347"
          }
        ]
      },
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
          "id": "a66c87c678c28c8273e75b8591db7cbb02a1e0ab",
          "message": "Better documentation",
          "timestamp": "2025-08-17T19:56:14+02:00",
          "tree_id": "c1c9a3f813bc80cf0fe238eb61caa4d53ed431f9",
          "url": "https://github.com/zeFresk/pyrauli/commit/a66c87c678c28c8273e75b8591db7cbb02a1e0ab"
        },
        "date": 1755453459429,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 66.53579640061231,
            "unit": "iter/sec",
            "range": "stddev: 0.00015840931128541225",
            "extra": "mean: 15.029503727271793 msec\nrounds: 66"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024clifford_run",
            "value": 47695.05748755696,
            "unit": "iter/sec",
            "range": "stddev: 0.000001374765302515726",
            "extra": "mean: 20.966533068146266 usec\nrounds: 30921"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 53173.02077325187,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013710185488759784",
            "extra": "mean: 18.806529805111985 usec\nrounds: 24375"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 55000.72150644293,
            "unit": "iter/sec",
            "range": "stddev: 0.000001583142032587547",
            "extra": "mean: 18.181579670420454 usec\nrounds: 30645"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4930.441345336553,
            "unit": "iter/sec",
            "range": "stddev: 0.00001101507431995201",
            "extra": "mean: 202.82159951985793 usec\nrounds: 3748"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1373.7373853262131,
            "unit": "iter/sec",
            "range": "stddev: 0.00006019769177487711",
            "extra": "mean: 727.9411703296813 usec\nrounds: 1274"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1333.8446958705051,
            "unit": "iter/sec",
            "range": "stddev: 0.000030294949572661213",
            "extra": "mean: 749.7124688473357 usec\nrounds: 1284"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1231.7303713067683,
            "unit": "iter/sec",
            "range": "stddev: 0.000013812859238134833",
            "extra": "mean: 811.8659921806419 usec\nrounds: 1151"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1364.580838053683,
            "unit": "iter/sec",
            "range": "stddev: 0.000011460147454611523",
            "extra": "mean: 732.8257675274932 usec\nrounds: 1355"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 47509.23142823509,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017008020559322873",
            "extra": "mean: 21.048540882218788 usec\nrounds: 18908"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 151562.90053888262,
            "unit": "iter/sec",
            "range": "stddev: 7.542988529258304e-7",
            "extra": "mean: 6.597920707801812 usec\nrounds: 54482"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1767149.158009399,
            "unit": "iter/sec",
            "range": "stddev: 1.9876313918701476e-7",
            "extra": "mean: 565.8831884493823 nsec\nrounds: 166362"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2743546.5590202212,
            "unit": "iter/sec",
            "range": "stddev: 4.7993400543681934e-8",
            "extra": "mean: 364.49171847009626 nsec\nrounds: 103115"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 765436.6751264512,
            "unit": "iter/sec",
            "range": "stddev: 3.069418195122744e-7",
            "extra": "mean: 1.3064438019445548 usec\nrounds: 101338"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 683.1365905440362,
            "unit": "iter/sec",
            "range": "stddev: 0.0001023523710621397",
            "extra": "mean: 1.4638360963853807 msec\nrounds: 581"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 420.8327377122126,
            "unit": "iter/sec",
            "range": "stddev: 0.00003790288286214382",
            "extra": "mean: 2.3762409869449184 msec\nrounds: 383"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.20428007216855,
            "unit": "iter/sec",
            "range": "stddev: 0.018896979788989902",
            "extra": "mean: 830.3716245999965 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.5458303005314318,
            "unit": "iter/sec",
            "range": "stddev: 0.08644705623312261",
            "extra": "mean: 1.8320712481999977 sec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 360.24220069073795,
            "unit": "iter/sec",
            "range": "stddev: 0.00011973800925628562",
            "extra": "mean: 2.7759102017547455 msec\nrounds: 342"
          }
        ]
      }
    ]
  }
}