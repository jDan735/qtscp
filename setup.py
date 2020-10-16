from setuptools import setup
from qtscp import __version__

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="qtscp",
    version=__version__,
    author="Daniel Zakharov",
    author_email="daniel734@bk.ru",
    description="Unoffical Qt client of SCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="kanobu qt game",
    url="https://github.com/jDan735/qtscp",
    license="MIT",
    include_package_data=True,
    packages=["qtscp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3",
    install_requires=[
        "pyscp",
    ],
    entry_points={
        "console_scripts": [
            "qtscp=qtscp.app:main",
        ]
    }
)
