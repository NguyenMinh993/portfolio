# Azure Blob Storage Setup Guide

## Bước 1: Tạo Azure Storage Account

1. Đăng nhập vào [Azure Portal](https://portal.azure.com)
2. Tìm "Storage accounts" và click "Create"
3. Điền thông tin:
   - **Resource Group**: Tạo mới hoặc chọn có sẵn
   - **Storage account name**: `portfoliominh` (phải unique)
   - **Region**: Southeast Asia (gần Việt Nam nhất)
   - **Performance**: Standard
   - **Redundancy**: LRS (rẻ nhất)
4. Click "Review + Create" → "Create"

## Bước 2: Tạo Container

1. Vào Storage Account vừa tạo
2. Sidebar → "Containers"
3. Click "+ Container"
4. Tên: `portfolio-images`
5. Public access level: **Blob** (cho phép public access)
6. Click "Create"

## Bước 3: Lấy Connection String

1. Trong Storage Account, sidebar → "Access keys"
2. Click "Show keys"
3. Copy **Connection string** của key1 hoặc key2

## Bước 4: Cấu hình Environment Variables

### Local Development (.env file)
```env
# Azure Storage
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
AZURE_STORAGE_CONTAINER_NAME=portfolio-images

# PostgreSQL (Railway sẽ tự động set)
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### Railway Production
1. Vào Railway Dashboard → Your Project
2. Click "Variables" tab
3. Thêm các biến:
   - `AZURE_STORAGE_CONNECTION_STRING`: paste connection string
   - `AZURE_STORAGE_CONTAINER_NAME`: `portfolio-images`

## Bước 5: Tạo PostgreSQL Database trên Railway

1. Railway Dashboard → Click "+ New"
2. Chọn "Database" → "PostgreSQL"
3. Railway tự động tạo và set `DATABASE_URL`
4. Link database với service Django của bạn

## Bước 6: Run Migrations

```bash
# Local
python manage.py makemigrations
python manage.py migrate

# Tạo superuser để login admin
python manage.py createsuperuser
```

## Bước 7: Deploy lên Railway

```bash
git add .
git commit -m "Add PostgreSQL and Azure Blob Storage"
git push origin main
```

Railway sẽ tự động:
1. Detect thay đổi
2. Install dependencies
3. Run migrations
4. Deploy

## Bước 8: Tạo Admin User trên Production

```bash
# Trong Railway Dashboard → Service → Terminal
python manage.py createsuperuser
```

## Sử dụng Admin Panel

1. Truy cập: `https://your-app.railway.app/admin`
2. Login với superuser
3. Quản lý:
   - Projects (dự án)
   - Experience (kinh nghiệm)
   - Photos (ảnh photography)
   - Skills (kỹ năng)

## Upload Hình Ảnh

Khi upload hình trong admin panel:
- Hình sẽ tự động upload lên Azure Blob Storage
- URL sẽ được lưu vào database
- Hình có thể truy cập public qua URL

## Chi phí Azure

- **Free tier**: 5GB storage + 20,000 operations/month
- Sau đó: ~$0.02/GB/month
- Rất rẻ cho portfolio cá nhân!

## Troubleshooting

### Lỗi "AZURE_STORAGE_CONNECTION_STRING not set"
→ Kiểm tra environment variables đã set chưa

### Lỗi upload hình
→ Kiểm tra container có public access level = "Blob"

### Database connection error
→ Kiểm tra `DATABASE_URL` trong Railway variables
