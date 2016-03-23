from distutils.core import setup
from setuptools import setup

setup(
    name='Orctrix',
    version='0.0.1',
    author='Raniere Silva',
    author_email='raniere.silva@manchester.ac.uk',
    packages=['Orctrix'],
    url='https://github.com/njall/Orctrix',
    license='LICENSE',
    description='Hackday project for CW16',
    long_description='Hackday project for CW16',
    entry_points={
        'console_scripts':['Orctrix = Orctrix.main:main']},
)
