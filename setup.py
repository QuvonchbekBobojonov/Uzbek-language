from setuptools import setup, find_packages

setup(
    name="uzbek-language",
    version="0.1.0",
    description="This package was created to correct Uzbek spelling mistakes and translate from Latin to Cyrillic",
    author="Quvonchbek Bobojonov",
    author_email="moorfoinfo@gmail.com",
    url="https://github.com/QuvonchbekBobojonov/Uzbek-language",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
