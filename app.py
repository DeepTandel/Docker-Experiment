from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sample():
    return "This is a Docker experiment"

if __name__ == "__main__":
    app.run(debug=True)
