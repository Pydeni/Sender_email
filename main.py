import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# Логин и пароль, кому, список адресов
EMAIL = 'fkp50/denis.osipov'
PASSWORD = '1CK4pu6NRF'
email_to = 'Sonic269@yandex.ru'
spisok_adressov = ['Sonic269@yandex.ru',"Sonic144@mail.ru"]

# Через Хромсервис
# driver = webdriver.Chrome(service=ChromeService(
#     executable_path=r'C:\Users\denis.osipov\PycharmProjects\Reestr_granits_send_email\chromedriver'))

# Через Фаерфокс
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# запускаем браузер
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Переходим на страницу авторизации почты
driver.get('https://exc50mail.fkp50.local/owa/#path=/mail')

# Выставляем тайминги задержки чтобы браузер успел прогрузить страницу
time.sleep(3)

# Теперь нам надо авторизоваться
# заполняем поле логин
emailElem = driver.find_element(By.NAME,'username')
emailElem.send_keys(EMAIL)
# emailElem.submit()
time.sleep(5)

# # заполняем поле пароль
passwordElem = driver.find_element(By.NAME,'password')
passwordElem.send_keys(PASSWORD)
passwordElem.submit()
time.sleep(3)

# Функция отправки почты
def sendder(email_to):
    # Жмем на кнопку "Создать"
    creat = driver.find_element(By.XPATH,'//button[@title="Создать новое сообщение (N)"]').click()

    # Заполняем поле кому
    to = driver.find_element(By.XPATH,"//input[@aria-label='Кому']")
    to.send_keys(email_to)
    to.submit()
    time.sleep(3)

    # Заполняем поле тема
    tema = driver.find_element(By.XPATH , "//input[@placeholder='Добавьте тему']")
    tema.send_keys('Тестовая тема')
    time.sleep(2)


    # Заполняем письмо
    telo_pisma = driver.find_element(By.XPATH, "//div[@aria-label='Тело сообщения']")
    telo_pisma.send_keys('Тут будет тема письма')
    time.sleep(2)

    # Добавляем вложение
    app = driver.find_element(By.XPATH , "//input[@type='file']").send_keys(r'C:\Users\denis.osipov\PycharmProjects\Selenium_parsing_saitov\Вложения\1.txt')
    time.sleep(2)


    # Жмем отправить
    # send = driver.find_element(By.XPATH,'//button[@title="Отправить"]').click()

# Отправляем по списку адресов
vsego_adressov = len(spisok_adressov)
otpravleno = vsego_adressov
for i in spisok_adressov:
    sendder(i)
    otpravleno -= 1

print(f"Всего  отправлено на адрессов - {vsego_adressov}")
