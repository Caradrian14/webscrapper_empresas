from playwright.sync_api import sync_playwright
from datetime import datetime
from .constantes import programming_keywords
def scrape_job_listings(empresa, url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()

        filter_div = page.query_selector('.filters-header')
        filter_div.click()

        # Esperar a que el checkbox esté visible y luego hacer clic en él
        #page.wait_for_selector('.filter-checkbox', state='visible'
        #h3_elements = page.locator(
        #    '//div[contains(@class, "filters-content")]//ul//li[contains(@data, "whr-title")]/a')
        checkbox = page.locator('//div[contains(@class, "filters-content")]//ul//li[contains(@data-location, "remote")]/a')
        #checkbox.click()
        print(checkbox.inner_text())
        # Esperar a que se complete la solicitud AJAX y se actualice la página
        # Aquí puedes esperar a que un elemento específico esté presente o visible
        page.wait_for_selector('.ajax-result', state='visible')

        # Continuar con más interacciones o extracciones de datos
        # Por ejemplo, extraer los resultados filtrados
        results = page.query_selector_all('.ajax-result')
        for result in results:
            print(result.inner_text())

        browser.close()