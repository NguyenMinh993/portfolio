"""
Script to rotate gen-h-film3.jpg to correct orientation
"""
from PIL import Image
import os

def rotate_film3():
    # Input and output paths
    input_path = 'portfolio/static/portfolio/images/gen-h-film3.jpg'
    
    try:
        # Open the image
        img = Image.open(input_path)
        print(f"✓ Loaded image: {img.size}")
        print(f"✓ Original orientation: {img.width}x{img.height}")
        
        # Rotate 90 degrees clockwise (to make vertical image horizontal)
        img_rotated = img.rotate(-90, expand=True)
        print(f"✓ Rotated 90° clockwise: {img_rotated.size}")
        
        # Save the rotated image (overwrite original)
        img_rotated.save(input_path, 'JPEG', quality=95)
        print(f"✓ Saved rotated image: {input_path}")
        
        print("\n✅ Image rotated successfully!")
        print(f"   - New dimensions: {img_rotated.width}x{img_rotated.height}")
        print(f"   - Rotation: 90° clockwise")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find {input_path}")
        print("   Make sure the image file exists")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    rotate_film3()
