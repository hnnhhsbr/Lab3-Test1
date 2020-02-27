FROM       python:3
LABEL      maintainer="Hannah Sabri"

WORKDIR	   /app
COPY	   requirements.txt /app/
RUN	   pip install -r requirements.txt

COPY	   *.py /app/
RUN	   chmod a+x *.py

CMD	   ["./main.py"]
