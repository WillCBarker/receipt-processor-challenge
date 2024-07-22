FROM python:3.11-slim

WORKDIR /receipt-processor-challenge/

COPY . /receipt-processor-challenge/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /receipt-processor-challenge/receipt_processor/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

