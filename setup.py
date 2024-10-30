from setuptools import setup
import sys
import os
import platform

def get_platform_binary_files():
    """Determine which binary files to include based on OS and CPU architecture."""
    os_name = sys.platform
    cpu_arch = platform.machine().lower()
    
    # Normalize architecture names
    arch_map = {
        'x86_64': 'amd64',
        'amd64': 'amd64',
        'arm64': 'arm64',
        'aarch64': 'arm64',
    }
    cpu_arch = arch_map.get(cpu_arch, cpu_arch)
    
    if os_name.startswith('darwin'):
        platform_name = 'mac'
    elif os_name.startswith('linux'):
        platform_name = 'linux'
    else:
        return []
    
    # Define binary files
    binaries = ['age', 'age-keygen']
    
    # Create list of source files and their destinations
    binary_files = []
    for binary in binaries:
        src = f'bin/{platform_name}-{cpu_arch}-{binary}'
        if os.path.exists(src):
            # Install to both flat and nested structure
            binary_files.extend([
                (f'bin/{platform_name}/{cpu_arch}', [src]),
                ('bin', [src])
            ])
    
    print(f"Including binaries for: {platform_name}/{cpu_arch}")
    return binary_files

setup(
    name="agecrypt",
    version="1.0.0",
    packages=["agecrypt"],
    package_data={
        "agecrypt": ["assets/*"],
    },
    data_files=get_platform_binary_files(),
    install_requires=[
        "flet>=0.21.0",
        "pexpect>=4.8.0"
    ],
    entry_points={
        "console_scripts": [
            "agecrypt=agecrypt.agecrypt:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A GUI for age encryption",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/agecrypt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
) 