from setuptools import setup, find_packages

setup(
    name="mem0-modified",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        # add other requirements here
    ],
)
