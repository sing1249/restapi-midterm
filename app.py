# Import necessary modules from Flask
# Flask: the core framework for the web app
# jsonify: to convert Python dictionaries to JSON responses
# request: to access incoming request data (e.g., POST data)
# abort: to handle errors and send error status codes
from flask import Flask, jsonify, request, abort

# Initialize the Flask app
app = Flask(__name__)

# In-memory "database" students
# This list holds a set of student dictionaries. 

students = [
    {"id": 1, "name": "Jack", "grade": 90, "email": "jack@abc.com"},
    {"id": 2, "name": "Peter", "grade": 80, "email": "peter@abc.com"},
    {"id": 3, "name": "Rob", "grade": 70, "email": "rob@abc.com"},
]

# Define route to handle requests to the root URL ('/')
@app.route('/')
def index():
    return "Welcome to Flask REST API Demo! Try accessing /students to see all students."

# Health check route (GET)
# This endpoint returns a 200 OK status and a JSON response to confirm that the service is running.
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200  # Return HTTP status 200 OK

# Route to retrieve all students (GET request)
# When the client sends a GET request to /students, this function will return a JSON list of all students.
# The @ symbol in Python represents a decorator. 
# In this case, @app.route is a Flask route decorator.
# It is used to map a specific URL (route) to a function in your Flask application.
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200  # 200 is the HTTP status code for 'OK'

# Route to retrieve a single student by their ID (GET request)
# When the client sends a GET request to /student/<id>, this function will return tstudent with the specified ID.
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Using a list comprehension to find the student by ID
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)  # If the student is not found, return a 404 error (Not Found)
    return jsonify(student), 200  # Return the student as a JSON object with a 200 status code (OK)

# Route to create a new student (POST request)
# When the client sends a POST request to /students with student data, this function will add the new student to the list.
@app.route('/students', methods=['POST'])
def create_student():
    # If the request body is not in JSON format or if the 'name' field is missing, return a 400 error (Bad Request)
    if not request.json or not 'name' in request.json:
        abort(400)
    
    # Create a new student dictionary. Assign the next available ID by incrementing the highest current ID.
    # If no students exist, the new ID will be 1.
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': request.json['name'],  # The name is provided in the POST request body
        'grade': request.json.get('grade', 0),  # The grade is optional; default is 0 if not provided
        'email': request.json.get('email', "") #Leaves the email string empty if no email provided.    
    }

    # Add the new student to the students list
    students.append(new_student)
    return jsonify(new_student), 201  # 201 is the HTTP status code for 'Created'

# Route to update an existing student (PUT request)
# When the client sends a PUT request to /students/<id> with updated student data, this function will update the student.
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    # Find the student by their ID
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)  # If the student is not found, return a 404 error (Not Found)
    
    # If the request body is missing or not in JSON format, return a 400 error (Bad Request)
    if not request.json:
        abort(400)
    
    # Update the student's data based on the request body
    # If a field is not provided in the request, keep the existing value
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    return jsonify(student), 200  # Return the updatstudent data with a 200 status code (OK)

# Route to delete a student (DELETE request)
# When the client sends a DELETE request to /students/<id>, this function will remove the student with that ID.
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students  # Reference the global students list
    # Rebuild the students list, excluding the student with the specified ID
    students = [student for student in students if student['id'] != student_id]
    return '', 204  # 204 is the HTTP status code for 'No Content', indicating the deletion was successful

# Entry point for running the Flask app
# The app will run on host 0.0.0.0 (accessible on all network interfaces) and port 8000.
# Debug mode is disabled (set to False).
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)