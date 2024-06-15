from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return 'Hello, World! DevMart is coming SooN!'
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
