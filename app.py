from flask import Flask, render_template, request
import random
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configuração do cliente da API da Hugging Face
api_key = os.getenv('HUGGINGFACE_API_KEY')
if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY environment variable is required")

client = InferenceClient(api_key=api_key)

@app.route("/", methods=['GET'])
def home():
	return render_template("home.html")


@app.route("/generator", methods=['GET'])
def generator():
	return render_template("generator.html")


@app.route("/about", methods=['GET'])
def about():
	return render_template("about.html")


def gerar_roteiro_com_ia(nome, idades, cidade, dias, horas_diarias, orcamento, tamanho_grupo, atividades):
	"""Gera roteiro usando a API da Hugging Face"""
	user_prompt = f"""
Nome: {nome}
Idades do grupo: {idades}
Local de destino: {cidade}
Número de dias: {dias}
Horas diárias de atividades: {horas_diarias}
Tamanho do grupo: {tamanho_grupo} pessoa(s)
Orçamento total: {orcamento} Kz (Kwanza angolano)
Atividades preferidas: {atividades}

Crie um roteiro personalizado detalhado para {dias} dias de viagem em {cidade} com base nesses dados. 

INSTRUÇÕES ESPECÍFICAS:
- Organize por dias de forma clara e estruturada
- Inclua atividades, custos estimados em Kwanza (Kz) e horários sugeridos
- Mantenha-se dentro do orçamento especificado de {orcamento} Kz
- Considere {horas_diarias} horas de atividades por dia
- Adapte as atividades para um grupo de {tamanho_grupo} pessoa(s)
- Priorize experiências autênticas e sustentáveis de Angola
- Inclua dicas práticas e informações culturais relevantes
- Formate a resposta de forma clara, organizada e fácil de ler
- Use emojis para tornar o roteiro mais visual e atrativo

Se o orçamento for limitado, sugira alternativas econômicas. Se for generoso, inclua experiências premium.
"""

	# Histórico de conversa
	conversation = [
		{"role": "system", "content": "Você é um especialista em turismo angolano e assistente de viagens especializado em criar roteiros detalhados, autênticos e sustentáveis para Angola. Você conhece profundamente a cultura, geografia, custos locais e experiências únicas que Angola oferece. Sempre promova o turismo responsável e experiências que beneficiem as comunidades locais."},
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
		return f"Erro ao gerar roteiro: {str(e)}\n\nTente novamente em alguns instantes. Se o problema persistir, verifique sua conexão com a internet."



@app.route("/roteiro", methods=['POST'])
def getItineraries():
	# Campos básicos
	dias = int(request.form.get("dias"))
	orcamento = float(request.form.get("orcamento"))
	nome = request.form.get("nome", "")
	cidade = request.form.get("cidade", "")
	preferencias_texto = request.form.get("preferencias_texto", "")
	
	# Novos campos
	horas_diarias = int(request.form.get("horas_diarias", 8))
	tamanho_grupo = int(request.form.get("tamanho_grupo", 1))
	idades = request.form.get("idades", "")
	
	# Gerar roteiro com IA
	roteiro_ia = gerar_roteiro_com_ia(nome, idades, cidade, dias, horas_diarias, orcamento, tamanho_grupo, preferencias_texto)
	return render_template("roteiro.html", roteiro_ia=roteiro_ia)


if __name__ == "__main__":
	app.run(debug=True, port=5001)