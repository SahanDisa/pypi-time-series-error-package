import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="Time Series Error - Python",
    version="0.0.1",
    author="Sahan Dissanayaka - COTS",
    author_email="tsahandisaai@gmail.com",
    description="Robust python package to evaluate time series errors and validate the accuracy",
    long_description="This package consist of the novel state-of-the-art time series error evaluation metrics in order to measure and evaluate time series",
    long_description_content_type="text/markdown",
    url="https://github.com/SahanDisa/pypi-time-series-error-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)