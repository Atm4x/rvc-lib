from setuptools import setup, find_packages
import glob
import io

scripts_folder = glob.glob('rvc_lib/*.py')

# Read the requirements.txt file
with io.open('rvc_lib/requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='rvc',
    version='0.1',
    description='rvc package',
    author='RVC people',
    packages=find_packages(),
    install_requires=requirements,
    package_data={
        'rvc_lib.lib1.uvr5_pack.lib_v5.modelparams': ['*.json']
    },
    scripts=scripts_folder,
)
