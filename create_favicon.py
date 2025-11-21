"""
Script to create a grayscale favicon from gen-h-13.jpg
Zooms 200% and converts to black & white
"""
from PIL import Image, ImageEnhance
import os

def create_favicon():
    # Input and output paths
    input_path = 'portfolio/static/portfolio/images/gen-h-13.jpg'
    output_path = 'portfolio/static/portfolio/images/favicon.png'
    
    try:
        # Open the image
        img = Image.open(input_path)
        print(f"✓ Loaded image: {img.size}")
        
        # Get center coordinates
        width, height = img.size
        center_x, center_y = width // 2, height // 2
        
        # Calculate crop box for 150% zoom (crop to 66.67% of original size from center)
        # 150% zoom = 1/1.5 = 0.6667 of original size
        crop_size = int(min(width, height) * 0.6667)
        left = center_x - crop_size // 2
        top = center_y - crop_size // 2
        right = center_x + crop_size // 2
        bottom = center_y + crop_size // 2
        
        # Crop to center (this creates 150% zoom effect)
        img_cropped = img.crop((left, top, right, bottom))
        print(f"✓ Cropped to center: {img_cropped.size}")
        
        # Convert to grayscale (black & white)
        img_bw = img_cropped.convert('L')
        print("✓ Converted to grayscale")
        
        # Enhance contrast for better B&W effect
        enhancer = ImageEnhance.Contrast(img_bw)
        img_bw = enhancer.enhance(1.3)
        print("✓ Enhanced contrast")
        
        # Resize to standard favicon sizes
        # Create multiple sizes
        sizes = [16, 32, 48, 64, 128, 256]
        
        # Save as PNG with transparency support
        img_bw_rgb = img_bw.convert('RGB')
        img_bw_rgb.save(output_path, 'PNG', quality=95)
        print(f"✓ Saved favicon: {output_path}")
        
        # Also create ICO file with multiple sizes
        ico_path = 'portfolio/static/portfolio/images/favicon.ico'
        icon_sizes = [(size, size) for size in [16, 32, 48]]
        img_bw.save(ico_path, format='ICO', sizes=icon_sizes)
        print(f"✓ Saved ICO favicon: {ico_path}")
        
        print("\n✅ Favicon created successfully!")
        print(f"   - PNG: {output_path}")
        print(f"   - ICO: {ico_path}")
        print("   - Zoom: 150% (center crop)")
        print("   - Color: Black & White")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find {input_path}")
        print("   Make sure the image file exists")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    create_favicon()
