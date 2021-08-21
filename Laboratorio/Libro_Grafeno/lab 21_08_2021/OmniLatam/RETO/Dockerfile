 
FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /src
WORKDIR /src
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# COPY jet/utils.py /usr/local/lib/python3.7/site-packages/jet/
# COPY jet/selects.js /usr/local/lib/python3.7/site-packages/jet/static/jet/js/src/features

EXPOSE 9000
