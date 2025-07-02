from playwright.sync_api import sync_playwright
from datetime import datetime
from .constantes import programming_keywords, file_list
def scrape_job_listings(empresa, url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()
        # Ajusta los selectores según la página
        if page.get_by_text("IT"):
            h3_elements = page.locator(
                '//h2[contains(@class, "whr-group") and contains(text(), "IT")]/following-sibling::ul[contains(@class, "whr-items")]//h3[contains(@class, "whr-title")]/a')
            #h3_elements = page.query_selector_all('h2:-text("IT") + ul > li > h3 > a')
            #page.get_by_text("Backend").click()
            for h3 in h3_elements.element_handles():
                text = h3.inner_text().lower()
                print(f'Texto de h3: {text}')
                if any(keyword in text for keyword in programming_keywords):
                    with open(file_list, 'a', encoding='utf-8') as file:
                        # Obtener la fecha actual
                        fecha_actual = datetime.now().strftime("%Y-%m-%d")

                        # Escribir en el archivo README.md
                        file.write(f"## {fecha_actual}\n")
                        file.write(f"- Empresa: {empresa}\n")
                        file.write(f"- Enlace: {url}\n")
                        file.write(f"- Puesto: {text}\n\n")

        browser.close()