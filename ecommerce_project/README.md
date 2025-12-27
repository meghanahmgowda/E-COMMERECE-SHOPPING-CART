E-Commerce Store Django Project

A medium-level e-commerce web application built using Django and Bootstrap.
Users can browse products, add items to the cart, and checkout. This project uses a session-based shopping cart and displays 100 sample products with images.

Features

User-friendly product catalog

Product details page with quantity selection

Shopping cart functionality:

Add / remove items

View subtotal, tax, and grand total

Checkout page

Responsive Bootstrap 5 design

Admin interface to manage products

Session-based cart (no login required)

Technologies Used

Python 3.x

Django 4.x

SQLite (default Django database)

HTML / CSS / Bootstrap 5

Picsum Photos for placeholder images

Project Structure
ecommerce_project/
│
├── ecommerce_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── store/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── management/
│   │   └── commands/add_sample_products.py
│   ├── templates/store/
│   │   ├── base.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   └── checkout_success.html
│   └── migrations/
│       └── __init__.py
│
├── static/css/style.css
├── manage.py
└── db.sqlite3

Setup Instructions
1. Clone the Project
git clone <repository-url>
cd ecommerce_project

2. Create a Virtual Environment (Optional but recommended)
python -m venv venv
# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install django

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Add Sample Products
python manage.py add_sample_products


This adds 100 sample ladies’ dresses with placeholder images.

6. Run the Development Server
python manage.py runserver

7. Open in Browser

Go to http://127.0.0.1:8000
 to view the store.

Admin Panel

Create a superuser to access Django admin:

python manage.py createsuperuser


Visit http://127.0.0.1:8000/admin/
 to manage products.

Static Files

CSS files: static/css/style.css

Bootstrap 5 CDN used for styling.

Images use placeholder URLs (Picsum Photos) for testing.

Notes

The project uses session-based cart, so no login is required for shopping.

If you encounter template errors like {% static %} not found, ensure {% load static %} is included at the top of templates.
