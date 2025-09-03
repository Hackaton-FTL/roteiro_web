from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/roteiro", methods=["POST"])
def generateItineraries():
	dias = request.form.get("dias")
	orcamento = request.form.get("orcamento")
	preferencias = request.form.getlist("preferencias")
	return f"{dias} {orcamento} {preferencias}"

if __name__ == "__main__":
	app.run(debug=True)