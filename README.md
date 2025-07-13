````
# REST API with Flask and Python

A simple yet complete RESTful API built with **Flask**, **Flask‑Smorest**, **Flask‑SQLAlchemy**, **Flask‑JWT‑Extended**, and **Flask‑Migrate**—ideal for learning or bootstrapping projects. Inspired by the "REST APIs with Flask and Python" course by Jose Salvatierra :contentReference[oaicite:1]{index=1}.

---

## 🚀 Features

- Structured endpoints using Blueprints and Flask‑Smorest  
- Data storage powered by SQLAlchemy (with support for SQLite, PostgreSQL, etc.)  
- User authentication via JWT (access & refresh tokens, token revocation)  
- Database migrations using Flask‑Migrate/Alembic  
- Optional Docker support (image & `docker-compose`)  
- Easily extendable: add background jobs, email‑sending, task queues, etc.

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+  
- [pipenv](https://pipenv.pypa.io/) or `virtualenv` + `pip`  
- Optional: Docker & Docker Compose

### Setup locally

```bash
git clone https://github.com/Delvin233/REST-API-with-Flask-and-Python.git
cd REST-API-with-Flask-and-Python

# Create & activate virtual environment
pipenv shell
# or
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db upgrade

# Run the app
flask run
````

Flask server will start at `http://127.0.0.1:5000/`.

---

## 🔧 Configuration

| Environment Variable             | Default             | Description                             |
| -------------------------------- | ------------------- | --------------------------------------- |
| `FLASK_ENV`                      | `development`       | Flask environment mode                  |
| `DATABASE_URL`                   | `sqlite:///data.db` | Database URI (PostgreSQL, SQLite, etc.) |
| `JWT_SECRET_KEY`                 | *(random)*          | Secret key for signing JWTs             |
| `FLASK_APP`                      | `app.py`            | Flask entrypoint                        |
| `SQLALCHEMY_TRACK_MODIFICATIONS` | `False`             | Disable SQLAlchemy event notifications  |

You can set these in a `.env` file and load with `python-dotenv`.

---

## 🧭 API Endpoints

### Auth

* `POST /register` – Create a new user
* `POST /login` – Authenticate user, return access + refresh tokens
* `POST /refresh` – Generate new access token from refresh token
* `POST /logout` – Revoke access or refresh token

### Resources (example: items & stores)

* `GET /stores` – List all stores

* `GET /stores/<id>` – Retrieve single store

* `POST /stores` – Create a new store

* `DELETE /stores/<id>` – Delete a store

* `GET /stores/<id>/items` – List items in a store

* `GET /items` – List all items

* `GET /items/<id>` – Retrieve single item

* `POST /items` – Create an item (requires store ID)

* `PUT /items/<id>` – Update item data

* `DELETE /items/<id>` – Delete an item

All endpoints return JSON and appropriate status codes (200, 201, 401, 404, 500).

---
