FROM python:3.12-alpine

WORKDIR .

RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . . 

CMD ["python", "parser_1.py"]