# Cloudinary Setup Guide (Alternative to Azure)

## Tại sao dùng Cloudinary?
- ✅ Dễ setup hơn Azure
- ✅ Free tier: 25GB storage + 25GB bandwidth/month
- ✅ Tự động optimize ảnh
- ✅ Không cần thẻ tín dụng

## Bước 1: Tạo Tài Khoản

1. Truy cập: https://cloudinary.com/users/register/free
2. Điền thông tin:
   - Email
   - Password
   - Cloud name (tên unique, ví dụ: `portfolio-minh`)
3. Verify email
4. Login vào dashboard

## Bước 2: Lấy API Credentials

1. Dashboard → Settings (góc trên phải)
2. Scroll xuống "Account Details"
3. Copy các thông tin:
   - **Cloud Name**: portfolio-minh
   - **API Key**: 123456789012345
   - **API Secret**: abcdefghijklmnopqrstuvwxyz

## Bước 3: Install Package

```bash
pip install cloudinary
```

## Bước 4: Update Code

Tạo file mới: `portfolio/cloudinary_storage.py`

```python
import cloudinary
import cloudinary.uploader
import os
from django.conf import settings

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

class CloudinaryStorage:
    def upload_image(self, file, folder='portfolio'):
        """Upload image to Cloudinary"""
        try:
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type='image',
                transformation=[
                    {'width': 1200, 'height': 800, 'crop': 'limit'},
                    {'quality': 'auto'},
                    {'fetch_format': 'auto'}
                ]
            )
            return result['secure_url']
        except Exception as e:
            raise Exception(f"Failed to upload to Cloudinary: {str(e)}")
    
    def delete_image(self, public_id):
        """Delete image from Cloudinary"""
        try:
            cloudinary.uploader.destroy(public_id)
            return True
        except Exception as e:
            print(f"Error deleting from Cloudinary: {e}")
            return False

def get_cloudinary_storage():
    return CloudinaryStorage()
```

## Bước 5: Update Forms

Update `portfolio/forms.py`:

```python
# Thay đổi import
from .cloudinary_storage import get_cloudinary_storage

# Trong ProjectForm.save():
cloudinary_storage = get_cloudinary_storage()
image_url = cloudinary_storage.upload_image(image_file)
```

## Bước 6: Environment Variables

### Local (.env)
```env
CLOUDINARY_CLOUD_NAME=portfolio-minh
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=your-api-secret
```

### Railway
Add variables:
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

## Bước 7: Update requirements.txt

```
cloudinary==1.36.0
```

## Deploy

```bash
git add .
git commit -m "Switch to Cloudinary for image storage"
git push origin main
```

## So Sánh Azure vs Cloudinary

| Feature | Azure Blob | Cloudinary |
|---------|-----------|------------|
| Free Storage | 5GB | 25GB |
| Free Bandwidth | 20K ops | 25GB/month |
| Setup | Phức tạp | Dễ |
| Credit Card | Cần | Không cần |
| Auto Optimize | Không | Có |
| CDN | Cần setup | Built-in |

## Khuyến nghị

Dùng **Cloudinary** cho portfolio vì:
- Dễ setup
- Free tier tốt hơn
- Tự động optimize ảnh
- Không cần thẻ tín dụng
