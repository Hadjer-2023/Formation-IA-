from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message = "Hello World!")

if __name__ == "__main__":
    app.run()

    from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message_bienvenue="Bienvenue sur la page d'accueil !")

@app.route("/next")
def suite():
    return render_template("page_suivante.html")

if __name__ == "__main__":
    app.run()
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    processed_text = text.upper()
    return render_template("bienvenue.html" , message = processed_text )

if __name__ == '__main__':
    app.run()
