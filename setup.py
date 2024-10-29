#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
     name='hmmstuff',
     zip_safe=False,
     include_package_data=True,

     version='0.0.1',

     author="Gabriele Orlando",

     author_email="gabriele.orlando@kuleuven.be",

     description="A tool to get structural information about light chain amyloids",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/grogdrinker/hmmstuff",
     
     #packages=['chaplin',"chaplin.src",'chaplin.marshalled','chaplin.marshalled.final_modelBert'],
     packages=['HMMSTUFF'],
     package_dir={'HMMSTUFF': 'HMMSTUFF/'},
     package_data={'HMMSTUFF': ['models/*','templates/*']},

     python_requires='<=3.9',

     install_requires=["pomegranate==0.14.0","numpy", "scikit-learn" ],

     classifiers=[

         "Programming Language :: Python :: 3",

         "Operating System :: OS Independent",

     ],

 )
