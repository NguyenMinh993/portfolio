#!/bin/bash
# Setup database script

echo "🔄 Making migrations..."
python manage.py makemigrations

echo "🔄 Running migrations..."
python manage.py migrate

echo "✅ Database setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Create superuser: python manage.py createsuperuser"
echo "2. Access admin: http://localhost:8000/admin"
