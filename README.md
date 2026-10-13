# TaskUp — Task Management API

TaskUp is a backend application built with FastAPI and PostgreSQL to provide API functionality for a task management system. The project focuses on building a structured backend that can be tested, maintained, and deployed to the cloud.

## Features

- RESTful API development using FastAPI.
- PostgreSQL database integration for persistent data storage.
- Environment-based configuration for database connections and application settings.
- Interactive API documentation through Swagger UI.
- Cloud deployment preparation using Render.

*Note: Confirm that each feature is implemented in your current codebase before publishing this README.*

## Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **API Documentation:** Swagger UI / OpenAPI
- **Deployment:** Render
- **Version Control:** Git and GitHub

## Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

If `requirements.txt` is in the repository root:

```bash
pip install -r requirements.txt
```

If the file is missing, create or locate it before running this command.

### 4. Configure environment variables

Create a `.env` file in the location expected by your application and configure the required settings.

Example:

```env
DATABASE_URL=your_postgresql_connection_string
```

Use the actual environment variable name expected by your `database.py` file. Never commit real database credentials, passwords, or secret keys to GitHub.

### 5. Run the application

If your FastAPI application instance is named `app` in `main.py`, run:

```bash
uvicorn main:app --reload
```

If `main.py` is inside a subdirectory, adjust the command to match your project structure.

### 6. Explore the API

Once the server is running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

These pages let you explore and test the available API endpoints.

## Database

TaskUp uses PostgreSQL for persistent data storage. The application is configured to read its database connection from an environment variable, allowing local development and cloud deployment to use different database credentials.

Ensure that the database exists and that its connection settings are correctly configured before starting the application.

## Deployment

The project is being prepared for deployment on Render, with PostgreSQL used as the database.

The general deployment process is:

1. Push the application code to GitHub.
2. Create a PostgreSQL database on Render.
3. Configure the database connection and other required environment variables.
4. Configure the Render web service with the correct build and start commands.
5. Deploy the application and verify its API endpoints.

## Project Structure

The exact structure depends on the current repository. A typical FastAPI project may look like this:

```text
TaskUp/
├── main.py
├── database.py
├── requirements.txt
├── .env
├── .gitignore
└── ...
```

Update this section to reflect the actual files and folders in your repository.

## Security

- Store credentials in environment variables.
- Keep `.env` out of version control.
- Do not expose production database credentials.
- Configure production settings separately from local development.

## Future Improvements

Potential improvements include:

- Automated tests for API endpoints.
- Input validation and consistent error handling.
- Authentication and authorization, if not already implemented.
- Database migrations and improved deployment workflows.
- Continuous integration and deployment.

## Author

**Sharon Njambi**

Software Engineering Student | Backend Development

GitHub: [@njambisharon](https://github.com/njambisharon)

---

*This project is part of my journey in software engineering, with a focus on building reliable backend applications and learning how to deploy them to production.*
