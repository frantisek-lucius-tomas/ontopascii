from setuptools import setup, find_packages

setup(
    name="ontopascii",
    version="1.0.0",
    author="frantisek tomas",
    author_email="wfrantisektomas@gmail.com",
    url="https://github.com/frantisek-lucius-tomas/ontopascii",
    description="more information on the github page",
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
