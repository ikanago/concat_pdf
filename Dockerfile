FROM python:3.8-slim

WORKDIR /app

COPY Pipfile Pipfile.lock main.py ./

RUN pip install pipenv \
    && pipenv install --system --deploy \
    && pip uninstall -y pipenv

ENTRYPOINT [ "python", "main.py" ]
