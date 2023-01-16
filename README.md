# MongoDB with FastAPI

This is a sample books application using python fastAPI and mongodb.


# Application Requirements

The application needs to be with the below version

1. Python 3.8x aloing with pip 

## Quick start

```bash
#Download and install Python 3.8X along with pip

#windows:- 
https://www.python.org/ftp/python/3.8.8/python-3.8.8-amd64.exe

#MacOs
https://www.python.org/ftp/python/3.8.8/python-3.8.8-macosx10.9.pkg

#Set environment variable(windows)
#replace User from the below link with appropriate username
C:\Users\{User}\AppData\Local\Programs\Python\Python38
C:\Users\{user}\AppData\Local\Programs\Python\Python38\Scripts

#Clone the repo from github
git clone https://github.com/pradeepjey/python-fastAPI-mongo-booksApp.git

# change directory
cd python-fastAPI-mongo-booksApp/

# install the dependencies with pip
pip install -r requirements.txt

# Database connectivity
Follow the database setup given below

# start the server
uvicorn main:app --reload

```

## Database setup
This application is readily available to be connected with mongodb atlas. </br>
All configuration related to db can be found in db.py file.</br>
Replace or provide 'mongodb_user' and 'mongodb_password' from the file. Alternatively, configuration can be stored in virtual env.</br>


Now you can load http://localhost:8000/docs in your browser ... but there won't be much to see until you've inserted some data. </br>

If you have any questions or suggestions, check out the [MongoDB Community Forums](https://developer.mongodb.com/community/forums/)!
