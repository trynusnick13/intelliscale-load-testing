FROM python:3.10

WORKDIR /server

COPY . /server


RUN pip install --no-cache-dir --upgrade poetry
RUN poetry install

CMD ["poetry", "run", "python3", "main.py", "run-stress-load-campaign"]
