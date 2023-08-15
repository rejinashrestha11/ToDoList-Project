# Project Documentation

This documentation provides an overview of the technologies used in the project and instructions on how to run the program locally.

## Technologies Used

- Programming Languages: HTML, CSS, JavaScript, Python
- Frontend Framework: React
- Backend Framework: Django (Python)
- Database: SQLite3
- Libraries: Bootstrap, Django Rest Framework, django-cors-headers, Axios, Reactstrap

## Local Setup

Follow these steps to set up and run the program locally on your machine.

### Prerequisites

- Python 3
- Node.js and npm (Node Package Manager)

### Backend Setup (Django)

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the backend directory: `cd your-repo/todoapp`
3. Create a virtual environment: `python3 -m venv todo`
4. Activate the virtual environment:
   - On macOS and Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
5. Install backend dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Run the Django development server: `python manage.py runserver`

### Frontend Setup (React)

1. Navigate to the frontend directory: `cd your-repo/frontend`
2. Install frontend dependencies: `npm install`
3. Start the React development server: `npm start`

### Accessing the Application

- Frontend: Open your web browser and go to `http://localhost:3000`
- Backend (Django Admin): `http://localhost:8000/admin/`

### Additional Configuration

- To enable CORS for local development, ensure that `django-cors-headers` is properly configured in your Django settings.


# InternProject
