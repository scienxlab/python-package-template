# Installation

At the command line:

    pip install mypackage

Or, if you use Conda environments:

    conda create -n mypackage python=3.9
    conda activate mypackage
    pip install mypackage

For developers, there are also options for installing `tests`, `docs` and `dev` dependencies, e.g. `pip install mypackage[dev]` to install all testing and documentation packages.

For development, you can also clone the repository, then change to its directory, then do the following for an "editable" install that changes while you develop:

    pip install -e .

If you want to help develop `mypackage`, please read [Development](development.md).
