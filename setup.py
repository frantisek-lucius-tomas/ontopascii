from setuptools import setup, find_packages

setup(
    name="asciiart",
    version="0.1.0",
    description="A Python library to convert images and GIFs into ASCII art.",
    author="frantisek tomas",
    author_email="wfrantisektomas@gmail.com",
    url="https://github.com/yourusername/asciiart",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0",  # Pillow is used for image processing
        # Add any other dependencies your project might have
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
