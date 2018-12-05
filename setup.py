from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='TagCounter',
    version='1.0.0',
    author='Andrey Zakharov',
    packages=['tagcounter'],
    description='Count tags in html page',
    entry_points={'console_scripts': ['tagcounter = tagcounter:main']},
    install_requires=['optparse', "tkinter"],
)