from setuptools import setup
import sys
import os

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='metatabdecl',
    version='1.6',
    packages=['metatabdecl'],
    package_data={'metatabdecl': ['*.csv','*.json']},
    url='https://github.com/Metatab/metatab-declarations',
    license='BSD 2-Clause License',
    author='Eric Busboom',
    author_email='eric@busboom.org',
    description='Declaration files and specifications for the Metatab package',
    zip_safe=False
)
