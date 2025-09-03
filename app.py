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
	query = db.get_db()
	rows = query.execute("SELECT * FROM categorias").fetchall()
	categorias = [dict(row) for row in rows ]
	return render_template("index.html", categorias=categorias)

# def generateItineraries():


@app.route("/roteiro", methods=['POST'])
def getItineraries():
	dias = int(request.form.get("dias"))
	dias_em_horas = dias * 24
	orcamento = float(request.form.get("orcamento"))
	preferencias = request.form.getlist("preferencias")
	preferencias_ids = [int(pref) for pref in preferencias ]
	
	query = db.get_db()
	placeholders = ",".join("?" * len(preferencias))
	sql = f"SELECT * FROM atividades WHERE id_categoria IN ({placeholders})"
	rows = query.execute(sql, preferencias_ids).fetchall()
	actividades = [dict(row) for row in rows ]

	return render_template("roteiro.html",
		actividades=actividades,
		dias=dias,
		orcamento=orcamento,
		preferencias=preferencias,
		dias_em_horas=dias_em_horas)

if __name__ == "__main__":
	app.run(debug=True)