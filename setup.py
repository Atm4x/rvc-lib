from setuptools import setup, find_packages
import glob

scripts_folder = glob.glob('rvc_lib/*.py')

# Read the requirements.txt file
with open('rvc_lib/requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='rvc_lib',
    version='0.1',
    description='rvc package',
    author='RVC people',
    packages=find_packages(),
    install_requires=requirements,
    package_data={
        'lib.uvr5_pack.lib_v5.modelparams': ['*.json']
    },
    scripts=scripts_folder,
)
