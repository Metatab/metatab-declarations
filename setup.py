from setuptools import setup
import sys
import os

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='metatab_declarations',
    version='0.2',
    packages=['metatab_declarations'],
    package_data={'metatab_declarations': ['*.csv','*.json']},
    url='https://github.com/CivicKnowledge/metatab-declarations',
    license='BSD 2-Clause License',
    author='Eric Busboom',
    author_email='eric@busboom.org',
    description='',
    zip_safe=False
)
