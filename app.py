from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
	return "API + DOCKER + PosgresSQL FUNCIONANDO"

@app.route("/db")
def db():
	conn = psycopg2.connect(
	hosts="db",
	database="meubanco",
	user="posgres",
	password="postgres"
	)
	return "Conectado ao PosgresSQL !!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
