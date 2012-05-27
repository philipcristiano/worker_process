#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def run_setup():
    setup(
        name='workerprocess',
        version='0.1.1',
        description='A tool for creating external worker processes',
        keywords = '',
        url='https://github.com/philipcristiano/worker_process',
        author='Philip Cristiano',
        author_email='worker_process@philipcristiano.com',
        license='BSD',
        packages=['workerprocess'],
        install_requires=[''],
        test_suite='tests',
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Programming Language :: Python',
        ],
        entry_points="""
            [console_scripts]
        """


if __name__ == '__main__':
    run_setup()
