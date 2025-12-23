FROM python:3.13-slim

WORKDIR /app

RUN pip install googletrans==4.0.0-rc1 legacy-cgi

COPY Bachynskyi_Anton.py .

CMD ["python", "Bachynskyi_Anton.py"]