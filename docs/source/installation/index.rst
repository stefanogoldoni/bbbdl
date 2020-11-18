Installation
============

Requirements
------------

You can install bbbdl on any computer which the following software already installed:

* `Python 3.8+ <https://www.python.org/>`_
* `ffmpeg <https://ffmpeg.org/download.html>`_


Installing bbbdl
----------------

bbbdl is distributed through `PyPI, the Python Package Index <https://pypi.org/project/bbbdl/>`_.


Using pipx
~~~~~~~~~~

The easiest way to install bbbdl, but requires `pipx <https://pipxproject.github.io/pipx/installation/>`_ to be
installed separately.

Run the following command in a terminal or command prompt:

.. code-block:: bash

   pipx install bbbdl

This will install bbbdl for the current user in an isolated environment so that the dependencies don't conflict with
other software already on your system.


Using pip and venv
~~~~~~~~~~~~~~~~~~

If pipx is not available, you can manually install bbbdl in a virtual environment (venv).

First, create a venv:

.. code-block:: bash

   python -m venv venv

Then, enter the venv:

.. code-block:: bash

   # Assuming you're using Linux
   source venv/bin/activate

While inside the venv, install bbbdl with pip:

.. code-block:: bash

   pip install bbbdl

Done! Remember that, if you install bbbdl using this method, you'll need to have entered the venv in that terminal
session to use bbbdl!


For development
~~~~~~~~~~~~~~~

If you want to contribute to bbbdl, you'll need to install it from source in editable mode.

This requires `Git <https://git-scm.com/>`_ and `Poetry <https://python-poetry.org/docs/#installation>`_, ensure to have
both of them installed.

First, fork the repository on GitHub:

.. image:: fork.png

Then, clone the forked repository on your computer and enter the created directory:

.. code-block:: bash

   git clone https://github.com/YOUR-USERNAME-HERE/bbbdl
   cd bbbdl

Finally, automatically create a venv and install all dependencies with Poetry:

.. code-block:: bash

   poetry install

This installs bbbdl in a Poetry venv, which you can access with:

.. code-block:: bash

   poetry shell
