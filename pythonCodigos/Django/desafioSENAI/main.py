from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

esc = int(input("Qual a versão do seu navegador(Chrome?)\n0- 87.0\n1- 88.0\n2- 89.0\n3- 90.0\nSua Escolha: "))
while 0 < esc > 3:
    esc = int(input("Digite dentro das opc: "))
num = str(87 + esc)

driver = webdriver.Chrome(executable_path=f"chromedriver_{num}.0/chromedriver.exe")
driver.get("https://aiqfome.com/RS/santa-cruz-do-sul")

try:
    stage = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    pesq = input("Que Tipo de Comida Você está Procurando? ")
    stage.send_keys(pesq)

finally:
    pass



