# Personal Website

A personal website built with Django to present personal information, skills, services, resume, blog posts, and contact information.

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=FFD43B&labelColor=1F2937" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=44B78B&labelColor=1F2937" alt="Django">
  </a>
  <a href="https://www.mysql.com/">
    <img src="https://img.shields.io/badge/MySQL-00758F?style=flat&logo=mysql&logoColor=FFFFFF&labelColor=1F2937" alt="MySQL">
  </a>
  <a href="https://docs.astral.sh/uv/">
    <img src="https://img.shields.io/badge/uv-6E56CF?style=flat&logo=uv&logoColor=FFFFFF&labelColor=1F2937" alt="uv">
  </a>
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=FFFFFF&labelColor=1F2937" alt="Docker">
  </a>
  <a href="https://hub.docker.com/">
    <img src="https://img.shields.io/badge/Docker%20Hub-2496ED?style=flat&logo=docker&logoColor=FFFFFF&labelColor=1F2937" alt="Docker Hub">
  </a>
</p>

<p align="center">
  <a href="https://github.com/unfoldadmin/django-unfold">
    <img src="https://img.shields.io/badge/Django%20Unfold-2563EB?style=flat&logo=django&logoColor=FFFFFF&labelColor=1F2937" alt="Django Unfold">
  </a>
  <a href="https://pypi.org/project/django-unfold-rtl/">
    <img src="https://img.shields.io/badge/Unfold%20RTL-7C3AED?style=flat&logo=django&logoColor=FFFFFF&labelColor=1F2937" alt="django-unfold-rtl">
  </a>
  <a href="https://pypi.org/project/django-cleanup/">
    <img src="https://img.shields.io/badge/django--cleanup-16A34A?style=flat&logo=python&logoColor=FFFFFF&labelColor=1F2937" alt="django-cleanup">
  </a>
  <a href="https://pypi.org/project/django-social-share/">
    <img src="https://img.shields.io/badge/django--social--share-DB2777?style=flat&logo=sharethis&logoColor=FFFFFF&labelColor=1F2937" alt="django-social-share">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/LGPL--2.1-D97706?style=flat&logo=opensourceinitiative&logoColor=FFFFFF&labelColor=1F2937" alt="License: LGPL 2.1">
  </a>
</p>

---

## 📸 Preview

### Home Page

<p align="center">
  <img src="docs/images/home-preview.png" alt="Home page preview" width="90%">
</p>

### About Page

<p align="center">
  <img src="docs/images/about-preview.png" alt="About page preview" width="90%">
</p>

---

## ✨ Features

- Personal profile and information
- Skills and services management
- Resume management
- Blog and article management
- Contact information management
- Social media management
- Customized Django Admin panel
- Modern Admin interface with Django Unfold
- RTL support for the Admin panel
- Jalali date support
- Automatic cleanup of uploaded files
- Social sharing functionality
- Environment-based configuration for sensitive settings
- Docker and Docker Compose support

---

## 🛠️ Technologies

- Python
- Django
- MySQL
- Docker
- Docker Compose
- Django Unfold
- django-unfold-rtl
- django-cleanup
- django-social-share
- python-dotenv
- jdatetime
- uv

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/MMahdiGhaioumi/personal_website.git
cd personal_website
```

### 2. Install dependencies

The project provides both `pyproject.toml` and `requirements.txt`.

#### Using `requirements.txt`

```bash
pip install -r requirements.txt
```

#### Using `uv`

```bash
uv sync
```

---

### 3. Install MySQL

Install MySQL Server and make sure the service is running.

Create a database:

```sql
CREATE DATABASE personal_website;
```

---

### 4. Configure environment variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Configure your database:

```env
DB_NAME=personal_website
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
```

> **Important:** Never commit `.env` to Git or GitHub.

---

### 5. Generate a Django Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Add the generated value to `.env`:

```env
SECRET_KEY=your_generated_secret_key
```

---

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

Admin: `http://127.0.0.1:8000/admin/`

---

# 🐳 Docker Installation

The project includes `Dockerfile`, `.dockerignore`, and `docker-compose.yml`, so it can be run using Docker and Docker Compose.

### 🐳 1. Install Docker

Install Docker and Docker Compose, then verify:

```bash
docker --version
docker compose version
```

### ⚙️ 2. Configure `.env`

Create the environment file:

```bash
cp .env.example .env
```

Configure the required values:

```env
SECRET_KEY=your_generated_secret_key

DB_NAME=personal_website
DB_HOST=db
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
```

When Django runs inside Docker Compose, `DB_HOST` should normally be the database service name from `docker-compose.yml`, not `localhost`.

> **Important:** Never commit `.env` to GitHub.

### 🏗️ 3. Build the images

Build the images:

```bash
docker compose build
```

Or build and start everything at once:

```bash
docker compose up --build
```

### ▶️ 4. Start the project

Start normally:

```bash
docker compose up
```

Or in the background:

```bash
docker compose up -d
```

Open:

`http://127.0.0.1:8000/`

### 🗃️ 5. Run migrations

If the Django service is named `web`:

```bash
docker compose exec web python manage.py migrate
```

If your `docker-compose.yml` uses another service name, replace `web` with that name.

### 👤 6. Create a superuser

```bash
docker compose exec web python manage.py createsuperuser
```

### 📋 7. View logs

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

For the Django service:

```bash
docker compose logs -f web
```

### 🛑 8. Stop the project

```bash
docker compose down
```

This stops and removes the containers and Compose network. Named volumes are not removed unless explicitly requested.

### 🔄 9. Rebuild after dependency changes

If you change `requirements.txt`, `pyproject.toml`, or `Dockerfile`:

```bash
docker compose up --build
```

---

## ⚙️ Environment Variables

The project uses environment variables for sensitive configuration.

```env
SECRET_KEY=
DB_NAME=
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
```

Use `.env.example` as the template for your local `.env`.

---

## 📁 Project Structure

```text
personal_website/
│
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── manage.py
├── pyproject.toml
├── requirements.txt
├── README.md
│
├── docs/
│   └── images/
│       ├── home-preview.png
│       └── about-preview.png
│
└── ...
```

---

## 🎨 Django Admin

The project uses [Django Unfold](https://github.com/unfoldadmin/django-unfold) for a modern Django Admin interface.

[django-unfold-rtl](https://pypi.org/project/django-unfold-rtl/) provides RTL support for the Admin interface.

---

## 🧹 File Cleanup

The project uses [django-cleanup](https://pypi.org/project/django-cleanup/) to automatically clean up files associated with `FileField` and `ImageField`.

---

## 🔗 Social Sharing

The project uses [django-social-share](https://pypi.org/project/django-social-share/) to provide social sharing functionality.

---

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Django Unfold](https://github.com/unfoldadmin/django-unfold)
- [django-unfold-rtl](https://pypi.org/project/django-unfold-rtl/)
- [django-cleanup](https://pypi.org/project/django-cleanup/)
- [django-social-share](https://pypi.org/project/django-social-share/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [jdatetime](https://pypi.org/project/jdatetime/)

---

## 📄 License

This project is licensed under the **LGPL-2.1** license.

See the [`LICENSE`](LICENSE) file for more information.

---

Made with ❤️ by **Mohammad Mahdi Ghaioumi**
