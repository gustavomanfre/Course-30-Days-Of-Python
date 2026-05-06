import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = {}

# Buscamos todas las tablas
tables = soup.find_all("table")

for idx, table in enumerate(tables, start=1):
    rows = table.find_all("tr")
    table_data = []
    for tr in rows:
        cols = tr.find_all(["th", "td"])
        values = [col.get_text(strip=True) for col in cols]
        table_data.append(values)

    data[f"table_{idx}"] = table_data

# Guardar como JSON
with open("bu_facts_stats.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Guardado: bu_facts_stats.json")

#_______________________________________________________________

import pandas as pd
import json

url = "https://archive.ics.uci.edu/ml/datasets.php"

# pandas puede leer directamente tablas HTML
tables = pd.read_html(url)

# La tabla principal suele estar en tables[0]
df = tables[0]

# Convertir a JSON
data = df.to_dict(orient="records")

with open("uci_datasets.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Guardado: uci_datasets.json")
#_______________________________________________________________

import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# La tabla de presidentes es la primera con class "wikitable"
table = soup.find("table", {"class": "wikitable"})

presidents = []

rows = table.find_all("tr")

for tr in rows[1:]:  # saltamos el encabezado
    cols = tr.find_all(["th","td"])
    cols_text = [c.get_text(strip=True) for c in cols]

    # Esperamos que tenga al menos 6 columnas
    if len(cols_text) >= 6:
        president = {
            "number": cols_text[0],
            "name": cols_text[1],
            "party": cols_text[2],
            "term_start": cols_text[3],
            "term_end": cols_text[4],
            "vice_president": cols_text[5]
        }
        presidents.append(president)

with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4, ensure_ascii=False)

print("Guardado: us_presidents.json")
