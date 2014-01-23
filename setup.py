from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "GoogleTODO",
    version = "0.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    entry_points = {
        'console_scripts': [
            'google_todo = main.google_todo:main',
        ],
    },
)