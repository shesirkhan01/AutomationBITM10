from selenium import webdriver


def open_webpage_online():
    driver=webdriver.Firefox(executable_path="C:\\Users\\shesi\\Downloads\\geckodriver-v0.32.0-win64\\geckodriver.exe")
    driver.get("https://google.com")
    driver.close()


open_webpage_online()