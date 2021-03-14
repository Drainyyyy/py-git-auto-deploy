#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Covered by The MIT License (MIT)
#
#  Copyright 2021 Drainyyy
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
#  CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import sys
from pathlib import Path

from setuptools import setup, find_packages

ROOT = Path(__file__).parent

if sys.version_info < (3, 7):
    raise SystemExit("py-git-auto-deploy requires Python version 3.7+.")

with open("README.md", "r") as f:
    long_description = f.read()

with open(str(ROOT / 'requirements.txt'), encoding='utf-8') as f:
    REQUIREMENTS = f.read().splitlines()


setup(
    name='py-git-auto-deploy',
    author="Drainyyy",
    author_email="contact@drainyyy.xyz",
    version='0.0.1a',
    url="https://github.com/drainyyyy/py-git-auto-deploy",
    license="MIT",
    keywords=["py-git-auto-deploy", "python", "git", "deployment", "automatic deployment", "auto deploy"],
    description="A flask web server, which checks for git pushes to a repository and automatically deploys the new code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requirements=REQUIREMENTS,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Version Control"
    ],
 )
