# TroopNet API

A modernized backend API designed to streamline unit logistics and attendance tracking. Originally conceptualized and deployed for the 38 Signal Regiment, this project serves as a rebuilt technical showcase of the original internal tool. It demonstrates practical backend architecture and provides an open-source framework for other units or teams to adapt for their own personnel management.

## Tech Stack
* **Framework:** Python / FastAPI
* **Database:** SQLite / SQLAlchemy (ORM)
* **Server:** Uvicorn

## Current Status: In Development
- [x] Environment & Dependency setup
- [x] Database Engine initialization
- [x] Core DB models (Personnel)
- [ ] CRUD API endpoints
- [ ] Dockerization

## Local Setup
To run this project locally:
1. Clone the repository.
2. Create a virtual environment: `python -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn main:app --reload`
