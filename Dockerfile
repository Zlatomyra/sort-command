FROM python:3.13-slim
WORKDIR /app
COPY sort.py /app/sort.py
RUN pip install --no-cache-dir click
ENTRYPOINT ["python", "sort.py"]
