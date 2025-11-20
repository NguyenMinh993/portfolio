"""
Azure Blob Storage utilities for uploading images
"""
import os
from azure.storage.blob import BlobServiceClient, ContentSettings
from django.conf import settings


class AzureStorage:
    def __init__(self):
        self.connection_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
        self.container_name = os.environ.get('AZURE_STORAGE_CONTAINER_NAME', 'portfolio-images')
        
        if not self.connection_string:
            raise ValueError("AZURE_STORAGE_CONNECTION_STRING not set in environment variables")
        
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        self._ensure_container_exists()
    
    def _ensure_container_exists(self):
        """Create container if it doesn't exist"""
        try:
            container_client = self.blob_service_client.get_container_client(self.container_name)
            if not container_client.exists():
                container_client.create_container(public_access='blob')
        except Exception as e:
            print(f"Error ensuring container exists: {e}")
    
    def upload_image(self, file, blob_name=None):
        """
        Upload image to Azure Blob Storage
        
        Args:
            file: Django UploadedFile object
            blob_name: Optional custom blob name, otherwise uses file name
            
        Returns:
            str: Public URL of uploaded blob
        """
        if blob_name is None:
            blob_name = file.name
        
        # Ensure unique filename
        blob_name = self._get_unique_blob_name(blob_name)
        
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            
            # Set content type based on file extension
            content_type = self._get_content_type(file.name)
            content_settings = ContentSettings(content_type=content_type)
            
            # Upload file
            blob_client.upload_blob(
                file.read(),
                content_settings=content_settings,
                overwrite=True
            )
            
            # Return public URL
            return blob_client.url
        
        except Exception as e:
            raise Exception(f"Failed to upload image to Azure: {str(e)}")
    
    def delete_image(self, blob_url):
        """
        Delete image from Azure Blob Storage
        
        Args:
            blob_url: Full URL of the blob to delete
        """
        try:
            # Extract blob name from URL
            blob_name = blob_url.split('/')[-1]
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            blob_client.delete_blob()
            return True
        except Exception as e:
            print(f"Error deleting blob: {e}")
            return False
    
    def _get_unique_blob_name(self, filename):
        """Generate unique blob name to avoid conflicts"""
        import uuid
        from pathlib import Path
        
        name = Path(filename).stem
        ext = Path(filename).suffix
        unique_id = str(uuid.uuid4())[:8]
        return f"{name}_{unique_id}{ext}"
    
    def _get_content_type(self, filename):
        """Get content type based on file extension"""
        ext = filename.lower().split('.')[-1]
        content_types = {
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif',
            'webp': 'image/webp',
            'svg': 'image/svg+xml',
        }
        return content_types.get(ext, 'application/octet-stream')


# Singleton instance
_azure_storage = None

def get_azure_storage():
    """Get or create Azure Storage instance"""
    global _azure_storage
    if _azure_storage is None:
        _azure_storage = AzureStorage()
    return _azure_storage
