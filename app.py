from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    '''Main page handler'''
    try:
        user_id = int(request.args.get('id', 1))
    except ValueError:
        user_id = 1
    return f'<h1>Hello, user #{user_id}!</h1>'

@app.route('/health')
def health_check():
    '''Health check endpoint'''
    return 'OK'

if __name__ == '__main__':
    app.run(debug=False)
