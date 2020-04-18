import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mapsmx",
    version="0.0.2",
    author="Federico Garza",
    author_email="fede.garza.ramirez@gmail.com",
    description="Create maps of México easily with python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FedericoGarza/mapsmx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires = [
        "geopandas>=0.7.0"
    ]
)
