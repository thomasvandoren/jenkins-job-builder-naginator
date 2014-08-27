Naginator Plugin module for jenkins-job-builder
===============================================

Python module that extends `jenkins-job-builder
<http://ci.openstack.org/jenkins-job-builder/>`_ to support new publisher,
``naginator``.

.. raw:: html

    <a href="https://travis-ci.org/thomasvandoren/jenkins-job-builder-naginator" target="_blank"><img src="https://travis-ci.org/thomasvandoren/jenkins-job-builder-naginator.svg"></a>

Naginator Publisher
-------------------

.. automodule:: naginator_publisher
    :members:

Installation
------------

.. code-block:: bash

    pip install jenkins-job-builder-naginator

Development
-----------

To work on this project, install the dependencies, install the develop branch,
make change, and run tests with tox:

.. code-block:: bash

    pip install -r requirements.txt -r test-requirements.txt
    python setup.py develop
    # ... make changes ...
    tox

.. note:: It is best to use a virtualenv for developing this package.
