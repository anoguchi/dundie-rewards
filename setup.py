import os
from setuptools import setup, find_packages


def read(*paths):
    """Read the contents of a text file safely.
    >>> read("DUNDIE-REWARDS", VERSION)
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    print("filepath: ", filepath)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file."""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dundier Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Alberto Noguchi",
    packages=find_packages(),
    entry_points={"console_scripts": ["dundie=dundie.__main__:main"]},
    install_requires=[read_requirements("requirements.txt")],
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    },
)
