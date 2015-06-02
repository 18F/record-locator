from distutils.core import setup

readme = open('README.md').read()

setup(
    name="RecordLocator",
    version="0.1",
    packages=['recordlocator'],
    description="Generate airline style record locators",
    license="Public Domain",
    long_description=readme,
)
