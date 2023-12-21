# The cloudmesh bumpversion command

![GitHub Repo](https://img.shields.io/badge/github-repo-green.svg)](https://github.com/cloudmesh/cloudmesh-bumpversion)
[![image](https://img.shields.io/pypi/pyversions/cloudmesh-bumpversion.svg)](https://pypi.org/project/cloudmesh-bumpversion)
[![image](https://img.shields.io/pypi/v/cloudmesh-bumpversion.svg)](https://pypi.org/project/cloudmesh-bumpversion/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![General badge](https://img.shields.io/badge/Status-Production-<COLOR>.svg)](https://shields.io/)
[![GitHub issues](https://img.shields.io/github/issues/cloudmesh/cloudmesh-bumpversion.svg)](https://github.com/cloudmesh/cloudmesh-bumpversion/issues)
[![Contributors](https://img.shields.io/github/contributors/cloudmesh/cloudmesh-bumpversion.svg)](https://github.com/cloudmesh/cloudmesh-bumpversion/graphs/contributors)
[![General badge](https://img.shields.io/badge/Other-repos-<COLOR>.svg)](https://github.com/cloudmesh/cloudmesh)


[![Linux](https://img.shields.io/badge/OS-Linux-orange.svg)](https://www.linux.org/)
[![macOS](https://img.shields.io/badge/OS-macOS-lightgrey.svg)](https://www.apple.com/macos)
[![Windows](https://img.shields.io/badge/OS-Windows-blue.svg)](https://www.microsoft.com/windows)

see cloudmesh.cmd5

* https://github.com/cloudmesh/cloudmesh.cmd5


::

  Usage:
        bumpversion patch
        bumpversion minor
        bumpversion major
        bumpversion info
        bumpversion set --version=VERSION
        bumpversion --config=YAML --version=VERSION


  Manages bumping the version for cloudmesh

  Arguments:
      VERSION  the version number to set
      YAML  the yaml file name

  Options:
      --version=VERSION   the version number to set
      --config=YAML   the YAML FILE

  Description:

    this program modifies the following files.

    It reads the VERSION form the ./VERSION file
    the number is of the form MAYOR.MINOR.PATCH
    It increase the specified number
    It writes the number to the files
    ./VERSION
    ./cloudmesh/cloudmesh-PACKAGE/__version__.py

    > cms bumpversion patch
    >    increments the third number

    > cms bumpversion minor
    >    increments the second number

    > cms bumpversion mayor
    >    increments the first number

    > cms bumpversion info
    >    lists the numbers and identifies if one of them is wrong

    > cms bumpversion set --version=VERSION
    >   sets the version number to the spcified number

    > cms bumpversion --config=YAML --version=VERSION
    >   sets the versions in the files specifed in the yaml file

    > Example: bumpversion.yaml
    >
    > bumpversion:
    > - cloudmesh/bumpversion/__version__.py
    > - VERSION



# Timer: 0.0031s Load: 0.2415s help bumpversion
