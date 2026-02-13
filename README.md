# SimpleCSVCLI

SimpleTableCLI is a lightweight command-line tool for exploring and manipulating CSV files. It provides focused utilities for loading, inspecting, selecting, filtering, and formatting CSV data from the terminal. This repository contains a minimal, working implementation designed to be extended.

## Table of contents

- [Project overview](#project-overview)
- [Screen recordings](#screen-recordings)
- [Features](#features)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Tests](#tests)
- [Project layout](#project-layout)
- [Notes and Takeaways](#notes-and-Takeaways)
- [License](#license)

## Project overview

I built this project to learn the skill of building simple CLI tools according to a clearly scoped specification. And, for that matter, the general skill of completing a project with a clear finishing condition. I also used it as an opportunity to strengthen my ability to think through writing good tests and, critically, writing testable modules. 

## Screen recordings

Screen recordings of use will go here.

## Features

- Load local CSV files
- Inspect columns
- Select columns and project subsets of data
- Filter rows
- Basic regex search utilities across fields
- Unit tests covering core functionality
- Pipe-friendly output (raw CSV when piped, formatted tables in terminal)


## Installation

This project targets modern Python (3.11+). Use a virtual environment for development.

```bash
# macOS / zsh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For development installation:

```bash
pip install -e .
```

## Quick start

Display CLI help and available subcommands:

```bash
python main.py --help
```

## Tests

Run the test suite with pytest:

```bash
pytest -q
```

## Project layout

- `main.py` — CLI entrypoint
- `cli/` — core modules implementing parsing, loading, filtering, and formatting
  - `parser.py`
  - `data_loader.py`
  - `columns.py`
  - `filter.py`
  - `select.py`
  - `formatter.py`
  - `search_utils.py`
- `tests/` — unit tests and testdata
- `requirements.txt`, `pyproject.toml` — dependency and packaging metadata

## Notes and Takeaways

TO-DO

## License

TO-DO

---