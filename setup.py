# coding=utf-8
"""
Setup for scikit-surgerytrackedvideoultrasound
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgerytrackedvideoultrasound',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgerytracjedvideoultrasound is a Python package that contains helper functions to grab data from tracked ultrasound and tracked video cameras',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/NMontanaBrown/scikit-surgerytrackedvideoultrasound',
    author='Nina Montana-Brown',
    author_email='nina.brown.15@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
    ],

    entry_points={
        'console_scripts': [
            'sksurgerytrackedvidus=sksurgerytrackedvidus.__main__:main',
        ],
    },
)
