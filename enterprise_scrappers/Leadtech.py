from playwright.sync_api import sync_playwright
from datetime import datetime
from .constantes import programming_keywords
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
                text = h3.inner_text()
                print(f'Texto de h3: {text}')

        browser.close()