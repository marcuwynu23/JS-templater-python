import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jstemplater",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Mark Wayne B. Menorca",                     # Full name of the author
    description="Javascript Template Engine for web development",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["jstemplater"],             # Name of the python package
    package_dir={'':'jstemplater'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)