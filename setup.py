from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='praktyki-techmo',
    version='1.0', #Wersja 1.0 planowana na koniec prakttyk
    packages=find_packages(),
    install_requires=required,
)
