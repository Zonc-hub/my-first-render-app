from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the main page, which shows the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the message from the form field named "user_message"
    message_from_user = request.form['user_message']

    # Pass the message to the result.html template
    return render_template('result.html', message=message_from_user)