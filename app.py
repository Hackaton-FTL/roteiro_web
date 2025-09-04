from flask import Flask, render_template, request
import db, random
from huggingface_hub import InferenceClient

app = Flask(__name__)

# Configuração do cliente da API da Hugging Face
client = InferenceClient(api_key="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")

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


def gerar_roteiro_com_ia(nome, idade, cidade, dias, orcamento, atividades):
	"""Gera roteiro usando a API da Hugging Face"""
	user_prompt = f"""
Nome: {nome}
Idade: {idade}
Local: {cidade}
Número de dias: {dias}
Orçamento: {orcamento} kz
Atividades preferidas: {atividades}

Crie um roteiro personalizado detalhado para {dias} dias de viagem com base nesses dados. 
Organize por dias e inclua atividades, custos estimados e horários sugeridos.
Mantenha-se dentro do orçamento especificado.
Formate a resposta de forma clara e organizada.
"""

	# Histórico de conversa
	conversation = [
		{"role": "system", "content": "Você é um assistente de viagens útil e criativo especializado em criar roteiros detalhados e organizados."},
		{"role": "user", "content": user_prompt},
	]

	try:
		# Chama a API da Hugging Face
		response = client.chat.completions.create(
			model="meta-llama/Llama-3.3-70B-Instruct",
			messages=conversation,
			max_tokens=30000
		)
		return response.choices[0].message.content
	except Exception as e:
		return f"Erro ao gerar roteiro: {str(e)}"



@app.route("/roteiro", methods=['POST'])
def getItineraries():
	dias = int(request.form.get("dias"))
	orcamento = float(request.form.get("orcamento"))
	nome = request.form.get("nome", "")
	idade = request.form.get("idade", "")
	cidade = request.form.get("cidade", "")
	preferencias_texto = request.form.get("preferencias_texto", "")
	
	# Gerar roteiro com IA
	roteiro_ia = gerar_roteiro_com_ia(nome, idade, cidade, dias, orcamento, preferencias_texto)
	return render_template("roteiro.html", roteiro_ia=roteiro_ia)


if __name__ == "__main__":
	app.run(debug=True, port=5001)