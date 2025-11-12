"""Simple Flask application for CI/CD demonstration."""
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    """Handle main page request.
    
    Returns:
        str: HTML greeting message
    """
    try:
        user_id = int(request.args.get('id', 1))
    except ValueError:
        user_id = 1
    return f'<h1>Hello, user #{user_id}!</h1>'


if __name__ == '__main__':
    app.run(debug=False)
