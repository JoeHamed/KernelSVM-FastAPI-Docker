FROM python:3.11

WORKDIR /code

COPY /app/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

RUN pip install python-multipart

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.Server:app", "--host", "0.0.0.0", "--port", "8000"]
