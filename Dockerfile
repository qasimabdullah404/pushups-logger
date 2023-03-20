FROM python:3.10.10-slim

WORKDIR /src/

COPY app /src/app/

RUN apt update && apt install build-essential libpq-dev -y
RUN pip install -r app/requirements.txt

ENV FLASK_APP=app
EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0",  "--debug" ]