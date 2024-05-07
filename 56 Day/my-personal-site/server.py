#%%
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/angela")
def angela_site():
    return render_template('angela.html')

# http://127.0.0.1:5000/angela
if __name__ == "__main__":
    app.run(debug=True)