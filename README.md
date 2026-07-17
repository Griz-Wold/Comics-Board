# Comics Board
A web application built with Django for posting and browsing comic and manga advertisements, featuring user authentication and image uploads.

## Features

### Authentication & User Profile
- Custom user model with avatar support
- User registration, login, and logout (via standard Django auth system)
- User profile page with username, email and avatar

### Adмукшыьутеы (Postings)
- Full CRUD functionality for ads (Create, Read, Update, Delete)
- Clean list view for browsing all ads
- Detailed view page for each individual posting

### General
- Server-side rendering using Django templates
- Static files support (images, styles)
- Media handling for user-uploaded content (avatars and comic images)

## Tech stack
- Python
- Django
- SQLite
- HTML / CSS (templates)
- Bootstrap

## Project structure
- "accounts" - User registration, authentication, and profile management
- "postings" - Core ads logic (creating, viewing, and managing listings)
- "comics_board" - Main Django project configuration

## How to run

```bash
git clone https://github.com/Griz-Wold/Comics-Board.git
cd Comics-Board

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
