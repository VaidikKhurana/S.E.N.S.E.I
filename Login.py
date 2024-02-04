import subprocess
import datetime
from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import webbrowser
app = Flask(__name__)



def runsensei():
    try:
        script_path = 'Auth.py'
        subprocess.Popen(['python', script_path])  # Use Popen to run the script in background
    except Exception as e:
        log_error(e)

def log_error(error_msg):
    with open('error_log.txt', 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Error: {error_msg}\n")

# Dummy user data (replace this with a proper database)
users = {'sensei': generate_password_hash('blackcape')}

# Log file path
log_file = 'Resources\login_attempts.txt'

def log_attempt(username, password, success):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "Success" if success else "Failure"
        if status == "Success":
            runsensei()

@app.route('/')
def index():
    return render_template('dark.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Always log the attempt, whether successful or not
    log_attempt(username, password, username in users and check_password_hash(users[username], password))
    
    global query_message, response_message
    # Here you would update query_message and response_message based on your voice assistant's functionality
    # For demonstration, let's just update them with some dummy values
    query_message = "New query message from Python backend"
    
    # Return the updated messages to the frontend
    return render_template('voiceLoad.html', query=query_message)
    # For demonstration purposes, always return a success message
   
webbrowser.open("http://127.0.0.1:5000/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
