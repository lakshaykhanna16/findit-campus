# FindIT — Campus Lost & Found

FindIT is a campus lost-and-found web application designed to help students report lost or found items and browse reports submitted by other students.

## Features

- Submit reports for lost and found items.
- Store reports in an SQLite database using Flask-SQLAlchemy.
- Browse submitted reports dynamically.
- Display item name, category, status, location, date, and description.
- Show success notifications after submitting a report.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **ORM:** Flask-SQLAlchemy
- **Frontend:** HTML, CSS, Jinja Templates
- **JavaScript:** Planned for search and filtering
- **Deployment:** Vercel

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lakshaykhanna16/findit-campus.git
cd findit-campus
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

The application creates the SQLite database and required tables automatically when it starts.

## Project Structure

```text
findit-campus/
├── app.py
├── extensions.py
├── models.py
├── requirements.txt
├── instance/
│   └── items.db
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── browse-items.html
│   └── report-items.html
└── static/
    ├── css/
    ├── js/
    └── images/
```

## Project Status

The following functionality has been implemented:

- Flask application setup and routing.
- Jinja template inheritance.
- SQLAlchemy database integration.
- Item model and database operations.
- Lost/found report submission.
- Dynamic item browsing.

### Upcoming Improvements

- Search and filter functionality.
- Individual item image uploads.
- Improved backend validation.
- Production-ready persistent database hosting.
- Further testing and deployment improvements.

**Note:** SQLite is currently used for local development. A persistent hosted database will be required for reliable production deployment on a serverless platform.

## Team

- **Project Lead:** Lakshay Khanna
- **Team Member:** Manisha
