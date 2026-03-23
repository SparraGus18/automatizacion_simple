from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_precio_accion(driver, user_input):
    empresa = user_input.replace("precio", "").replace("accion", "").replace("de", "").strip()
    try:
        
        driver.get(f"https://www.google.com/search?q=stock+price+{empresa}+nasdaq&hl=en")
        time.sleep(3)

        # Intentamos detectar si hay un botón de cookies y lo saltamos
        try:
            botones = driver.find_elements(By.TAG_SCHEMA, "button")
            for b in botones:
                if "Accept" in b.text or "Aceptar" in b.text:
                    b.click()
                    time.sleep(1)
        except: pass

       
        wait = WebDriverWait(driver, 5)
        precio_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[jsname='L3mUVe']")))
        precio = precio_el.text
        
        return f"La acción de {empresa.upper()} está en 📈${precio} USD.📉"

    except Exception:
        
        titulo = driver.title
        if "$" in titulo or "USD" in titulo:
             return f"Dato desde el título: {titulo}"
        return f"Google bloqueó la lectura para '{empresa}'. Intenta sin headless una vez."