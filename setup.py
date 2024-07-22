from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='praktyki-techmo',
    version='0.9', #Version 1.0 is planned to be the one at the end of the practices
    packages=find_packages(),
    install_requires=required,
)
