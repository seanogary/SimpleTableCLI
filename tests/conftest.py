# """Pytest configuration helpers.

# This file ensures the project root is on sys.path when pytest collects tests,
# so tests can import local packages (like `cli`) without requiring the user to
# set PYTHONPATH in their environment.
# """
# from __future__ import annotations

# import sys
# from pathlib import Path

# # Insert the project root (one level above the tests directory) at the front of
# # sys.path so `import cli` will resolve to the local package when running
# # pytest from the repository root.
# ROOT = Path(__file__).resolve().parents[1]
# sys.path.insert(0, str(ROOT))
