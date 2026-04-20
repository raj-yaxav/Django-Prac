# 🧩 Django CRUD App with Authentication

A complete Django project implementing full CRUD operations with user authentication and authorization.  
Each user has their own private data — secured routes, clean UI, and a working admin panel.

---

## 🚀 Features

- 🔐 User Signup & Login System
- ➕ Create Cards
- ✏️ Update Cards
- ❌ Delete Cards
- 👤 User-specific data (each user sees only their own cards)
- 🔒 Secure routes using `@login_required`
- 🛡️ Ownership check — users can only edit/delete their own data

---

## 🧠 Concepts Covered

- Django Models & Migrations
- Views & URL Routing
- Templates & Template Tags
- GET & POST Requests
- Authentication System (`django.contrib.auth`)
- Database Relationships (`ForeignKey` → User)
- Django Admin Panel
- Flash messages (`django.contrib.messages`)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| Framework | Django |
| Database | SQLite |
| Frontend | HTML / CSS |

---

## 📂 Project Structure

```
crud/
│
├── home/
│   ├── models.py          → Card model with ForeignKey to User
│   ├── views.py           → CRUD views with auth checks
│   ├── urls.py            → App-level URL patterns
│   └── admin.py           → Registered models
│
├── templates/
│   └── card/
│       ├── home.html      → Dashboard — lists user's cards
│       ├── create.html    → Create new card
│       └── update.html    → Edit existing card
│
├── static/                → CSS & static assets
├── manage.py
└── db.sqlite3
```

---

## 🚀 How to Run

```bash
git clone <repo-link>
cd crud
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 Admin Panel

```bash
python manage.py createsuperuser
```

Then open: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🎯 Key Learning Outcomes

- Built a real-world Django app from scratch
- Implemented full CRUD with proper ownership logic
- Secured routes so unauthenticated users are redirected to login
- Understood `ForeignKey` relationships between models
- Used Django's built-in auth system instead of building one from scratch

---

## 📌 Future Improvements

- [ ] UI enhancement (modern design with Bootstrap or Tailwind)
- [ ] Search & filter functionality
- [ ] Pagination for large card lists
- [ ] Image/file attachment to cards
- [ ] Deployment (Railway / Render)

---

## 👨‍💻 Author

**Raj Yadav** — Full Stack Developer · MERN · Django  
📧 rajyaxav098@gmail.com · 🐙 [github.com/Raj-yadav-06](https://github.com/Raj-yadav-06)