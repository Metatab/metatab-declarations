from setuptools import setup

setup(
    name='metatab.declarations',
    version='0.2',
    package_dir={ 'metatab.declarations': 'declarations'},
    packages=['metatab.declarations'],
    package_data={'metatab.declarations': ['*.csv','*.json']},
    url='',
    license='',
    author='Eric Busboom',
    author_email='eric@busboom.org',
    description=''
)
