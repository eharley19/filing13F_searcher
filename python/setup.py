"""This is the setup module."""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="edgar_filing_searcher",
    version="0.0.1",
    description="Web backend for filing website",
    url="https://github.com/eharley19/filing13F_searcher",
    packages=find_packages(),
    python_requires=">=3.6",
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    install_requires=INSTALL_REQUIRES
)
