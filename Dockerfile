# Basis-Image auswählen
FROM python:3.10-slim

# Arbeitsverzeichnis erstellen und setzen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY . .

# Port freigeben
EXPOSE 5000

# Startbefehl definieren
CMD ["python", "app.py"]
