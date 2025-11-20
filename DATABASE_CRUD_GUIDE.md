# Hướng Dẫn Sử Dụng Database & CRUD với Azure

## 📋 Tổng Quan

Hệ thống bao gồm:
- **PostgreSQL Database**: Lưu trữ dữ liệu (Railway)
- **Azure Blob Storage**: Lưu trữ hình ảnh
- **Django Admin Panel**: Giao diện CRUD (có authentication)

## 🗄️ Models Đã Tạo

### 1. Project (Dự án)
- Tiêu đề, mô tả, tech stack
- GitHub URL, Live URL
- Hình ảnh (lưu trên Azure)
- Thứ tự hiển thị, featured

### 2. Experience (Kinh nghiệm làm việc)
- Vị trí, công ty
- Tech stack, mô tả
- Ngày bắt đầu/kết thúc
- Thứ tự hiển thị

### 3. Photo (Ảnh Photography)
- Tiêu đề, mô tả
- Category (Digital/Film)
- Hình ảnh (lưu trên Azure)
- Thumbnail, featured

### 4. Skill (Kỹ năng)
- Tên skill
- Category (Frontend/Backend/Database...)
- Proficiency (0-100)

## 🚀 Setup Local

### Bước 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Bước 2: Setup Environment Variables
Copy `.env.example` thành `.env` và điền thông tin:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://localhost/portfolio
AZURE_STORAGE_CONNECTION_STRING=your-azure-connection-string
AZURE_STORAGE_CONTAINER_NAME=portfolio-images
```

### Bước 3: Setup Database
```bash
# Tạo migrations
python manage.py makemigrations

# Chạy migrations
python manage.py migrate

# Tạo superuser (admin account)
python manage.py createsuperuser
# Nhập: username, email, password
```

### Bước 4: Run Server
```bash
python manage.py runserver
```

Truy cập:
- Website: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## 🔐 Admin Panel Authentication

### Login
1. Truy cập: http://localhost:8000/admin
2. Nhập username/password của superuser
3. Vào dashboard quản lý

### Tạo User Mới
```bash
python manage.py createsuperuser
```

Hoặc trong admin panel:
1. Sidebar → "Users"
2. Click "Add User"
3. Điền thông tin và set permissions

## 📝 CRUD Operations

### Thêm Project Mới
1. Admin → "Projects" → "Add Project"
2. Điền thông tin:
   - Title: "E-Commerce Platform"
   - Description: "Full stack e-commerce..."
   - Tech Stack: "Django, PostgreSQL, React"
   - GitHub URL: https://github.com/...
3. **Upload Image**:
   - Click "Choose File" ở field "Image file"
   - Chọn ảnh từ máy
   - Ảnh sẽ tự động upload lên Azure
   - URL sẽ tự động điền vào "Image url"
4. Set Order và Featured
5. Click "Save"

### Sửa Project
1. Admin → "Projects" → Click vào project
2. Sửa thông tin
3. Upload ảnh mới nếu muốn thay đổi
4. Click "Save"

### Xóa Project
1. Admin → "Projects"
2. Tick checkbox project muốn xóa
3. Action dropdown → "Delete selected projects"
4. Confirm

### Tương tự cho Experience, Photo, Skill

## 🖼️ Upload Hình Ảnh

### Cách hoạt động:
1. Chọn file ảnh trong admin form
2. Click Save
3. Django tự động:
   - Upload ảnh lên Azure Blob Storage
   - Lấy public URL
   - Lưu URL vào database
4. Ảnh có thể truy cập public qua URL

### Supported Formats:
- JPG/JPEG
- PNG
- GIF
- WEBP

### Best Practices:
- Resize ảnh trước khi upload (khuyến nghị < 2MB)
- Dùng tên file có ý nghĩa
- Projects: 1200x800px
- Photos: 1920x1080px

## 🌐 Deploy lên Railway

### Bước 1: Setup PostgreSQL trên Railway
1. Railway Dashboard → "+ New"
2. Chọn "Database" → "PostgreSQL"
3. Railway tự động tạo và set `DATABASE_URL`

### Bước 2: Setup Azure Blob Storage
Xem file `AZURE_SETUP.md` để setup Azure

### Bước 3: Set Environment Variables
Railway Dashboard → Variables:
```
SECRET_KEY=your-production-secret-key
DEBUG=False
AZURE_STORAGE_CONNECTION_STRING=your-azure-connection
AZURE_STORAGE_CONTAINER_NAME=portfolio-images
SENDGRID_API_KEY=your-sendgrid-key
FROM_EMAIL=your-email@gmail.com
```

### Bước 4: Deploy
```bash
git add .
git commit -m "Add database and Azure storage"
git push origin main
```

### Bước 5: Run Migrations trên Production
Railway Dashboard → Service → Terminal:
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Bước 6: Access Admin
Truy cập: `https://your-app.railway.app/admin`

## 🔧 Troubleshooting

### Lỗi "No such table"
```bash
python manage.py migrate
```

### Lỗi "AZURE_STORAGE_CONNECTION_STRING not set"
Kiểm tra environment variables đã set chưa

### Lỗi upload ảnh
- Kiểm tra Azure container có public access
- Kiểm tra connection string đúng
- Kiểm tra file size < 10MB

### Lỗi "Permission denied" trong admin
- Đảm bảo user có staff status
- Check user permissions trong admin

## 📊 Database Schema

```
Project
├── id (auto)
├── title
├── description
├── tech_stack
├── github_url
├── live_url
├── image_url (Azure URL)
├── order
├── is_featured
├── created_at
└── updated_at

Experience
├── id
├── title
├── company
├── tech_stack
├── description
├── start_date
├── end_date
├── order
├── created_at
└── updated_at

Photo
├── id
├── title
├── description
├── category
├── image_url (Azure URL)
├── thumbnail_url
├── order
├── is_featured
├── created_at
└── updated_at

Skill
├── id
├── name
├── category
├── proficiency
└── order
```

## 🎯 Next Steps

1. ✅ Setup Azure Blob Storage
2. ✅ Setup PostgreSQL trên Railway
3. ✅ Set environment variables
4. ✅ Deploy code
5. ✅ Run migrations
6. ✅ Create superuser
7. ✅ Login admin và thêm data
8. 🔄 Update views.py để hiển thị data từ database
9. 🔄 Update templates để render dynamic content

## 💡 Tips

- Backup database thường xuyên
- Dùng featured flag để highlight projects quan trọng
- Order field để sắp xếp thứ tự hiển thị
- Azure free tier: 5GB storage (đủ cho portfolio)
- PostgreSQL trên Railway: Free tier 500MB

## 📞 Support

Nếu gặp vấn đề:
1. Check logs: Railway Dashboard → Deployments → Logs
2. Check database: Railway → PostgreSQL → Data
3. Check Azure: Azure Portal → Storage Account → Containers
