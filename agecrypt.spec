import os
import platform
import sys
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Get platform-specific details
is_mac = sys.platform == 'darwin'
is_linux = sys.platform.startswith('linux')
cpu_arch = platform.machine().lower()

# Normalize architecture names
arch_map = {
    'x86_64': 'amd64',
    'amd64': 'amd64',
    'arm64': 'arm64',
    'aarch64': 'arm64',
}
cpu_arch = arch_map.get(cpu_arch, cpu_arch)

# Determine platform name
if is_mac:
    platform_name = 'mac'
elif is_linux:
    platform_name = 'linux'
else:
    raise Exception(f"Unsupported platform: {sys.platform}")

# Define paths
current_dir = os.path.dirname(os.path.abspath(SPEC))
bin_dir = os.path.join(current_dir, 'bin')

# Define binary files to include
binary_files = [
    (os.path.join(bin_dir, platform_name, cpu_arch, 'age'), f'bin/{platform_name}/{cpu_arch}'),
    (os.path.join(bin_dir, platform_name, cpu_arch, 'age-keygen'), f'bin/{platform_name}/{cpu_arch}'),
]

# Collect all data files
datas = collect_data_files('agecrypt') + binary_files

a = Analysis(
    ['agecrypt/__main__.py'],
    pathex=[],
    binaries=binary_files,
    datas=datas,
    hiddenimports=['flet.web'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='agecrypt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='agecrypt',
)

# macOS specific bundle
if is_mac:
    app = BUNDLE(
        coll,
        name='AgeCrypt.app',
        icon='agecrypt/assets/icon.icns',
        bundle_identifier='com.example.agecrypt',
        info_plist={
            'NSHighResolutionCapable': 'True',
            'LSApplicationCategoryType': 'public.app-category.utilities',
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleVersion': '1.0.0',
        },
    ) 