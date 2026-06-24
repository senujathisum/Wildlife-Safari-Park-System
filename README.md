# Yala Wild Safari Park System

Welcome to the management system for the Yala Wild Safari Park! This Django-based web application allows you to manage habitats, animals, tour guides, and visitor bookings, along with customizable site settings (like the logo).

## Features

- **Habitats & Animals**: Keep track of the various zones and the animals living there.
- **Tour Guides**: Manage your staff, their shifts, and their assigned zones.
- **Bookings**: Schedule and track visitor bookings with different pricing tiers.
- **Gallery**: Showcase the park with a dedicated gallery.
- **Site Settings**: Easily manage the application's logo straight from the admin dashboard.

## How to Start the Web System

To run the application locally, you will need to start the Django development server. Use the following command in your terminal from the root directory of the project:

```bash
.\venv\Scripts\python.exe manage.py runserver
```

Once the server is running, you can access the website in your browser at:
`http://127.0.0.1:8000/`

## Accessing the Admin Panel

You can log into the Django admin dashboard to manage the database records (including modifying the site logo):
1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials.

*(If you don't have a superuser yet, you can create one by running: `.\venv\Scripts\python.exe manage.py createsuperuser`)*
