# Django Portfolio - Nguyen Van Minh

A modern, dynamic portfolio website built with Django, featuring interactive animations, photography showcase, and admin panel for content management.

🌐 **Live Site:** [nguyenminh993.up.railway.app](https://nguyenminh993.up.railway.app)

## ✨ Features

### Main Portfolio Page
- **Interactive Hero Section** with typing animation and gradient effects
- **Professional Experience** showcase with detailed project descriptions
- **Skills & Certifications** display
- **Contact Form** with SendGrid email integration
- **Responsive Design** optimized for all devices

### Photography & Film Page
- **Dual Gallery System**: Main gallery + B&W collection
- **Animated Image Showcases** with hover effects
- **Film-style Image Frames** with vintage aesthetics
- **Smooth Scroll Animations** using Intersection Observer

### Admin Features
- **Django Admin Panel** for content management
- **CRUD Operations** for projects, photos, experiences, skills
- **Cloudinary Integration** for image storage
- **Custom Forms** with validation

## 🛠️ Technologies

**Backend:**
- Django 5.1.3
- Python 3.12
- PostgreSQL (Production)
- SQLite (Development)

**Frontend:**
- HTML5, CSS3 with custom animations
- JavaScript (Vanilla)
- Google Fonts (Inter, Space Mono)

**Deployment & Services:**
- Railway (Hosting)
- Cloudinary (Image Storage)
- SendGrid (Email Service)
- WhiteNoise (Static Files)
- Gunicorn (WSGI Server)

## 📦 Installation

### Prerequisites
- Python 3.12+
- pip
- Virtual environment

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/NguyenMinh993/portfolio.git
cd portfolio
```

2. **Create virtual environment:**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create `.env` file:
```env
SECRET_KEY=your-secret-key
DEBUG=True
SENDGRID_API_KEY=your-sendgrid-key
FROM_EMAIL=your-email@example.com
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create superuser:**
```bash
python manage.py createsuperuser
# Or use the script
python create_superuser.py
```

7. **Collect static files:**
```bash
python manage.py collectstatic
```

8. **Run development server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

## 🚀 Deployment (Railway)

The project is configured for Railway deployment with:
- `railway.toml` - Railway configuration
- `build.sh` - Build script
- `requirements-prod.txt` - Production dependencies
- Gunicorn WSGI server
- PostgreSQL database
- WhiteNoise for static files

### Deploy to Railway:
1. Connect GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push to main branch

## 📚 Documentation

- **CLOUDINARY_SETUP.md** - Cloudinary configuration guide
- **DATABASE_CRUD_GUIDE.md** - Admin panel usage
- **DEPLOYMENT.md** - Deployment instructions
- **RAILWAY_DATABASE_SETUP.md** - Railway database setup
- **SENDGRID_ANTI_SPAM_SETUP.md** - Email deliverability guide

## 🔧 Utility Scripts

- `create_superuser.py` - Create admin user
- `create_favicon.py` - Generate favicon from images
- `update_portfolio.py` - Bulk update portfolio data

## 📁 Project Structure

```
portfolio/
├── DjangoProject/          # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/              # Main app
│   ├── admin.py           # Admin configuration
│   ├── forms.py           # Form definitions
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── static/            # Static files
│   └── templates/         # HTML templates
├── staticfiles/           # Collected static files
├── manage.py
├── requirements.txt
└── README.md
```

## 🎨 Features in Detail

### Contact Form
- Email validation
- File attachment support
- SendGrid integration
- Beautiful HTML email templates
- Anti-spam configuration

### Image Management
- Cloudinary storage
- Automatic thumbnail generation
- Grayscale filter for B&W gallery
- Responsive image loading

### Admin Panel
- Custom forms with image upload
- CRUD operations for all models
- Cloudinary integration
- User authentication

## 🔒 Security

- Environment variables for sensitive data
- CSRF protection
- Secure password hashing
- SQL injection prevention
- XSS protection

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Nguyen Van Minh**
- Email: nguyenminh090903@gmail.com
- GitHub: [@NguyenMinh993](https://github.com/NguyenMinh993)
- LinkedIn: [Văn Minh Nguyễn](https://www.linkedin.com/in/văn-minh-nguyễn)

---

*Built with ❤️ using Django*
