FROM python:3.8

COPY requirements.txt .

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

RUN pip install git+https://github.com/pycord/pycord

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python", "./main.py" ]
