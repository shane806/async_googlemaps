import setuptools
from setuptools import setup
requirements = ["requests", "aiohttp"]

with open("README.md") as f:
    readme = f.read()

setup(
    name="async_googlemaps",
    version="0.0.10",
    description="Asynchronous Python client library for Google Maps Platform",
    long_description=readme,
    long_description_content_type="text/markdown",
    scripts=[],
    url="https://github.com/shane806/async_googlemaps",
    packages=['async_googlemaps'],
    license="Apache 2.0",
    platforms="Posix; MacOS X; Windows",
    setup_requires=requirements,
    install_requires=requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet",
    ],
    python_requires='>=3.5'
)
