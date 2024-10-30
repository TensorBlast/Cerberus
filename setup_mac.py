from setuptools import setup
import os
import subprocess
import shutil

def find_lib_path(lib_name):
    # Check common locations
    possible_paths = [
        f"/usr/local/opt/libffi/lib/{lib_name}",
        f"/opt/homebrew/opt/libffi/lib/{lib_name}",
        f"/usr/local/lib/{lib_name}",
        f"/usr/lib/{lib_name}",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
            
    # Try using brew to find it
    try:
        result = subprocess.run(['brew', '--prefix', 'libffi'], 
                              capture_output=True, text=True)
        brew_path = os.path.join(result.stdout.strip(), 'lib', lib_name)
        if os.path.exists(brew_path):
            return brew_path
    except:
        pass
    
    return None

# Find libffi
libffi_path = find_lib_path('libffi.8.dylib')
if not libffi_path:
    raise ValueError("Could not find libffi.8.dylib. Please install it with 'brew install libffi'")

print(f"Found libffi at: {libffi_path}")

APP = ['agecrypt/agecrypt.py']
DATA_FILES = [
    ('assets', ['agecrypt/assets/icon.png']),
    ('Frameworks', [libffi_path])  # Include libffi in the bundle
]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'agecrypt/assets/icon.icns',
    'packages': ['flet', 'pexpect'],
    'includes': ['ctypes'],
    'frameworks': [libffi_path],
    'plist': {
        'CFBundleName': "Age Encryption",
        'CFBundleDisplayName': "Age Encryption",
        'CFBundleGetInfoString': "GUI for age encryption",
        'CFBundleIdentifier': "com.yourdomain.agecrypt",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHumanReadableCopyright': "Copyright © 2024, Your Name, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 