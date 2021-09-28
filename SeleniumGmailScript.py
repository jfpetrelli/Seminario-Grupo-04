from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Firefox(executable_path="PATH")  # Ingresar path de webdriver
driver.maximize_window()
driver.get("http://www.gmail.com")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierId")))

email = driver.find_element_by_id("identifierId")
email.clear()
email.send_keys("mail")  #Reemplazar por su mail
email.send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("password")  #Reemplazar por su password
password.send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.title_contains("Recibido"))

boton_redactar = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
boton_redactar.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "to")))

receptor_mail = driver.find_element_by_name("to")
receptor_mail.send_keys("destinatario") #Ingresar direccion de destino

asunto_mail = driver.find_element_by_name("subjectbox")
asunto_mail.clear()
asunto_mail.send_keys("Un asunto")
asunto_mail.send_keys(Keys.TAB, "Un mensaje")
asunto_mail.send_keys(Keys.TAB, Keys.TAB, Keys.RETURN)

sleep(5)
#driver.implicitly_wait(5)
mensaje = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[4]/div[1]/div/div[3]/div/div/div[2]/span/span[1]")
print(mensaje.text)

driver.close()