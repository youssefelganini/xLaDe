# bin/

This directory contains the `xlade` CLI entrypoint script.

## `xlade`

```python
#!/usr/bin/env python3
from xlade.cli.main import main
if __name__ == "__main__":
    main()
```

---

## Why this exists

Before `pip install -e .` was set up, `./bin/xlade` was the only way
to run xLaDe. It remains useful for two reasons:

**Development without installing.** If you want to test changes without
running `pip install -e .` again, you can call `./bin/xlade` directly
from the repository root as long as the `xlade/` package directory is
on the Python path.

**Explicit path for scripts.** Any script or CI step that needs to call
xLaDe without assuming it is installed system-wide can use `./bin/xlade`
as a stable, predictable path.

---

## Normal usage

After `pip install -e .`, use `xlade` directly — not `./bin/xlade`.
Both call the same `xlade.cli.main:main` function. The pip-installed
command is the normal entry point.

---

## Do not delete this

Removing `bin/xlade` would break anyone following older documentation,
tutorials, or scripts that reference `./bin/xlade`. The file costs
nothing to keep. (actually it takes 1121 bytes of storage)