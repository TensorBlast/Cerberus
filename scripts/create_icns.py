from PIL import Image
import os

def create_icns(png_path, icns_path):
    # Open the PNG image
    img = Image.open(png_path)
    
    # Create temporary iconset directory
    iconset_path = 'icon.iconset'
    os.makedirs(iconset_path, exist_ok=True)
    
    # Create icons of different sizes
    sizes = [16, 32, 64, 128, 256, 512]
    for size in sizes:
        # Normal resolution
        icon = img.resize((size, size), Image.Resampling.LANCZOS)
        icon.save(f'{iconset_path}/icon_{size}x{size}.png')
        # High resolution (2x)
        if size * 2 <= 512:  # Don't exceed 512
            icon = img.resize((size * 2, size * 2), Image.Resampling.LANCZOS)
            icon.save(f'{iconset_path}/icon_{size}x{size}@2x.png')
    
    # Use iconutil to create icns (macOS command)
    os.system(f'iconutil -c icns {iconset_path} -o {icns_path}')
    
    # Clean up
    for file in os.listdir(iconset_path):
        os.remove(os.path.join(iconset_path, file))
    os.rmdir(iconset_path)

# Create the ICNS file
create_icns('agecrypt/assets/icon.png', 'agecrypt/assets/icon.icns') 