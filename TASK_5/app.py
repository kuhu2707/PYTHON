from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/' , methods=["GET" , "POST"])
def index():
    greeting = None
    if request.method == "POST":
        name = request.form.get("name" , "").strip()
        if name:
            greeting = f"Hello , {name}!"
        else:
            greeting = "Hello - please enter your name."
    return render_template("index.html", greeting=greeting)
    


if __name__ == "__main__":
    app.run(debug=True)