Naginator Plugin module for jenkins-job-builder
===============================================

Python module that extends `jenkins-job-builder
<http://ci.openstack.org/jenkins-job-builder/>`_ to support new publisher,
``naginator``.

Documentation
-------------

Please see http://jenkins-job-builder-naginator.readthedocs.org/

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
