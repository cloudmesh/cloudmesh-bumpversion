import re
import yaml
import toml


class BumpVersion:
    """
    BumpVersion Class

    This class provides functionality for bumping version numbers in files, updating package information,
    and managing version-related tasks.

    Methods:
        - __init__(file_path="./VERSION"): Initialize the BumpVersion class.
        - info(): Display information about the BumpVersion instance.
        - read_version_from_file(file_path="./VERSION"): Read and parse the version from a file.
        - verify_version_format(version): Verify the format of the provided version.
        - update_version(new_version): Update the version in the file with the provided version.
        - update_version_in_file(file_path, new_version, version_variable="__version__"): Update version in a specific file.
        - read_package_name_from_toml(filename="pyproject.toml"): Read package name from a TOML file.
        - read_package_name_from_setup(): Read package name from setup.py.
        - _read_files_to_change(yaml_file="bumpversion.yaml"): Read files to change from a YAML configuration file.
        - change_files(new_version): Change version in multiple files specified in a YAML configuration file.
        - incr(component, file_path="./VERSION"): Increment a specified version component.

    Usage:
        bump_version_instance = BumpVersion()
        bump_version_instance.info()

        new_version = bump_version_instance.incr("patch")
        bump_version_instance.update_version(new_version)
    """

    def __init__(self, file_path="./VERSION"):
        """
        Initialize the BumpVersion class.

        Args:
            file_path (str): Path to the file containing the version information. Default is "./VERSION".

        Returns:
            None
        """
        self.package_name = None
        self.file_path = file_path
        self.version = None  # Initialize version to None

    def __str__(self):
        if type(self.version) == dict:
            return f"{self.version['major']}.{self.version['minor']}.{self.version['patch']}"
        else:
            return self.version
        
    def info(self):
        """
        Display information about the BumpVersion instance.

        Args:
            None

        Returns:
            None
        """
        print(f"File Path: {self.file_path}")
        if self.version:
            print(f"Current Version: {self.version['major']}.{self.version['minor']}.{self.version['patch']}")
        else:
            print("Version information not available. Use read_version_from_file method to read the version.")

    def read_version_from_file(self, file_path="./VERSION"):
        """
         Read and parse the version from a file.

         Args:
             file_path (str): Path to the file containing the version information. Default is "./VERSION".

         Returns:
             None
         """
        try:
            # Use the provided file_path or the default one
            file_path = file_path or self.file_path

            # Read the content of the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Use regular expression to extract the version number
            version_match = re.search(r'(\d+)\.(\d+)\.(\d+)', content)

            if version_match:
                # Populate the version dictionary
                self.version = {
                    'major': int(version_match.group(1)),
                    'minor': int(version_match.group(2)),
                    'patch': int(version_match.group(3))
                }
            else:
                print("Error: Unable to extract version from file.")

        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def verify_version_format(version):
        """
        Verify the format of the provided version.

        Args:
            version (str): The version string to be verified.

        Returns:
            bool: True if the version has the correct format, False otherwise.
        """
        try:
            # Split version into major, minor, and patch components
            # noinspection PyUnusedLocal
            major, minor, patch = map(int, version.split('.'))
            return True
        except ValueError:
            return False

    def update_version(self, new_version, debug=False):
        """
        Update the version in the file with the provided version.

        Args:
            new_version (str): The new version string.

        Returns:
            None
        """

        try:
            # Verify the format of the new version
            if not self.verify_version_format(new_version):
                print("Error: Invalid version format. Please provide a version in X.X.X format.")
                return

            # Read the content of the file if version is not populated
            if self.version is None:
                self.read_version_from_file()

            # Update the version dictionary with the new version
            self.version['major'], self.version['minor'], self.version['patch'] = map(int, new_version.split('.'))

            # Format the new version string
            new_version_str = f"{self.version['major']}.{self.version['minor']}.{self.version['patch']}"

            # Read the content of the file
            with open(self.file_path, 'r') as file:
                content = file.read()

            # Use regular expression to find and replace the version number
            updated_content = re.sub(r'\d+\.\d+\.\d+', new_version_str, content)

            # Write the updated content back to the file
            with open(self.file_path, 'w') as file:
                file.write(updated_content)

            if debug:
                print(f"Version updated to {new_version_str} successfully.")

        except Exception as e:
            print(f"Error: {e}")

    def update_version_in_file(self, file_path, new_version, version_variable="__version__", debug=False):
        """
        Update version in a specific file.

        Args:
            file_path (str): Path to the file.
            new_version (str): The new version string.
            version_variable (str): The variable name containing the version. Default is "__version__".

        Returns:
            None
        """

        try:
            # Read the content of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Find the line containing the specified version variable
            for i, line in enumerate(lines):
                if version_variable == "version:":
                    if re.search(fr'{version_variable}\s*:\s*"\d+\.\d+\.\d+"', line):
                        print("LLLL", line)
                        # replace the version number after the : with the new version
                        parts = line.split(':', 1) 
                        lines[i] = parts[0] + ': "' + new_version + '"\n'  
                elif re.search(fr'{version_variable}\s*=\s*"\d+\.\d+\.\d+"', line):
                    lines[i] = f'{version_variable} = "{new_version}"\n'
                    break

            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)

            if debug:
                print(f"Version in {file_path} updated to {new_version} successfully.")

        except Exception as e:
            print(f"Error: {e}")
        if debug:
            print("Current version:", str(self))

        if self.verify_version_format(new_version):
            self.update_version(new_version)
            self.read_version_from_file()
            if debug:
               print("Updated version:", str(self))
        else:
            print("Invalid version format. Please provide a version in X.X.X format.")

    def read_package_name_from_toml(self, filename="pyproject.toml"):
        """
        Reads the 'name' value from the '[project]' section in a TOML file.

        Parameters:
        - toml_file_path (str): Path to the TOML file.

        Returns:
        - str: The value of 'name' if found, otherwise None.
        """

        try:
            data = toml.load(filename)
            project_name = data.get('project', {}).get('name')

            return project_name

        except FileNotFoundError:
            print(f"File not found: {filename}")
            return None
        except toml.TomlDecodeError as e:
            print(f"Error decoding TOML: {e}")
            return None

    def _read_files_to_change(self, yaml_file="bumpversion.yaml"):
        """
        Read files to change from a YAML configuration file.

        Args:
            yaml_file (str): Path to the YAML file.

        Returns:
            list or None: List of files to change or None if there is an error.

        Example:
            The bumpversion yaml file looks like

            bumpversion:
            - src/bumpversion/__init__.py
            - VERSION

        """
        try:
            with open(yaml_file, 'r') as file:
                yaml_data = yaml.safe_load(file)

            if 'bumpversion' in yaml_data and isinstance(yaml_data['bumpversion'], list):
                self.files_to_change = yaml_data['bumpversion']
                return self.files_to_change
            else:
                print(f"Error: Invalid or missing 'bumpversion' in {yaml_file}.")
                return None

        except Exception as e:
            print(f"Error: {e}")
            return None

    def change_files(self, new_version):
        """
        Change version in multiple files specified in a YAML configuration file.

        Args:
            new_version (str): The new version string.

        Returns:
            None
        """
        files = self._read_files_to_change(yaml_file="bumpversion.yaml")

        for file_path in files:
            print(new_version, "->", file_path)
            self.update_version_in_file(file_path, new_version, version_variable="__version__")
            self.update_version_in_file(file_path, new_version, version_variable="version")
            # self.update_version_in_file(file_path, new_version, version_variable="version:")
            
    def incr(self, component, file_path="./VERSION"):
        """
        Increment a specified version component.

        Args:
            component (str): The version component to increment (major, minor, or patch).
            file_path (str): Path to the file containing the version information. If None, the default file_path is used.

        Returns:
            str or None: The new version string or None if there is an error.
        """

        try:
            # Use the provided file_path or the default one
            self.read_version_from_file(file_path=file_path)

            # Increment the specified version component
            if component == "major":
                self.version['major'] += 1
            elif component == "minor":
                self.version['minor'] += 1
            elif component == "patch":
                self.version['patch'] += 1
            else:
                print("Error: Invalid component. Use 'major', 'minor', or 'patch'.")
                return

            # Format the new version string
            new_version_str = f"{self.version['major']}.{self.version['minor']}.{self.version['patch']}"
            return new_version_str

        except Exception as e:
            print(f"Error: {e}")
