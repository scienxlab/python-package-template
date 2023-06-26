# python-package-template

[![Tests](https://github.com/scienxlab/python-package-template/actions/workflows/build-test.yml/badge.svg)](https://github.com/scienxlab/python-package-template/actions/workflows/build-test.yml)
[![Docs](https://github.com/scienxlab/python-package-template/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/scienxlab/python-package-template/actions/workflows/publish-docs.yml)

**A prototype GitHub template for a basic Python package.**

This template repository implements a Python package, `mypackage` that contains a single module with a single function `myfunction`, accessible at the package level (i.e. you can do `mypackage.myfunction`, my assumption being that if you ever want submodules, you'll be able to implement it by that point in your Python journey).

It has most of the features you might want in a Python project:

- Some code that does something useful (not much, in this case!).
- A modern, PEP-517-style build process.
- A command-line interface.
- Tests, run automatically on GitHub Actions.
- Documentation, published to GitHub Pages.
- Publishing to PyPI ready to go.


## How to use this template

When you make a new repository in the GitHub interface, select `python-package-template` in the **Repository template** dropdown menu.

Then search and replace the placeholder names with your project's names. This will involve changing some file names and directory names. These are:

- `python-package-template` (ususally a GitHub repo has the same name as the package it contains, but not this one)
- `mypackage`
- `mycli`
- `myfunction`

You should alos change `LICENSE` if you want to use a different one, and the content of `AUTHORS.md`.


## Installing and building

To install the package, before or after changing its name, you can use `pip install .` or `pip install -e .` for an æeditableæ install (useful during development).

To build an `sdist` and `wheel` for `pip` to install (it can use either; wheels are the 'modern' way), you can do `python -m build`. 

Note: building the project makes a file called `src/mypackage/_version.py` which must not be checked into version control, hence it is included in `.gitignore`.


## Command line interface

As well as the Python package with its API, the package also implements a command line interface, or CLI, called `mycli` using Python's `script` entry point. So after installing with `pip`, there is a command-line tool you can invoke with `mycli --help`. The CLI is implemented with a popular tool called [`click`](https://click.palletsprojects.com/en/latest/).

You can also invoke the CLI by running the module with `python -m mypackage`, which relies on `__main__.py`. So many ways to run Python code!


## Tests

These are implemented using `pytest` for both the module and the CLI. The installation also includes `coverage` for checking test coverage (how much of your code is run under testing). The `pytest` options are in `pyproject.toml`. Run tests with:

    pytest

You can get an HTML report from Coverage with `coverage html`.


## Documentation

The docs are written in Markdown, with the top-level index written in RST. The documentation pages are built by [Sphinx](https://www.sphinx-doc.org/en/master/) with the following commands:

    cd docs
    make html

The []`myst-nb` plugin](https://myst-nb.readthedocs.io/en/latest/) for Sphinx should allow you to mix RST, Markdown, and Jupyter Notebooks in your documentation.

This package uses [the Furo theme](https://pradyunsg.me/furo/), but it's easy enough to change options like this in `docs/conf.py`.

The documentation builds as [a GitHub Action](https://github.com/scienxlab/python-package-template/blob/main/.github/workflows/publish-docs.yml) and [is deployed here](http://scienxlab.org/python-package-template/).


## Continuous integration

The package uses GitHub Actions for the automation of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration). There are 2 so-called workflows:

- `build_test.yml` &mdash; build and test the distribution using `pytest`.
- `publish-docs.yml` &mdash; build and publish the documentation to GitHub pages. Note that this requires you to anble GitHub package on your repo.


## Publishing to PyPI

At some point, you may want to publish your package to PyPI. There is a disabled GitHub action to help you do this, but you'll need to put some other things in place before you can use it:

- Create an account on PyPI, or get the credentials for an existing account.
- Create a project for the package.
- Create a token for publishing to the project.
- Install a repository secret on the GitHub project called `PYPI_API_TOKEN` with the value of the token.
- Install the `pypi-publish.yml` GitHub Action file (already in this repo) by removing `DISABLED` from the name.
- Create a 'release' with an appropriate [semantic version](https://semver.org/) tag in the GitHub interface. The GitHub Action should publish it to PyPI.
