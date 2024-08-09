FROM python:slim
WORKDIR /app/package
COPY . /app/package
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "hi.py"]
