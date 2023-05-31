FROM python:3

ENV PYTHONUNBUFFER=1

WORKDIR /CODE

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .


# EXPOSE 8000

# CMD ["python3 manage.py runserver"]


