# TaskForce - Professional Project Manager

TaskForce is a modern, responsive, and robust Web Application built with the Django framework. It is designed to help teams and managers to organize their workflow, track projects, assign tasks, and manage team members—all within an elegant, SaaS-like user interface.

## Features

* **Project Management:** Create, read, update, and delete (CRUD) projects with detailed descriptions and deadlines.
* **Task Tracking:** Break down projects into actionable tasks. Assign team members to specific tasks and track their progress (To Do, In Progress, Done).
* **Team Management (Workers):** Add, edit, and remove team members. View their assigned roles and currently active projects.
* **Modern UI/UX:** A clean, spacious, and highly readable interface built with Bootstrap 5 and custom CSS for a premium user experience.

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
* **Database:** PostgreSQL

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Installation

1. **Clone the repository (if using Git):**
   git clone https://github.com/sibelyazadzhieva/taskforce_django_project.git 
   cd taskforce

2. **Create and activate a virtual environment:**
   python -m venv venv
   
### On Windows:
   venv\Scripts\activate
### On macOS/Linux:
   source venv/bin/activate


3. **Install the dependencies:**
   pip install -r requirements.txt

4. **Apply database migrations:**
   python manage.py migrate

5. **Create a superuser (Admin):**
   python manage.py createsuperuser

6. **Run the development server:**
   python manage.py runserver

7. **Access the application:**
   Open your web browser and go to http://127.0.0.1:8000/