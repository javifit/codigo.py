from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de opciones del navegador
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

# Iniciar el navegador con las opciones
driver = webdriver.Chrome(options=chrome_options)

# Datos de inicio de sesión
usuario = "tu_usuario"
contrasenia = "tu_contraseña"

# URL del enlace a la foto
link = "https://www.facebook.com/URL_DE_LA_FOTO"

# Iniciar sesión en Facebook
driver.get("https://www.facebook.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(usuario)
driver.find_element(By.ID, "pass").send_keys(contrasenia)
driver.find_element(By.ID, "pass").send_keys(Keys.RETURN)
time.sleep(5)  # Esperar a que inicie sesión

# Ir al enlace de la foto
driver.get(link)

# Dar "me gusta" a la foto
try:
    like_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Me gusta']")))
    like_button.click()
    print("¡Me gusta dado con éxito!")
except Exception as e:
    print("No se pudo dar 'Me gusta':", str(e))

# Cerrar el navegador
driver.quit()