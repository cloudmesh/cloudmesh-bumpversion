from cloudmesh.bumpversion.bumpversion import BumpVersion
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import banner
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.shell.command import map_parameters


class BumpversionCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_bumpversion(self, args, arguments):
        """
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


        """

        # arguments.FILE = arguments['--file'] or None

        # switch debug on

        def update(component):

            bump_version = BumpVersion()

            bump_version.info()

            new_version = bump_version.incr(component)

            banner(new_version)

            if bump_version.verify_version_format(new_version):
                bump_version.update_version(new_version)
                bump_version.read_version_from_file()
                bump_version.info()

                package = bump_version.read_package_name_from_toml("pyproject.toml")
                if package is None:
                    package = bump_version.read_package_name_from_setup().replace("-", "/")

                version_file_path = f"{package}/__version__.py"  # Change this to the actual path of your version.py file
                bump_version.update_version_in_file(version_file_path, new_version, version_variable="version")
                print()

                toml_file_path = f"pyproject.toml"  # Change this to the actual path of your version.py file
                bump_version.update_version_in_file(toml_file_path, new_version, version_variable="version")
                print()

                bump_version.read_version_from_file()
                print()

                bump_version.info()
            else:
                print("Invalid version format. Please provide a version in X.X.X format with integer components.")

        map_parameters(arguments, "version", "config")

        VERBOSE(arguments)

        if arguments.patch:
            update("patch")

        elif arguments.minor:
            update("minor")

        elif arguments.major:
            update("major")

        elif arguments.info:
            version_file_path = "VERSION"  # Change this to the actual path of your VERSION file

            bump_version = BumpVersion()
            bump_version.read_version_from_file()
            bump_version.info()

        elif arguments.set:

            bump_version = BumpVersion()
            bump_version.read_version_from_file()
            bump_version.info()
            new_version = arguments.version

            if bump_version.verify_version_format(new_version):
                bump_version.update_version(new_version)
                bump_version.read_version_from_file()
                bump_version.info()

                package = bump_version.read_package_name_from_setup().replace("-", "/")

                for version_file_path in  [f"{package}/__version__.py", f"{package}/__init__.py", f".bumpversion.cfg"]:
                    try:
                        bump_version.update_version_in_file(version_file_path, new_version, version_variable="version")
                    except:
                        pass
                    try:
                        bump_version.update_version_in_file(version_file_path, new_version, version_variable="__version__")
                    except:
                        pass
                bump_version.read_version_from_file()
                bump_version.info()
            else:
                print("Invalid version format. Please provide a version in X.X.X format with integer components.")

        elif arguments.config:

            bump_version = BumpVersion()
            bump_version.info()
            new_version = arguments.version

            bump_version.change_files(new_version)

            print("AAA")

        return ""
