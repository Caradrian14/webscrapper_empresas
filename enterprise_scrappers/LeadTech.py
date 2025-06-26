from playwright.sync_api import sync_playwright
from datetime import datetime

def scrape_job_listings(empresa, url):
    programming_keywords = ['java', 'php', 'python', 'javascript', 'c++', 'c#', 'ruby', 'swift', 'go', 'rust', 'backend', 'frontend', 'symfony', 'laravel', 'react', 'angular', 'springboot', 'spring']
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()
        # Ajusta los selectores según la página
        job_listings = page.query_selector_all('.notion-page-block')

        for job in job_listings:
            # si en el titulo existen una serie de palabras clave, que se muestre
            title = job.inner_text().lower()
            if any(keyword in title for keyword in programming_keywords):
                with open('README.md', 'a', encoding='utf-8') as file:
                    # Obtener la fecha actual
                    fecha_actual = datetime.now().strftime("%Y-%m-%d")

                    # Escribir en el archivo README.md
                    file.write(f"## {fecha_actual}\n")
                    file.write(f"- Empresa: {empresa}\n")
                    file.write(f"- Enlace: {url}\n")
                    file.write(f"- Puesto: {title}\n\n")

        browser.close()