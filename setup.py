from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='praktyki-techmo',
    version='0.9', #version 1.0 will be the one at the end of the internship
    packages=find_packages(),
    install_requires=required,
)
