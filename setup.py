from setuptools import setup, find_packages

setup(
    name="ontopascii",
    version="0.0.1",
    author="frantisek tomas",
    author_email="wfrantisektomas@gmail.com",
    url="https://github.com/frantisek-lucius-tomas",
    description="ontopascii is a library for generating ascii art, it is very easy to use and you can do miracles with it.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PIL", "math"],
    entry_points={"console_scripts": ["ontopascii = ontopascii.ontopascii"]}

)
