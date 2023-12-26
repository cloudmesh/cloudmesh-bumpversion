# The cloudmesh bumpversion command

[![GitHub Repo](https://img.shields.io/badge/github-repo-green.svg)](https://github.com/cloudmesh/cloudmesh-bumpversion)
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

## Manual Page

```

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

    > bumpversion patch
    >    increments the third number

    > bumpversion minor
    >    increments the second number

    > bumpversion mayor
    >    increments the first number

    > bumpversion info
    >    lists the numbers and identifies if one of them is wrong

    > bumpversion set --version=VERSION
    >   sets the version number to the spcified number

    > bumpversion --config=YAML --version=VERSION
    >   sets the versions in the files specifed in the yaml file

    > Example: bumpversion.yaml
    >
    > bumpversion:
    > - cloudmesh/bumpversion/__version__.py
    > - VERSION

```

## Manual Page

<!-- START-MANUAL -->
```
Command bar
===========

::

  Usage:
        bar --file=FILE
        bar list
        bar [--parameter=PARAMETER] [--experiment=EXPERIMENT] [COMMAND...]

  This command does some useful things.

  Arguments:
      FILE   a file name
      PARAMETER  a parameterized parameter of the form "a[0-3],a5"

  Options:
      -f      specify the file

  Description:

    > cms bar --parameter="a[1-2,5],a10"
    >    example on how to use Parameter.expand. See source code at
    >      https://github.com/cloudmesh/cloudmesh-bar/blob/main/cloudmesh/bar/command/bar.py
    >    prints the expanded parameter as a list
    >    ['a1', 'a2', 'a3', 'a4', 'a5', 'a10']

    > bar exp --experiment=a=b,c=d
    > example on how to use Parameter.arguments_to_dict. See source code at
    >      https://github.com/cloudmesh/cloudmesh-bar/blob/main/cloudmesh/bar/command/bar.py
    > prints the parameter as dict
    >   {'a': 'b', 'c': 'd'}

```
<!-- STOP-MANUAL -->