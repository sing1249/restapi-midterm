## Project setup
The app.py contains the code that helps us to retreive all the students data and modify the data using CRUD operations.
**GET** request is used to access available student data. Data can be accessed for all students or for students using specific IDs. 
**POST** request is used to enter a new student data in the existing data.
**PUT** request is used to update an existing student by using their ID.
**DELETE** request is used to delete an existing user by using their ID.  

## Environment configuration and How to run it locally.
The app is running in python and all the requirements required are in requirements.txt file. 

In order to run the service locally we will first have to switch the working directory to restapi-midterm.

Install Flask using the command - pip install Flask
And tgeb Gunicorn using command - pip install gunicorn

To install all the requirements to the local environment we will use the command:
pip install -r requirements.txt

After the dependencies are installed, we can used the command python3 app.py to run the service. 

The test-api.http file can be used to test the all the request types. 
