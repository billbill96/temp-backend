<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

<!-- Workspace-specific Copilot instructions generated from current source code -->

This project is a simple Python RESTful API built with Flask. Use these instructions as a prompt for GitHub Copilot to generate and modify code in this workspace.

Project summary
- App entry: app.py (calls mcp.create_app())
- App factory: mcp/__init__.py
  - Uses Flask, Flask-SQLAlchemy, Flask-JWT-Extended, and Flasgger (Swagger UI)
  - Config:
    - SQLALCHEMY_DATABASE_URI = sqlite:///users.db
    - SQLALCHEMY_TRACK_MODIFICATIONS = False
    - JWT_SECRET_KEY = 'your-secret-key' (override in CI/ENV)
  - Initializes db and jwt, registers blueprint(s) and runs db.create_all() inside app context
- Routes (blueprint mcp.routes):
  - GET / returns { "message": "hello world" }
  - POST /auth/register  — accepts { "email", "password" }, stores user in SQLite (hashed password)
  - POST /auth/login     — accepts { "email", "password" }, returns JWT access_token
- Swagger UI available at /apidocs
- Database file: users.db (SQLite)
- Run: python app.py (listens on 0.0.0.0:3000 by default)

Copilot guidance / constraints
- Preserve project structure: keep app factory in mcp package and a minimal app.py that calls create_app().
- Use Flask blueprints for route grouping (auth blueprint under /auth).
- Use SQLAlchemy models inside mcp.models (User model with id, email (unique), password).
- Store passwords hashed using Werkzeug generate_password_hash/check_password_hash (or bcrypt). Do not store plaintext.
- Use Flask-JWT-Extended to issue JWT access tokens on successful login.
- Ensure db.create_all() runs inside app context (do not rely on deprecated Flask lifecycle decorators).
- Keep Swagger (flasgger) docs for /auth/register and /auth/login (include request and response examples in docstrings).
- Make configuration overridable via create_app(config_overrides={...}) for tests and CI.
- Keep dependencies explicit: Flask, Flask-SQLAlchemy, Flask-JWT-Extended, flasgger, werkzeug (and bcrypt if migrating).
- Tests: provide unit tests for registration and login flows using the app factory and SQLite in-memory config (sqlite:///:memory:).
- Security: never commit real secret keys; allow override via environment or config_overrides for JWT_SECRET_KEY.
- CLI / run: app.py should remain a thin launcher that calls create_app() and app.run(host='0.0.0.0', port=3000) when __main__.

Example request/response to include in docs and tests
- POST /auth/register
  - body: { "email": "user@example.com", "password": "secret" }
  - response: 201 { "msg": "User registered successfully" }
- POST /auth/login
  - body: { "email": "user@example.com", "password": "secret" }
  - response: 200 { "access_token": "<jwt>" }

Notes
- Use sqlite:///:memory: for fast tests.
- Do not expose JWT_SECRET_KEY in the repository.
- Keep endpoints and docstrings in routes for Flasgger to pick up.
