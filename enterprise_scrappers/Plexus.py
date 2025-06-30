from playwright.sync_api import sync_playwright
from datetime import datetime
from .constantes import programming_keywords
def scrape_job_listings(empresa, url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()

# class 'jobs-list-content'
        ul_tag = page.query_selector('ul.fusion-grid.fusion-grid-3.fusion-flex-align-items-stretch')
        # Iterar sobre cada artículo
        if ul_tag:
            # Acceder a los elementos li dentro del ul
            li_elements = ul_tag.query_selector_all('li')
            # Iterar sobre los elementos li y extraer la información deseada
            for li in li_elements:
                # Aquí puedes extraer el texto o cualquier otra información que necesites
                div_title = li.inner_text()
                print(f'Texto del li: {div_title}')
        browser.close()