FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
<<<<<<< HEAD
=======

>>>>>>> b006571910c1276587d0dc4eec25479aa08acbd9
