import os
import time
import random
import undetected_chromedriver as uc
from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from funciones_agentes.obtener_divisas import obtener_divisas
from utils.sanitizar import sanitizar

def iniciar_driver():
    options = uc.ChromeOptions()
    
    # 1. Configuración de Headless (Descomenta para ocultar la ventana)
    options.add_argument("--headless") 

    # 2. Evitar el error de "Keyring" y contraseñas en Linux
    options.add_argument("--password-store=basic")
    options.add_argument("--use-mock-keychain")
    
    # 3. Estabilidad en Linux
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    # 4. User-Agent Genérico (Sin versiones extremas para evitar el error de Agent)
    # Si este da error, puedes borrar esta línea y uc usará el por defecto
    options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    print("🚀 Iniciando chatbot...")
    
    try:
        # uc.Chrome se encarga de todo
        driver = uc.Chrome(options=options)
        
        # Parche de JS para limpiar la huella de Selenium
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "const newProto = navigator.__proto__; delete newProto.webdriver; navigator.__proto__ = newProto;"
        })
        return driver
    except Exception as e:
        print(f"❌ Error al iniciar el driver: {e}")
        return None

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    
    monedas = ["dolar", "euro", "dirham", "yen", "peso", "libra", "divisa", "cambio", "valor del", "cuanto cuesta"]
    if any(m in user_input for m in monedas) or " a " in user_input:
        return obtener_divisas
        
    if "precio" in user_input or "accion" in user_input:
        return obtener_precio_accion
        
    return None

# --- EJECUCIÓN ---
driver = iniciar_driver()

if driver:
    print("\n✅ ¡Chatbot listo! Escribe 'salir' para terminar.\n")
    try:
        while True:
            raw_input = input("---> ")
            if raw_input.lower() in ["salir", "exit"]: break
            
            user_input = sanitizar(raw_input)
            funcion_agente = procesar_input(user_input)
            
            if funcion_agente:
                espera = random.uniform(2, 4)
                print(f">>> Esperando {espera:.2f}s...")
                time.sleep(espera)
                
                respuesta = funcion_agente(driver, user_input)
                print(f">>> {respuesta}")
            else:
                print(">>> No entiendo esa solicitud.")
    finally:
        driver.quit()