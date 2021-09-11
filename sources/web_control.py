import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_driver():
    return webdriver.Chrome(r"..\assets\chromedriver.exe")


if __name__ == "__main__":
    dv = get_driver(driver_path)


