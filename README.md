# Resume App

A Django-powered personal portfolio site: home page, portfolio gallery, blog, testimonials, and a contact form, all editable from the Django admin (rich text via CKEditor). Live at [resume-app-pgqw.onrender.com](https://resume-app-pgqw.onrender.com/).

## Features

- **Portfolio** and **Blog** sections with slug-based detail pages, managed as Django models.
- **Skills**, **Testimonials**, and **Certificates** displayed on the home page.
- **Contact form** that stores submissions (`ContactProfile`) in the database.
- Media (avatar, CV, project images) served through Django's media handling; static assets served via WhiteNoise.

## Stack

Django 5, django-ckeditor, WhiteNoise (static files), Gunicorn (WSGI server), SQLite, deployed on Render.

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Set the `SECRET_KEY` environment variable in any real deployment (a local-only fallback is used in development). Set `DEBUG=True` only for local development — it defaults to `False`.
