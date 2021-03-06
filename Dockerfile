FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./file_downloader .

EXPOSE 8000

RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
