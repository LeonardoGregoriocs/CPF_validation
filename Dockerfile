FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app"]

CMD ["--host=0.0.0.0"]