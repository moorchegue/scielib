################
ScieCoin Library
################


Installation
============

Install the app and migrate::

    pip install -e '.[dev,testing]'
    manage migrate

Create a super user (optional)::

    manage createsuperuser

Load sample data, i.e. fixtures (optional, requires at least one user)::

    manage loaddata sample_data

To run the dev server do::

    manage runserver


Versioning
==========

Use `Zest.releaser <https://zestreleaser.readthedocs.io/en/latest/>`__.


Tests
=====

Run all tests with `py.test`::

    py.test -v
