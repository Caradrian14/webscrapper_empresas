from playwright.sync_api import sync_playwright
from datetime import datetime
from .constantes import programming_keywords, file_list
def scrape_job_listings(empresa, url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()

# class 'jobs-list-content'
        articles = page.query_selector_all('.jobs-list-content article')
        # Iterar sobre cada artículo
        for article in articles:
            # Extraer el texto del h4
            h4 = article.query_selector('header.header-entrie div h4')
            # Extraer el texto del ul, ignorando el svg
            ul = article.query_selector('header.header-entrie div ul')
            if ul and h4:
                h4_text = h4.inner_text()
                if any(keyword in h4_text for keyword in programming_keywords):
                    print(f'Título del Trabajo: {h4_text}')
                    # Obtener todos los elementos li dentro del ul
                    li_elements = ul.query_selector_all('li')
                    with open(file_list, 'a', encoding='utf-8') as file:
                        # Obtener la fecha actual
                        fecha_actual = datetime.now().strftime("%Y-%m-%d")
                        file.write(f"## {fecha_actual}\n")
                        file.write(f"- Empresa: {empresa}\n")
                        file.write(f"- Enlace: {url}\n")
                        li_text = ''
                        for li in li_elements:
                            li_text += li.inner_text() + " "
                        # Escribir en el archivo README.md
                        file.write(f"- Puesto: {h4_text}-{li_text}\n\n")
        browser.close()