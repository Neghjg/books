FROM python:3.11.8-alpine



ENV PYTHONDONTWRITEBYECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /booking

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]