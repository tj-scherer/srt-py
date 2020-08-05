import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="srt-py",
    version="0.0.0",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.mit.edu/SmallRadioTelescope/srt-py",
    packages=setuptools.find_packages(),
    scripts=[str(path) for path in Path("./bin/").glob("**/*.py")],
    package_data={"": ["*.js", "*.css", "*.ico", "*.png"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
