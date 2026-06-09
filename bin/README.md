# bin/

This directory contains the `xlade` CLI entrypoint script.

## `xlade`

```python
#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xlade.cli.main import main

if __name__ == "__main__":
    main()
```

---

## Two Ways to Run xLaDe

**The manual way (no pip required):**

```bash
./bin/xlade
./bin/xlade --help
./bin/xlade run exp-002-kernel-boundary
```

Works from the repo root with just Python 3.11+ installed. No venv,
no pip, no installation step. This was the original way to run xLaDe
and remains fully supported.

**The installed way:**

```bash
pip install -e .
xlade
```

Installs xlade as a proper command. Useful when working across
multiple directories or integrating with other tools.

Both call the same `xlade.cli.main:main` function. Both are
supported. Neither is more correct than the other.

---

## Do not delete this

Removing `bin/xlade` would break anyone using the manual invocation
path. The file costs nothing to keep.