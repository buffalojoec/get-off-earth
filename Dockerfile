FROM tiangolo/uwsgi-nginx-flask

ENV FLASK_APP="get_off_earth"
ENV FLASK_ENV="development"

COPY . .
RUN pip install -e .

EXPOSE 5000
ENTRYPOINT flask run --host=0.0.0.0