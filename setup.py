import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mapsmx",
    version="0.0.3",
    author="Federico Garza",
    author_email="fede.garza.ramirez@gmail.com",
    description="Create maps of México easily with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FedericoGarza/mapsmx",
    packages=setuptools.find_packages(),
    package_data={
        "mapsmx": ["geo/*.zip"]
    },
    include_package_data=True,
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
