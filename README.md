# Non-linear Computational Mechanics of Structures

<!--
SPDX-FileCopyrightText: 2024 The Ikarus Developers mueller@ibb.uni-stuttgart.de
SPDX-License-Identifier: LGPL-3.0-or-later
-->

This repository aims to provide additional material for the course *Non-linear Computational Mechanics of Structures* offered by the *Institute for Structural Mechanics* of the University of Stuttgart.
Different problems to be solved during the exercise sessions reside in the `Exercise` folder.
Their corresponding solution is available in the `Solution` folder.

## Instructions for Use

To be updated !!!

### Troubleshooting

If Ikarus doesn't install or compile itself automatically, run:

```bash
pip install --pre pyikarus --verbose --upgrade --no-build-isolation
```

If Python isn't able to find Ikarus, make sure to be in the correct Python venv.
Run  `pip -V`. This should return something similar to

```bash
pip 23.3.1 from /dune/dune-common/build-cmake/dune-env/lib/python3.11/site-packages/pip (python 3.11)
```

If this is not the case, enable the venv via

```bash
source /dune/dune-common/build-cmake/dune-env/bin/activate
```
