FROM python:3.11-slim

WORKDIR /app

COPY sistema_faculdade.py .

CMD ["python", "sistema_faculdade.py"]
