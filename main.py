import json
from enterprise_scrappers import scrapperA

def main():
    with open('empresas.json', 'r', encoding='utf-8') as file:
        empresas = json.load(file)

    for empresa in empresas:
        print(f"Realizando scraping para {empresa['nombre']}...")
        if empresa['nombre'] == "Empresa A":
            scrapperA.scrape_job_listings(empresa['url'])


if __name__ == "__main__":
    main()
