import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="poms",
    version="0.0.18",
    author="Lauro Cesar",
    author_email="lauro@dlceducationalgames.com",
    description="Python3 Omnidirectional microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lauro-cesar/poms",
    project_urls={
    "Documentation":"https://github.com/lauro-cesar/poms/wiki",
    "GitHub Sources": "https://github.com/lauro-cesar/poms",
    "Tracker": "https://github.com/lauro-cesar/poms/projects/",
    "Developer Story":"https://stackoverflow.com/story/lauro-cesar",
    },    
    install_requires=['websockets'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    test_loader='unittest:TestLoader',
)