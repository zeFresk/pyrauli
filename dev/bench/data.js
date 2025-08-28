window.BENCHMARK_DATA = {
  "lastUpdate": 1756418341011,
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
          "id": "36166704f13166aae63bc4055130dfdd2ef5cb4b",
          "message": "Added publish workflow",
          "timestamp": "2025-08-17T20:24:41+02:00",
          "tree_id": "2f1974d5d71af214b55a3db3c7d0221b7b260ff2",
          "url": "https://github.com/zeFresk/pyrauli/commit/36166704f13166aae63bc4055130dfdd2ef5cb4b"
        },
        "date": 1755455179695,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 66.34109491959367,
            "unit": "iter/sec",
            "range": "stddev: 0.00020930185413657633",
            "extra": "mean: 15.073613138462878 msec\nrounds: 65"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024clifford_run",
            "value": 47307.27121227792,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014473663810862722",
            "extra": "mean: 21.138399539317845 usec\nrounds: 32565"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 51048.73595846602,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030531460284797905",
            "extra": "mean: 19.58912363302422 usec\nrounds: 24233"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 54307.6448645273,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013972774263627656",
            "extra": "mean: 18.413613819832218 usec\nrounds: 30970"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4896.843733245119,
            "unit": "iter/sec",
            "range": "stddev: 0.00000499762688355047",
            "extra": "mean: 204.21317372472163 usec\nrounds: 4156"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1357.2986475297741,
            "unit": "iter/sec",
            "range": "stddev: 0.000011958491994362888",
            "extra": "mean: 736.757530717324 usec\nrounds: 1351"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1305.6878003955283,
            "unit": "iter/sec",
            "range": "stddev: 0.000012262797700241498",
            "extra": "mean: 765.8798678344647 usec\nrounds: 1256"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1245.044284857653,
            "unit": "iter/sec",
            "range": "stddev: 0.000008891564478017477",
            "extra": "mean: 803.1842820067486 usec\nrounds: 1156"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1352.1188255972545,
            "unit": "iter/sec",
            "range": "stddev: 0.000012734699138550366",
            "extra": "mean: 739.5799696511751 usec\nrounds: 1318"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 47548.99549549128,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018444174929432578",
            "extra": "mean: 21.030938499948387 usec\nrounds: 14439"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 151462.94881005472,
            "unit": "iter/sec",
            "range": "stddev: 7.632029452499305e-7",
            "extra": "mean: 6.602274733565837 usec\nrounds: 60717"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1749684.3072423453,
            "unit": "iter/sec",
            "range": "stddev: 1.9979182806984936e-7",
            "extra": "mean: 571.5316733771746 nsec\nrounds: 175747"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2744551.9149349327,
            "unit": "iter/sec",
            "range": "stddev: 4.810474746010359e-8",
            "extra": "mean: 364.3582016278631 nsec\nrounds: 102376"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 784213.0580602464,
            "unit": "iter/sec",
            "range": "stddev: 3.1497171805377733e-7",
            "extra": "mean: 1.275163668497823 usec\nrounds: 119962"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 655.0709341917632,
            "unit": "iter/sec",
            "range": "stddev: 0.00004609410217868469",
            "extra": "mean: 1.526552237024248 msec\nrounds: 578"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 418.55274029628873,
            "unit": "iter/sec",
            "range": "stddev: 0.00019817927655308345",
            "extra": "mean: 2.389185170050759 msec\nrounds: 394"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.3062139297627968,
            "unit": "iter/sec",
            "range": "stddev: 0.008376317087055092",
            "extra": "mean: 765.5713794000008 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.6952708688924745,
            "unit": "iter/sec",
            "range": "stddev: 0.011214279749434283",
            "extra": "mean: 1.4382883632000016 sec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 362.2014294222927,
            "unit": "iter/sec",
            "range": "stddev: 0.0000960958634848623",
            "extra": "mean: 2.7608946811584625 msec\nrounds: 345"
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
          "id": "d37c2a8917f5709976dc8bad4514592515d9d839",
          "message": "CI for deploying to pip",
          "timestamp": "2025-08-17T21:01:18+02:00",
          "tree_id": "c5c7926cd760184714aa19d56c4cc58d14095515",
          "url": "https://github.com/zeFresk/pyrauli/commit/d37c2a8917f5709976dc8bad4514592515d9d839"
        },
        "date": 1755457366702,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 66.39042312958838,
            "unit": "iter/sec",
            "range": "stddev: 0.00029992917469091304",
            "extra": "mean: 15.062413415382007 msec\nrounds: 65"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024clifford_run",
            "value": 47692.39397024338,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014720036528692027",
            "extra": "mean: 20.967704003785762 usec\nrounds: 33916"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 53496.900612768724,
            "unit": "iter/sec",
            "range": "stddev: 0.000001442568829684686",
            "extra": "mean: 18.69267169771922 usec\nrounds: 24316"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 55899.11849359161,
            "unit": "iter/sec",
            "range": "stddev: 0.000001418394764078754",
            "extra": "mean: 17.889369760180422 usec\nrounds: 32229"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4996.053959686736,
            "unit": "iter/sec",
            "range": "stddev: 0.0000055182446962283655",
            "extra": "mean: 200.157966280793 usec\nrounds: 3885"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1411.0813132463554,
            "unit": "iter/sec",
            "range": "stddev: 0.000011691087737144664",
            "extra": "mean: 708.6763821564504 usec\nrounds: 1345"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1356.4432079096935,
            "unit": "iter/sec",
            "range": "stddev: 0.000010528534867877624",
            "extra": "mean: 737.2221661539523 usec\nrounds: 1300"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1237.7750199057662,
            "unit": "iter/sec",
            "range": "stddev: 0.000009679154723345728",
            "extra": "mean: 807.9012614716781 usec\nrounds: 1155"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1376.6688108016767,
            "unit": "iter/sec",
            "range": "stddev: 0.00002362120569379909",
            "extra": "mean: 726.391120474117 usec\nrounds: 1353"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 47213.21534396849,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016452093532759977",
            "extra": "mean: 21.1805104294332 usec\nrounds: 20375"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 153098.39731445504,
            "unit": "iter/sec",
            "range": "stddev: 8.037638348397062e-7",
            "extra": "mean: 6.531747017220952 usec\nrounds: 57664"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1766580.8344857944,
            "unit": "iter/sec",
            "range": "stddev: 2.3227874321832516e-7",
            "extra": "mean: 566.0652377059632 nsec\nrounds: 193799"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 1894785.2303815726,
            "unit": "iter/sec",
            "range": "stddev: 2.1155670034135376e-7",
            "extra": "mean: 527.7642995974903 nsec\nrounds: 50386"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 788052.4946575443,
            "unit": "iter/sec",
            "range": "stddev: 3.188824166827754e-7",
            "extra": "mean: 1.2689509985430087 usec\nrounds: 111895"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 667.6953573933906,
            "unit": "iter/sec",
            "range": "stddev: 0.00016843130046871659",
            "extra": "mean: 1.4976890118030628 msec\nrounds: 593"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 427.934853708129,
            "unit": "iter/sec",
            "range": "stddev: 0.000021941593664647883",
            "extra": "mean: 2.3368042853598587 msec\nrounds: 403"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.321538764785639,
            "unit": "iter/sec",
            "range": "stddev: 0.007819153781591454",
            "extra": "mean: 756.6936564000116 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.6822232662712454,
            "unit": "iter/sec",
            "range": "stddev: 0.037646781441687184",
            "extra": "mean: 1.4657958023999869 sec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 367.3877348680478,
            "unit": "iter/sec",
            "range": "stddev: 0.00008534306832923222",
            "extra": "mean: 2.721919936600941 msec\nrounds: 347"
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
          "id": "1794375a5b20cd172f17c6554b529885cb7584ae",
          "message": "Merge branch 'pypi'",
          "timestamp": "2025-08-17T21:06:28+02:00",
          "tree_id": "8ced22c08acbc387fd1b38d5bb6b74aedfda2cc4",
          "url": "https://github.com/zeFresk/pyrauli/commit/1794375a5b20cd172f17c6554b529885cb7584ae"
        },
        "date": 1755457701721,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 65.8592378148887,
            "unit": "iter/sec",
            "range": "stddev: 0.00035757887159300637",
            "extra": "mean: 15.1838987692313 msec\nrounds: 65"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024clifford_run",
            "value": 47330.672637188756,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013827515879153698",
            "extra": "mean: 21.127948205288718 usec\nrounds: 33710"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 53274.936668033224,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013818670322835315",
            "extra": "mean: 18.77055258143618 usec\nrounds: 24134"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 55244.21765032336,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013981258477234719",
            "extra": "mean: 18.101441970445695 usec\nrounds: 30450"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4926.0593287003885,
            "unit": "iter/sec",
            "range": "stddev: 0.000005616825975260612",
            "extra": "mean: 203.00202114370876 usec\nrounds: 4162"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1349.840212613279,
            "unit": "iter/sec",
            "range": "stddev: 0.000013500186173160814",
            "extra": "mean: 740.8284259542163 usec\nrounds: 1310"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1318.205766517747,
            "unit": "iter/sec",
            "range": "stddev: 0.000047736058960977314",
            "extra": "mean: 758.6069075100933 usec\nrounds: 1265"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1236.121963919585,
            "unit": "iter/sec",
            "range": "stddev: 0.000011839425285219159",
            "extra": "mean: 808.9816613476615 usec\nrounds: 1128"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1362.5401592325238,
            "unit": "iter/sec",
            "range": "stddev: 0.000013242624875262312",
            "extra": "mean: 733.923321983602 usec\nrounds: 1351"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 46984.439400527495,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019158859611453923",
            "extra": "mean: 21.283642260266557 usec\nrounds: 20104"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 151631.28855478833,
            "unit": "iter/sec",
            "range": "stddev: 7.281472253432978e-7",
            "extra": "mean: 6.5949449452754205 usec\nrounds: 57797"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1745988.0264852382,
            "unit": "iter/sec",
            "range": "stddev: 2.1052806515049855e-7",
            "extra": "mean: 572.7416138202565 nsec\nrounds: 195351"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2694229.840414569,
            "unit": "iter/sec",
            "range": "stddev: 3.7116358854296335e-8",
            "extra": "mean: 371.16358263114154 nsec\nrounds: 107435"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 775607.5015720209,
            "unit": "iter/sec",
            "range": "stddev: 3.4563707604282164e-7",
            "extra": "mean: 1.2893119238444375 usec\nrounds: 106417"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 679.7940069878107,
            "unit": "iter/sec",
            "range": "stddev: 0.00003062955999082028",
            "extra": "mean: 1.4710338569047297 msec\nrounds: 601"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 425.86678544014455,
            "unit": "iter/sec",
            "range": "stddev: 0.000023940809459394307",
            "extra": "mean: 2.348152131579065 msec\nrounds: 380"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.2864145756641538,
            "unit": "iter/sec",
            "range": "stddev: 0.002874152055479808",
            "extra": "mean: 777.3543762000031 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.6714939739036918,
            "unit": "iter/sec",
            "range": "stddev: 0.01320678686234276",
            "extra": "mean: 1.4892166406 sec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 362.32302516211,
            "unit": "iter/sec",
            "range": "stddev: 0.00014463709670052956",
            "extra": "mean: 2.7599681238932616 msec\nrounds: 339"
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
          "id": "b7b025cf6affa9b95344a9e8323e94c356c3bd6d",
          "message": "Fix bench url in README",
          "timestamp": "2025-08-18T10:53:16+02:00",
          "tree_id": "e208aff7a41ca74b52575445ca0de2ca1fe3672c",
          "url": "https://github.com/zeFresk/pyrauli/commit/b7b025cf6affa9b95344a9e8323e94c356c3bd6d"
        },
        "date": 1755507309808,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 65.098262501136,
            "unit": "iter/sec",
            "range": "stddev: 0.00033927847313384573",
            "extra": "mean: 15.361393093748843 msec\nrounds: 64"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024clifford_run",
            "value": 48113.7958843037,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013387796572327875",
            "extra": "mean: 20.784059574194455 usec\nrounds: 34008"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 51739.02585738623,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013131085576867294",
            "extra": "mean: 19.327770158572488 usec\nrounds: 25535"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 54023.43079934109,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013148383706081887",
            "extra": "mean: 18.510486749986207 usec\nrounds: 32717"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 4953.872782766714,
            "unit": "iter/sec",
            "range": "stddev: 0.000005280467825348052",
            "extra": "mean: 201.8622689461768 usec\nrounds: 3919"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1386.4267066381128,
            "unit": "iter/sec",
            "range": "stddev: 0.000010126850931482304",
            "extra": "mean: 721.2786620540926 usec\nrounds: 1373"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1342.7154717818187,
            "unit": "iter/sec",
            "range": "stddev: 0.000009729690019204294",
            "extra": "mean: 744.7594229870411 usec\nrounds: 1279"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1252.0132842026785,
            "unit": "iter/sec",
            "range": "stddev: 0.00000949503533528703",
            "extra": "mean: 798.7135700695312 usec\nrounds: 1156"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1365.7752911616308,
            "unit": "iter/sec",
            "range": "stddev: 0.000009898634747739776",
            "extra": "mean: 732.1848670651169 usec\nrounds: 1339"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 46866.914484121764,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014717745160483689",
            "extra": "mean: 21.33701377629189 usec\nrounds: 19236"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 150690.97291104772,
            "unit": "iter/sec",
            "range": "stddev: 7.938354799465272e-7",
            "extra": "mean: 6.6360975756012675 usec\nrounds: 61501"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 1739616.170640716,
            "unit": "iter/sec",
            "range": "stddev: 2.3782448196561745e-7",
            "extra": "mean: 574.8394484236665 nsec\nrounds: 196890"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2669685.351354633,
            "unit": "iter/sec",
            "range": "stddev: 5.6380752893123544e-8",
            "extra": "mean: 374.57597746213315 nsec\nrounds: 97088"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 772921.2219143477,
            "unit": "iter/sec",
            "range": "stddev: 3.278253014443684e-7",
            "extra": "mean: 1.2937929140090507 usec\nrounds: 108496"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 672.6403667228274,
            "unit": "iter/sec",
            "range": "stddev: 0.000029015463320015108",
            "extra": "mean: 1.4866785424611106 msec\nrounds: 577"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 430.4786173820913,
            "unit": "iter/sec",
            "range": "stddev: 0.000018225261860817514",
            "extra": "mean: 2.3229957531488807 msec\nrounds: 397"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 1.2985351185851808,
            "unit": "iter/sec",
            "range": "stddev: 0.017166269032036132",
            "extra": "mean: 770.098540799998 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 0.66063531490472,
            "unit": "iter/sec",
            "range": "stddev: 0.013429986256861634",
            "extra": "mean: 1.513694435399998 sec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 366.2163007045427,
            "unit": "iter/sec",
            "range": "stddev: 0.00008261908715471601",
            "extra": "mean: 2.730626676300746 msec\nrounds: 346"
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
          "id": "18e055c516d9f554c563e50e020dc706ca07264f",
          "message": "Merge pull request #6 from zeFresk/propauli_v2\n\nUpdate to Propauli v2",
          "timestamp": "2025-08-28T23:57:44+02:00",
          "tree_id": "4b521ebe60c74f0a04395b457e52d3e084c13d12",
          "url": "https://github.com/zeFresk/pyrauli/commit/18e055c516d9f554c563e50e020dc706ca07264f"
        },
        "date": 1756418339757,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024_construction",
            "value": 69.10294067091871,
            "unit": "iter/sec",
            "range": "stddev: 0.0001585755518424007",
            "extra": "mean: 14.47116418333323 msec\nrounds: 60"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit1024x1024clifford_run",
            "value": 47378.31625383987,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015290865360633938",
            "extra": "mean: 21.106701948677905 usec\nrounds: 28173"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_without_truncator",
            "value": 122481.41860822197,
            "unit": "iter/sec",
            "range": "stddev: 8.625518628056664e-7",
            "extra": "mean: 8.164503737490772 usec\nrounds: 49097"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_truncator",
            "value": 125934.50143021582,
            "unit": "iter/sec",
            "range": "stddev: 8.299910591033316e-7",
            "extra": "mean: 7.940635716528648 usec\nrounds: 60129"
          },
          {
            "name": "benchmarks/test_benchmark_circuit.py::test_circuit16x32_run_with_noise_model_and_truncators",
            "value": 8853.933238477728,
            "unit": "iter/sec",
            "range": "stddev: 0.000006967467591133373",
            "extra": "mean: 112.94415409121964 usec\nrounds: 7846"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024pauli",
            "value": 1349.7656026901054,
            "unit": "iter/sec",
            "range": "stddev: 0.000009612974631471161",
            "extra": "mean: 740.8693761398151 usec\nrounds: 1316"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024clifford",
            "value": 1289.7599839644604,
            "unit": "iter/sec",
            "range": "stddev: 0.00001002804670012145",
            "extra": "mean: 775.3380570284116 usec\nrounds: 1245"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024cx",
            "value": 1271.1789193642642,
            "unit": "iter/sec",
            "range": "stddev: 0.000014899909580173571",
            "extra": "mean: 786.671321217406 usec\nrounds: 1183"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_1024unital_noise",
            "value": 1352.4759768457202,
            "unit": "iter/sec",
            "range": "stddev: 0.000009552168887882501",
            "extra": "mean: 739.384667173332 usec\nrounds: 1316"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8rz",
            "value": 82700.93766645183,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015230001878028845",
            "extra": "mean: 12.09176132963794 usec\nrounds: 30385"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_1024observable_apply_8amplitude_damping",
            "value": 152022.5878104734,
            "unit": "iter/sec",
            "range": "stddev: 7.494358170256457e-7",
            "extra": "mean: 6.577969855681579 usec\nrounds: 50590"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_merge",
            "value": 3194727.787354482,
            "unit": "iter/sec",
            "range": "stddev: 3.620894953103688e-8",
            "extra": "mean: 313.0157141895613 nsec\nrounds: 162576"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_coefficient",
            "value": 2988987.2533188034,
            "unit": "iter/sec",
            "range": "stddev: 3.9666215388488324e-8",
            "extra": "mean: 334.56148027719297 nsec\nrounds: 129300"
          },
          {
            "name": "benchmarks/test_benchmark_observable.py::test_observable_truncate_lambda",
            "value": 890577.3775842184,
            "unit": "iter/sec",
            "range": "stddev: 3.166040893800719e-7",
            "extra": "mean: 1.1228670581242493 usec\nrounds: 113418"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_1024observable_conversion",
            "value": 663.0252970965186,
            "unit": "iter/sec",
            "range": "stddev: 0.0000503018202384613",
            "extra": "mean: 1.5082380783646436 msec\nrounds: 587"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_32x32circuit_conversion",
            "value": 420.9984137868535,
            "unit": "iter/sec",
            "range": "stddev: 0.00002722222033558772",
            "extra": "mean: 2.3753058616184908 msec\nrounds: 383"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_run8x8",
            "value": 4.131517328527402,
            "unit": "iter/sec",
            "range": "stddev: 0.0004676628958986732",
            "extra": "mean: 242.04182639999487 msec\nrounds: 5"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8",
            "value": 6.401246198999511,
            "unit": "iter/sec",
            "range": "stddev: 0.0004838565003370566",
            "extra": "mean: 156.2195811428556 msec\nrounds: 7"
          },
          {
            "name": "benchmarks/test_benchmark_qiskit.py::test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy",
            "value": 448.266339631135,
            "unit": "iter/sec",
            "range": "stddev: 0.00013318168260368493",
            "extra": "mean: 2.2308166185818683 msec\nrounds: 409"
          }
        ]
      }
    ]
  }
}