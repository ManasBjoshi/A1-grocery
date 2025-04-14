# 🛒 A1-Grocery

**A1-Grocery** is a modern and user-friendly online grocery shopping platform built using Django for the backend and HTML, CSS, JavaScript for the frontend. It allows users to browse products, add items to their cart, and place orders with ease.

## 🔧 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Django (Python)
- **Database**: SQLite (default Django DB)

## 🌟 Features

- 🔐 User Authentication (Login/Signup)
- 🛍️ Product Browsing and Search
- 🛒 Add to Cart and Checkout
- 📦 Order Placement and Confirmation
- 🖼️ Clean and Responsive UI

## 🚀 Getting Started

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.7+
- Git
- Virtualenv (optional but recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/ManasBjoshi/A1-grocery.git
cd A1-grocery

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (admin access)
python manage.py createsuperuser

# Start the development server
python manage.py runserver


Open your browser and go to http://127.0.0.1:8000/ to view the app.
# Project Structure
A1-grocery/
├── grocery/              # Main app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── A1_grocery/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt

# 🙌 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.
