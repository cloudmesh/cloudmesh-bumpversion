"""
::

    Usage:
        bumpversion patch
        bumpversion minor
        bumpversion major
        bumpversion info
        bumpversion --set=VERSION

    Manages bumping the version for cloudmesh from the bumpversion.yaml file.

    Arguments:
        VERSION  the version number to set
        YAML  the yaml file name

    Options:
        --set=VERSION   the version number to set

    Description:

    this program modifies the following files.

    It reads the VERSION form the ./VERSION file
    the number is of the form MAYOR.MINOR.PATCH
    It increase the specified number
    It writes the number to the files
    ./VERSION
    ./src/cloudmesh/PACKAGE/__version__.py

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
    > - src/cloudmesh/bumpversion/__version__.py
    > - VERSION


"""
from bumpversion.bumpversion import BumpVersion
from pprint import pprint
from docopt import docopt

def banner(msg):
    print(70 * "=")
    print(msg)
    print(70 * "=")

def bumpversion(arguments):
   
    def update(component):

        bump_version = BumpVersion()
        bump_version.read_version_from_file(file_path="./VERSION")
        new_version = bump_version.incr(component)
        new_version = bump_version.version
        bump_version.change_files(str(bump_version))

    if arguments["patch"]:
        update("patch")

    elif arguments["minor"]:
        update("minor")

    elif arguments["major"]:
        update("major")

    elif arguments["info"]:
        version_file_path = "VERSION"  # Change this to the actual path of your VERSION file

        bump_version = BumpVersion()
        bump_version.read_version_from_file()
        bump_version.info()

    elif arguments["--set"]:

        bump_version = BumpVersion()
        bump_version.read_version_from_file(file_path="./VERSION")
        new_version = arguments["--set"]

        if bump_version.verify_version_format(new_version):

            bump_version.update_version(new_version)
            new_version = bump_version.version
            bump_version.change_files(str(bump_version))

        else:
            print("Invalid version format. Please provide a version in X.X.X format with integer components.")


    return ""

def main():
    arguments = docopt(__doc__)
    bumpversion(arguments)


if __name__ == '__main__':
    main()
