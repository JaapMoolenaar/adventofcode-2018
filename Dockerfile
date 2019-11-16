FROM python:3.7-alpine

COPY start.sh /start.sh

WORKDIR /src
COPY src /src

ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

RUN apk add --no-cache bash gcc musl-dev linux-headers
RUN pip install -r /src/requirements.txt

ENTRYPOINT ["/start.sh"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app"]
