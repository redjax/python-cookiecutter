# Python Cookiecutter

A cookiecutter template for a [`pdm`](https://pdm-project.org)-managed Python project.

## Description

Initialize a Python project. Sets up:

- Project structure (uses a `src/` directory layout)
- `pyproject.toml` file
  - [`ruff`](https://astral.sh/ruff) rules
  - [`pytest`](https://docs.pytest.org/en/latest/) configuration
- Dev dependencies
  - `ruff`
  - [`nox`](nox.thea.codes/en/stable)
  - [`pytest-xdist`](https://pytest-xdist.readthedocs.io/en/latest/)
  - [`uv`](https://github.com/astral-sh/uv)
  - [black](https://black.readthedocs.io/en/stable/index.html)
- Custom `.gitignore`; builds on the default `pdm` `.gitignore`
- Demo `pytest` tests
  - Import the templated module's [`__test_demo.demo_test_print()`](./{{%20cookiecutter.project_name%20}}/src/{{%20cookiecutter.project_src%20}}/__test_demo.py) function
  - Runs multiple `xfail` tests
  - Prints the OS
- Custom [`noxfile.py`](./{{%20cookiecutter.project_name%20}}/noxfile.py)
  - Sessions for linting (with `ruff` and `black`), exporting `requirements.txt` file(s), and running `pytest` tests with `pytest-xdist`

## Usage

- Using the `gh:<username>/<repo>` syntax:

```shell
cookiecutter gh:redjax/python-cookiecutter
```

- Using the full URL to a cookiecutter

```shell
cookiecutter https://github.com/redjax/python-cookiecutter.git [-c/--checkout <branch>] [-o/--output-dir] /path/to/cloned/cookiecutter
```
