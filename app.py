from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
	db.close_db(exception)

@app.route("/createdb", methods=['GET'])
def initdb():
	db.init_db()
	return "Banco de dados criado"

@app.route("/", methods=['GET'])
def home():
	return render_template("index.html")

@app.route("/roteiro", methods=['POST'])
def generateItineraries():
	dias = request.form.get("dias")
	orcamento = request.form.get("orcamento")
	preferencias = request.form.getlist("preferencias")
	return render_template("roteiro.html")

if __name__ == "__main__":
	app.run(debug=True)