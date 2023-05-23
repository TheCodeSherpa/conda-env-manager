# Conda Environment Manager

## Introduction

This repository contains a Python script for managing dependencies across different Conda environments. The script fetches a list of all Conda environments, retrieves the packages installed in each of these environments, and writes those packages to a text file. This could be particularly useful for replicating an environment on a different machine, or for managing dependencies across different Conda environments. 

## Getting Started

The script uses Python's built-in `os` and `subprocess` modules, so there are no additional dependencies to install. 

To run the script, simply clone this repository and execute the script as follows:

```
python conda_env_manager.py
```

The script will create a text file for each Conda environment, named `{env}_requirements.txt`, where `{env}` is the name of the Conda environment. Each file contains a list of packages installed in the corresponding environment, with each package on a new line.

## Functions

The script contains the following functions:

- `get_conda_envs()`: This function retrieves a list of all Conda environments on the machine.

- `get_env_packages(env)`: This function retrieves a list of all packages installed in a specified Conda environment.

- `write_to_file(env, packages)`: This function writes a list of packages to a text file, with each package on a new line.

- `main()`: This is the main function. It gets a list of all Conda environments, retrieves the packages installed in each environment, and writes those packages to a text file.

## About Me

Hi, I'm `TheCodeSherpa`. I'm a passionate programmer who loves to share knowledge and help others in their coding journey. I believe that coding should be fun and accessible to everyone. 

Please feel free to reach out to me if you have any questions, suggestions, or feedback!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.