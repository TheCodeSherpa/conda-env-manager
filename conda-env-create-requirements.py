import os
import subprocess

def get_conda_envs():
    cmd = "conda env list"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error is not None:
        print(f'Error occurred while getting conda environments: {error}')
        return []

    envs = output.decode('utf-8').split('\n')
    envs = [line.split()[0] for line in envs if line and not line.startswith('#') and line.split()[0] != 'base']
    print('Identified the following conda environments: ', ', '.join(envs))
    return envs

def get_env_packages(env):
    print(f'Getting packages for environment {env}...')
    cmd = f"conda list -n {env} --export"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error is not None:
        print(f'Error occurred while getting packages for environment {env}: {error}')
        return []

    packages = output.decode('utf-8').split('\n')
    packages = [line for line in packages if line and not line.startswith('#')]
    print(f'Found {len(packages)} packages in environment {env}')
    return packages

def write_to_file(env, packages):
    filename = f'{env}_requirements.txt'
    with open(filename, 'w') as f:
        for pkg in packages:
            f.write(pkg + '\n')
    print(f'Requirements for {env} written to {filename}')

def main():
    envs = get_conda_envs()
    for env in envs:
        packages = get_env_packages(env)
        write_to_file(env, packages)
    print('Task completed.')

if __name__ == '__main__':
    main()

