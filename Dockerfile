FROM python:3.8-slim

COPY Pipfile Pipfile.lock main.py /app/

WORKDIR /app

RUN pip install pipenv \
    && pipenv install --system --deploy \
    && pip uninstall -y pipenv
	
WORKDIR /data

ENTRYPOINT [ "python", "/app/main.py" ]
