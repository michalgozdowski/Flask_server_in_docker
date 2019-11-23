FROM python:3-alpine
COPY requirements.txt /app/
COPY app.py /app/
COPY templates/index.html /app/templates/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]

