
# FastAPI Authentication Service

A REST API built with **FastAPI** and **PostgreSQL** for user registration and authentication. The project uses SQLAlchemy for database interaction and Pydantic for request validation and response schemas.

## Features

- User registration with full name, username, email, and password.
- Request validation using Pydantic.
- PostgreSQL database integration.
- SQLAlchemy ORM for managing user records.
- Password hashing using a dedicated security module.
- Duplicate-user validation for email and username, if enabled in the registration route.
- Interactive API documentation through Swagger UI.

> Note: Add login, JWT authentication, and other features here once they are implemented and tested.

## Tech Stack

- **Python**
- **FastAPI** — REST API framework
- **PostgreSQL** — relational database
- **SQLAlchemy** — ORM and database interaction
- **Pydantic** — request and response validation
- **Uvicorn** — ASGI server

## Project Structure

```text
authentication-service/
├── router/
│   └── auth.py
├── main.py
├── database.py
├── models.py
├── schemas.py
├── security.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Prerequisites

Before running the project, make sure you have:

- Python installed
- PostgreSQL installed and running, or access to a PostgreSQL server
- Git installed

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/authentication-service.git
cd authentication-service
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

Configure the database connection string and any other environment variables required by the application.

Example format:

```env
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME
```

Replace the placeholders with your own PostgreSQL credentials and database details.

**Never commit `.env` or real credentials to GitHub.**

### 5. Prepare the database

Make sure your PostgreSQL database exists and that the configured database user has the required permissions.

Create the required tables using the project's database setup or migration process.

> If the project does not yet use a migration tool, document the exact table-creation procedure here.

### 6. Run the application

```bash
python -m uvicorn main:app --reload
```

The development server should be available at:

- API base URL: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc


## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate a user using email and password |

### 1. Register a User

**Endpoint:** `POST /register`

Creates a new user account using their full name, username, email, and password.

**Request Body:**

```json
{
  "full_name": "Example User",
  "username": "exampleuser",
  "email": "example@example.com",
  "password": "your-test-password"
}
```

**Expected behavior:**
- Validates the submitted user information.
- Creates a new user account.
- Stores the password securely as a hash rather than plaintext.
- Rejects duplicate email addresses or usernames if duplicate checks are enabled.

### 2. Login

**Endpoint:** `POST /login`

Authenticates an existing user using their email address and password.

**Request Body:**

```json
{
  "email": "example@example.com",
  "password": "your-test-password"
}
```

**Expected behavior:**
- Validates the email and password fields.
- Checks whether the email belongs to an existing user.
- Verifies the submitted password against the stored password hash.
- Returns an appropriate response for successful or failed authentication.

The login request requires only an email and password. The full name and is not required.

## Security

- Store credentials and secrets in environment variables.
- Hash passwords before storing them in the database.
- Never return password hashes in API responses.
- Use strong, unique secrets for token signing if JWT is implemented.
- Use HTTPS and appropriate configuration before deploying to production.
- Avoid exposing sensitive database errors or credentials in logs.

## Development

The project can be tested locally using the interactive Swagger UI at `/docs`.

For development, the `--reload` option automatically restarts Uvicorn when source files change. Do not use development settings as a substitute for production deployment configuration.

## Future Improvements

Potential improvements include:

- Login endpoint and password verification
- JWT access-token generation and validation
- Protected endpoints
- Database migrations
- Automated tests
- Production deployment configuration

## License

No license has been specified yet. Add a license if you intend to permit others to use, modify, or distribute this project.
