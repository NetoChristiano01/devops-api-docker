from flask import Flask
<<<<<<< HEAD
import psycopg2
import os
=======
>>>>>>> b006571910c1276587d0dc4eec25479aa08acbd9

app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
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
=======
    return "Projeto DevOps rodando com Docker"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> b006571910c1276587d0dc4eec25479aa08acbd9
