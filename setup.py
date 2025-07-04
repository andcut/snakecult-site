#!/usr/bin/env python3

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() if (this_directory / "README.md").exists() else ""

setup(
    name="snakecult-translate",
    version="0.1.0",
    author="Andrew Cutler",
    author_email="andrew@vectorsofmind.com",
    description="A modular translation system for Hugo multilingual sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snakecult/snakecult-site",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "python-frontmatter>=1.0.0",
        "python-dotenv>=1.0.0",
        "tiktoken>=0.5.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "snakecult-translate-one=snakecult_translate.cli_one:main",
            "snakecult-translate-parallel=snakecult_translate.cli_parallel:main", 
            "snakecult-translate-batch=snakecult_translate.cli_batch_async:main",
        ],
    },
) 