# Pulled March 22, 2023
FROM --platform=linux/amd64 python:3.8@sha256:a07637d351af5829bbd650735a5beed77fb467a124388191ac3fa5b8812e67c5
RUN pip install --upgrade pip && pip install gunicorn==20.1.0
WORKDIR /srv
COPY gunicorn_conf.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY *.py ./
COPY templates ./templates
ENV PYTHONUNBUFFERED=1
ARG VERSION
RUN if [ -z "$VERSION" ]; then echo "$(date +%s)" > /srv/VERSION.txt; else echo "${VERSION}" > /srv/VERSION.txt; fi
ENTRYPOINT ["gunicorn", "-c", "gunicorn_conf.py", "app:app"]
