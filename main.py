from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My WEBSITE!</h1><p>This is the home page.</p>"

if __name__ == '__main__':
    app.run(debug=True)
