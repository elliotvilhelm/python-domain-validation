import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whois_python",
    version="1.5.2",
    author="Elliot Pourmand",
    author_email="elliot@pourmand.com",
    description="whois client and parser focused on creation date",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/ElliotVilhelm/python-whois',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
