"""
Cloudinary Storage utilities for uploading images
Alternative to Azure Blob Storage - easier setup, better free tier
"""
import os
import cloudinary
import cloudinary.uploader
from django.conf import settings


class CloudinaryStorage:
    def __init__(self):
        # Configure Cloudinary
        cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME')
        api_key = os.environ.get('CLOUDINARY_API_KEY')
        api_secret = os.environ.get('CLOUDINARY_API_SECRET')
        
        # Validate configuration
        if not all([cloud_name, api_key, api_secret]):
            print("⚠️  Warning: Cloudinary credentials not set")
            print(f"CLOUDINARY_CLOUD_NAME: {'✓' if cloud_name else '✗'}")
            print(f"CLOUDINARY_API_KEY: {'✓' if api_key else '✗'}")
            print(f"CLOUDINARY_API_SECRET: {'✓' if api_secret else '✗'}")
            raise ValueError("Cloudinary credentials not set in environment variables")
        
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True
        )
        
        print(f"✅ Cloudinary configured: {cloud_name}")
    
    def upload_image(self, file, folder='portfolio'):
        """
        Upload image to Cloudinary with automatic optimization
        
        Args:
            file: Django UploadedFile object
            folder: Cloudinary folder name (default: 'portfolio')
            
        Returns:
            str: Public URL of uploaded image
        """
        try:
            # Upload with transformations
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type='image',
                # Automatic optimizations
                transformation=[
                    {'width': 1200, 'height': 800, 'crop': 'limit'},  # Max dimensions
                    {'quality': 'auto'},  # Auto quality
                    {'fetch_format': 'auto'}  # Auto format (WebP if supported)
                ],
                # Generate unique filename
                use_filename=True,
                unique_filename=True
            )
            
            return result['secure_url']
        
        except Exception as e:
            raise Exception(f"Failed to upload image to Cloudinary: {str(e)}")
    
    def upload_photo(self, file, folder='photos'):
        """
        Upload photo with higher quality for photography portfolio
        
        Args:
            file: Django UploadedFile object
            folder: Cloudinary folder name (default: 'photos')
            
        Returns:
            dict: URLs for full image and thumbnail
        """
        try:
            # Upload original
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type='image',
                transformation=[
                    {'width': 1920, 'height': 1080, 'crop': 'limit'},
                    {'quality': 'auto:best'}
                ],
                use_filename=True,
                unique_filename=True
            )
            
            # Generate thumbnail URL
            public_id = result['public_id']
            thumbnail_url = cloudinary.CloudinaryImage(public_id).build_url(
                width=400,
                height=300,
                crop='fill',
                quality='auto'
            )
            
            return {
                'image_url': result['secure_url'],
                'thumbnail_url': thumbnail_url
            }
        
        except Exception as e:
            raise Exception(f"Failed to upload photo to Cloudinary: {str(e)}")
    
    def delete_image(self, image_url):
        """
        Delete image from Cloudinary
        
        Args:
            image_url: Full URL of the image to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Extract public_id from URL
            # URL format: https://res.cloudinary.com/{cloud_name}/image/upload/v{version}/{public_id}.{format}
            parts = image_url.split('/')
            if 'cloudinary.com' in image_url:
                # Find the public_id (after 'upload/')
                upload_index = parts.index('upload')
                public_id_with_ext = '/'.join(parts[upload_index + 2:])  # Skip version
                public_id = public_id_with_ext.rsplit('.', 1)[0]  # Remove extension
                
                cloudinary.uploader.destroy(public_id)
                return True
            return False
        
        except Exception as e:
            print(f"Error deleting from Cloudinary: {e}")
            return False


# Singleton instance
_cloudinary_storage = None

def get_cloudinary_storage():
    """Get or create Cloudinary Storage instance"""
    global _cloudinary_storage
    if _cloudinary_storage is None:
        _cloudinary_storage = CloudinaryStorage()
    return _cloudinary_storage
