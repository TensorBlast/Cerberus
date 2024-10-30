from setuptools import setup

setup(
    name="agecrypt",
    version="1.0.0",
    packages=["agecrypt"],
    install_requires=[
        "flet>=0.21.0",
        "pexpect>=4.8.0"
    ],
    entry_points={
        "console_scripts": [
            "agecrypt=agecrypt.agecrypt:main",
        ],
    },
    author="Ankit Pasi",
    author_email="ankitpasi1@gmail.com",
    description="A GUI for age encryption",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TensorBlast/agecrypt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 