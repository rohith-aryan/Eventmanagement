# Event Management System

## Instructions to Run Code

### Prerequisites
- Python (version 3.6 or higher)
- Django framework
- Django REST Framework
- Requests library (for making HTTP requests to external APIs)

### Setup
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/Eventmanagement.git
   ```

2. Navigate to the project directory:
   ```
   cd Eventmanagement
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source env/bin/activate
     ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Migrate the database:
   ```
   python manage.py migrate
   ```

7. Load CSV data into the database:
   ```
   python manage.py populate_events.py
   ```

### Running the Server
1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Access the API endpoints:
   - Data Creation API: [http://127.0.0.1:8000/event/](http://127.0.0.1:8000/event/)
   - Event Finder API: [http://127.0.0.1:8000/events/find/](http://127.0.0.1:8000/events/find/)

### API Documentation
- Detailed information about how the API endpoints work can be found in the APIdocumentation file.



