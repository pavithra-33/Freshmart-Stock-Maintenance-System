## 🛒 FreshMart Stock Maintenance System

The **FreshMart Stock Maintenance System** is a web-based full-stack application built with **Flask (Python)** for backend logic, **MongoDB** for database storage, and **HTML/CSS** for the frontend.

It enables businesses to **add, view, update, and delete** stock items efficiently while ensuring persistent storage in **MongoDB**.

---

## 📂 Project Structure

```
Stock_Maintenance/
│
├── static/                     # Contains all CSS files
│   ├── home.css
│   ├── dashboard.css
│   ├── add.css
│   ├── delete.css
│   ├── update.css
│   ├── view.css
│
├── templates/                  # Contains HTML files for pages
│   ├── home.html
│   ├── dashboard.html
│   ├── add.html
│   ├── delete.html
│   ├── update.html
│   ├── view.html
│
├── app.py                      # Main Flask application (with MongoDB integration)
│
└── README.md                   # Project documentation
```

---

## ⚙️ Features

✅ **Home Page** – Entry point with navigation to login/dashboard.
✅ **Dashboard** – Hub for stock management operations.
✅ **Add Stock** – Insert new items into MongoDB.
✅ **View Stock** – Retrieve and display inventory from MongoDB.
✅ **Update Stock** – Modify stock details directly in MongoDB.
✅ **Delete Stock** – Remove stock records by Product ID from MongoDB.
✅ **Persistent Storage** – All operations are saved in **MongoDB**, ensuring data is never lost after restarting the app.
✅ **CSS Styling** – Separate CSS files for each page for a clean and modular UI.

---

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/Stock_Maintenance.git
cd Stock_Maintenance
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install flask pymongo dnspython
```

### 4. Set Up MongoDB

* Create a free **MongoDB Atlas Cluster** (or run MongoDB locally).
* Get your **connection string (URI)**, e.g.:

```python
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("your_mongodb_connection_uri")
db = client["stockdb"]
collection = db["stocks"]
```

### 5. Run the Flask App

```bash
python app.py
```

### 6. Access the Application

Open your browser and go to:
👉 `http://127.0.0.1:5000/`

---

## 🔑 Usage Guide

1. **Home Page** → Navigate to the system.
2. **Dashboard** → Access Add, View, Update, Delete functions.
3. **Add Stock** → Fill in details → Data saved in MongoDB.
4. **View Stock** → Fetches inventory directly from MongoDB.
5. **Update Stock** → Updates existing stock entry by Product ID.
6. **Delete Stock** → Removes entry from MongoDB.

## 🛠️ Technologies Used

* **Backend**: Flask (Python)
* **Database**: MongoDB Atlas / Local MongoDB
* **Frontend**: HTML, CSS (separate files for each page)
* **ORM/Driver**: PyMongo

## 🔮 Future Enhancements

* Add **user authentication** (Admin vs Staff).
* Low-stock alerts (when quantity < 10).
* Generate reports (PDF/Excel).
* Sales tracking and dashboard analytics.
* Multi-branch support with centralized database.


## 👩‍💻 Author

Developed by Pavithra Bharathidasan
