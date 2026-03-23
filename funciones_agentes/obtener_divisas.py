from selenium.webdriver.common.by import By
import time

def obtener_divisas(driver, user_input):
    try:
        # Ejemplo: "10 dirham a peso"
        driver.get(f"https://www.google.com/search?q={user_input}&hl=es")
        time.sleep(3)

        # Buscamos el div que contiene la respuesta rápida de conversión
        try:
            # Este selector busca el área de la calculadora de moneda
            resultado = driver.find_element(By.CSS_SELECTOR, "div.vk_ans.vk_bk.cur71a").text
            return f"Conversión final: {resultado}"
        except:
            # Selector alternativo para el número grande
            valor = driver.find_element(By.CSS_SELECTOR, "span.DFlfde.SwHCTb").text
            unidad = driver.find_element(By.CSS_SELECTOR, "span.MWvIVe").text
            return f"El valor es: 💰{valor} {unidad}🪙"

    except Exception:
        return "No se pudo extraer el cambio. Google pide verificación humana."