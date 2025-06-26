import json
from enterprise_scrappers import Wuolah
from enterprise_scrappers import Leadtech

def main():
    with open('enterprises.json', 'r', encoding='utf-8') as file:
        empresas = json.load(file)

    for empresa in empresas:
        if empresa['Empresa'] == "Leadtech":
            print(f"Realizando scraping para {empresa['Empresa']}...")
            Leadtech.scrape_job_listings(empresa['Empresa'], empresa['URL'])


if __name__ == "__main__":
    main()
