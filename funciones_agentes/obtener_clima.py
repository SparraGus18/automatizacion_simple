from selenium.webdriver.common.by import By
import time

def obtener_clima(driver, user_input):
    
    iconos_clima = {
        "soleado": "☀️",
        "despejado": "🌙" if "noche" in user_input else "☀️",
        "nublado": "☁️",
        "nubes": "⛅",
        "lluvia": "🌧️",
        "llovizna": "🌦️",
        "tormenta": "⛈️",
        "nieve": "❄️",
        "niebla": "🌫️",
        "viento": "🌬️",
        "cubierto": "☁️"
    }

    try:
        driver.get(f"https://www.google.com/search?q={user_input}&hl=es")
        time.sleep(3)

        # Extraemos los datos básicos
        temp = driver.find_element(By.ID, "wob_tm").text
        condicion = driver.find_element(By.ID, "wob_dc").text.lower() # Pasamos a minúsculas
        lugar = driver.find_element(By.ID, "wob_loc").text

        
        emoji = "🌍"
        for clave, simbolo in iconos_clima.items():
            if clave in condicion:
                emoji = simbolo
                break

        return f"{emoji} En {lugar}, el clima está {condicion} con {temp}°C."

    except Exception:
        return "❌ No pude obtener el clima. Google detectó comportamiento de bot."