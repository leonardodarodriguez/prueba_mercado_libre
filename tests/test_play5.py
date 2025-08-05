import os
import time
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://www.mercadolibre.com"
SCREENSHOTS = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "screenshots"
)


@pytest.fixture(scope="session")
def driver():
    profile_dir = tempfile.mkdtemp(prefix="selenium-profile-")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--window-size=1200,800")
    opts.add_argument(f"--user-data-dir={profile_dir}")
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=opts)
    yield drv
    drv.quit()


def screenshot(driver, name):
    path = os.path.join(SCREENSHOTS, f"{name}.png")
    driver.save_screenshot(path)
    return path


def test_play5_scraper(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    screenshot(driver, "01_home")

    country = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ml-site-link#MX"))
    )
    country.click()
    time.sleep(1)
    screenshot(driver, "02_mexico")

    search = wait.until(
        EC.presence_of_element_located((By.ID, "cb1-edit"))
    )
    search.send_keys("playstation 5")
    search.submit()
    time.sleep(2)
    screenshot(driver, "03_busqueda")

    nuevo = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//span[@class='ui-search-filter-name' and normalize-space(text())='Nuevo']/ancestor::a"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", nuevo)
    nuevo.click()
    time.sleep(1)
    screenshot(driver, "04_nuevo")

    local_filter = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(text(),'Local')]/ancestor::a"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", local_filter)
    local_filter.click()
    time.sleep(1)
    screenshot(driver, "05_local")

    order_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.andes-dropdown__trigger"))
    )
    order_btn.click()
    menor = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-key='price_asc']"))
    )
    menor.click()
    time.sleep(2)
    screenshot(driver, "06_orden_menor")

    wrappers = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.ui-search-result__wrapper"))
    )[:5]

    resultados = []
    for wrap in wrappers:
        driver.execute_script("arguments[0].scrollIntoView(true);", wrap)
        title = wrap.find_element(By.CSS_SELECTOR, "a.poly-component__title").text
        price = wrap.find_element(By.CSS_SELECTOR, "span.andes-money-amount__fraction").text
        resultados.append((title, price))

    print("\n--- Productos obtenidos ---")
    for idx, (title, price) in enumerate(resultados, start=1):
        print(f"{idx}. {title} — ${price}")

    screenshot(driver, "07_resultados")
    assert len(resultados) == 5, f"Se esperaban 5 productos, pero se obtuvieron {len(resultados)}"
