# Comics Board
Web application built with Django for postings and browsing comic and manga ads.

## Features

### Authentication & User Profile
- Custom user model with avatar support
- User registration
- Login/logout (via Django auth system)
- User profile page with username, email and avatar

### Ads (Postings)
- Create ads for comics and manga
- View list of ads
- View detailed page for each ad
- Basic CRUD functionality for postings

### General
- Django templates for rendering pages
- Static files support (images, styles)
- Media handling for user avatars

## Tech stack
- Python
- Django
- SQLite
- HTML / CSS (templates)

## Project structure
- "accounts" - user registration, authentication and profile
- "postings" - ads logic (creating, viewing, managing)
- "comics_board" - main Django configuration

## How to run

```bash
git clone https://github.com/Griz-Wold/Comics-Board.git
cd Comics-Board

python -m venv .venv
source .venv/bin/activate

pip install django
python manage.py migrate
python manage.py runserver
