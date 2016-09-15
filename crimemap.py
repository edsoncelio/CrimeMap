# -*- coding: utf-8 -*- 

from flask import Flask
from flask import render_template
from flask import request
import json,ast
import pymongo

##WARNING :
'''
falta implementar a busca dos dados do banco (MongoDB) para a montagem dos pontos salvos, possiveis problemas:
*codificação
'''

#conexao ao MongoDB    obs: recomenda-se criar uma classe para a conexao
conectar = pymongo.MongoClient()
db = conectar.NomeBD.nomecolecao

		

app = Flask(__name__)

@app.route("/")
def home():
	#string em formato JSON que será usada para exemplo, a mesma ficará marcada no mapa, e fará a função de ponto salvo
	dados = [{"latitude":"","longitude":"","date":"2016","categoria":"assalto","descricao":"assalto a map armada"}]	
	return render_template("map.html",crimes=dados)

		
			
@app.route("/adicionarcrime",methods=["POST"])
def addcrime():
	# requests para receber os dados do FORM html
	category = request.form.get("category")
	date = request.form.get("date")
	latitude = float(request.form.get("latitude"))
	longitude = float(request.form.get("longitude"))
	description = request.form.get("description")
	dados = {"latitude":latitude,"longitude":longitude,"date":date,"categoria":category,"descricao":description} #montagem do template para o banco de dados
	db.insert(dados)     #insercao dos dados inseridos no FORM no banco de dados definido na conexao com o MongoDB
	return home()



if __name__=="__main__":
	app.run(port=5000, debug=True)		
		







