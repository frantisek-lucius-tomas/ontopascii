from setuptools import setup, find_packages

setup(
    name="ontopascii",
    version="0.0.4",
    author="frantisek tomas",
    author_email="wfrantisektomas@gmail.com",
    url="https://github.com/frantisek-lucius-tomas/ontopascii",
    description="A library for generating ASCII art easily and effectively.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    license="MIT",
)
