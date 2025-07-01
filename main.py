import json
import importlib
from enterprise_scrappers import Plexus, Wuolah  # Importa los módulos necesarios

def main():
    with open('enterprises.json', 'r', encoding='utf-8') as file:
        empresas = json.load(file)

    for empresa in empresas:
        nombre_empresa = empresa['Empresa']
        print(f"Realizando scraping para {nombre_empresa}...")

        try:
            # Intenta importar dinámicamente el módulo basado en el nombre de la empresa
            modulo = importlib.import_module(f'enterprise_scrappers.{nombre_empresa}')

            # Llama a la función scrape_job_listings del módulo importado
            modulo.scrape_job_listings(empresa['Empresa'], empresa['URL'])

        except ImportError:
            print(f"No se encontró un módulo de scraping para {nombre_empresa}.")

if __name__ == "__main__":
    main()
