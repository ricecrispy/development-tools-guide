Running a python + poetry container from WSL using VSCode
=================================================

Purpose
--------

This project contains a sample python project, which is initiaited with `poetry`_, and the configurations needed to run and develope the project in a python container from WSL using VSCode.

The Dockerfile to start the container in VSCode is a slight modification of the starter python container provided by Microsoft. 
 

Pre-requisites
---------------

VSCode

WSL

Setting up
----------

1. ``git clone https://github.com/ricecrispy/development-tools-guide.git`` 

2. ``cd development-tools-guide/python-poetry-container``

3. ``code .``

4. Follow this `article`_ to install all the VSCode extensions needed

5. In VSCode, type ``control + shift + p``, then type ``Remote-Containers: Reopen in container``

6. Open a new integrated terminal and run the app with ``poetry run python print_greetings/print_greetings.py``

7. You can also run the tests with ``poetry run pytest``



.. _article: https://code.visualstudio.com/blogs/2020/07/01/containers-wsl
.. _poetry: https://python-poetry.org