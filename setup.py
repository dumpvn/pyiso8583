import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iso8583-pkg-phucnguyenv",
    version="0.0.1",
    author="Phuc Nguyen",
    author_email="phuc.vinh@outlook.com",
    description="A small iso8583 package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dumpvn/pyiso8583",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
