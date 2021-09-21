# General API

##

## Requirements

- Create and activate a virtual environment.
- Run `pip install -r requirements.txt`.
- Create a `secrets.json` file with the following content:
  - `"DJANGO_SECRET_KEY": "YOUR_SECRET_KEY"`
  - `"POSTGRESQL_NAME": "YOUR_POSTGRESQL_NAME"`
  - `"POSTGRESQL_USER": "YOUR_POSTGRESQL_USER"`
  - `"POSTGRESQL_PASSWORD": "YOUR_POSTGRESQL_PASSWORD"`
  - `"POSTGRESQL_HOST": "YOUR_POSTGRESQL_HOST"`
  - `"POSTGRESQL_PORT": "YOUR_POSTGRESQL_PORT"`
  - `"EMAIL_HOST": "YOUR_EMAIL_HOST"`
  - `"EMAIL_PORT": "YOUR_EMAIL_PORT"`
  - `"EMAIL_HOST_USER": "YOUR_EMAIL_HOST_USER"`
  - `"EMAIL_HOST_PASSWORD": "YOUR_EMAIL_HOST_PASSWORD"`
  - `"EMAIL_FROM": "YOUR_EMAIL_FROM"`
  - `"EMAIL_BCC": "YOUR_EMAIL_BCC"`
- Run `python3 manage.py makemigrations`.
- Run `python3 manage.py migrate`.
- Run `python3 manage.py runserver`.

##

## Endpoints

- `https://general.abdullahalrafi.com/` || `http://127.0.0.1:8000/` - Base URL
- `api/v1/email/send` - POST - Send email
  - `api_key` - API key
  - `email` - Email address
  - `subject` - Email subject
  - `message` - Email message

##

## API Key

To get a temporary API key, contact [Abdullah Alrafi](https://abdullahalrafi.com/).

##
