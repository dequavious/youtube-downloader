# syntax=docker/dockerfile:1

FROM python:3.10 as compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /yt-dl-docker

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM python:3.10 as runner
WORKDIR /yt-dl-docker
COPY --from=compiler /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
COPY . .
CMD ["python3", "wsgi.py", "13882"]