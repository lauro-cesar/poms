import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="poms",
    version="0.0.3",
    author="Lauro Cesar",
    author_email="lauro@dlceducationalgames.com",
    description="Python Async IO microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lauro-cesar/poms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)