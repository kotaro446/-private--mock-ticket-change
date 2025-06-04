FROM python:3.13.0

RUN apt update \
  && apt install --no-install-recommends -y lsb-release tzdata \
  && apt clean \
  && pip install -U pip \
  && pip install pipenv

RUN mkdir -p /usr/src/app/app
WORKDIR /usr/src/app/app/

COPY ./app/Pipfile* ./
RUN pipenv sync
COPY ./app/.* ./app/src ./

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/app/src"
ENTRYPOINT ["pipenv", "run"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app","--timeout", "30"]
