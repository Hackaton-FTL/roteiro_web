from flask import Flask, render_template, request
import db, random

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


def generateItineraries(orcamento, actividades, dias):
	roteiro = []
	orcamento_restante = orcamento
	horas_por_dia = 8
	atividades_filtradas = [
        a for a in actividades
    ]
	random.shuffle(atividades_filtradas)

	for dia in range(1, dias + 1):
		horas_disponiveis = horas_por_dia
		actividades_dia = []
		for atividade in atividades_filtradas:
			duracao = atividade['duracao_horas']
			custo = atividade['custo']

			if (custo <= orcamento_restante and duracao <= horas_disponiveis ):
				orcamento_restante -= custo
				horas_disponiveis -= duracao
				actividades_dia.append(atividade)
				atividades_filtradas.remove(atividade)
		roteiro.append({"dia": dia, "atividade": actividades_dia})

	return roteiro



@app.route("/roteiro", methods=['POST'])
def getItineraries():
	dias = int(request.form.get("dias"))
	orcamento = float(request.form.get("orcamento"))
	preferencias = request.form.getlist("preferencias")
	preferencias_ids = [int(pref) for pref in preferencias ]
	
	query = db.get_db()
	if preferencias_ids:
		placeholders = ",".join("?" * len(preferencias))
		sql = f"SELECT * FROM atividades WHERE id_categoria IN ({placeholders})"
		rows = query.execute(sql, preferencias_ids).fetchall()
	else:
		rows = query.execute("SELECT * FROM atividades").fetchall()

	actividades = [dict(row) for row in rows ]
	roteiro = generateItineraries(orcamento, actividades, dias)

	return render_template("roteiro.html", roteiro=roteiro)


if __name__ == "__main__":
	app.run(debug=True)