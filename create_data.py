from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox, FirefoxOptions
import json


class Data:
    '''
    Этот класс создан для формирования файла с ссылками на товары,
    которые находятся на странице.
    '''

    def __init__(self, URLS: list, PATH: str):
        options = FirefoxOptions()
        options.headless = True
        self.data = {'urls': []}
        self.URLS = URLS
        self.PATH = PATH

    def find_element_url(self, driver, num: int):
        '''Метод ищет на странице элемент товара и возвращает его ссылку.
            В блоке except мы пробуем отловить этот же элемент
            только с другим xpath, от чего это зависит я не понял'''
        try:
            element = driver.find_element_by_xpath(
                f'/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[{num}]/div[2]/div/a'
            ).get_attribute('href')
            
            return element

        except NoSuchElementException:
            element = driver.find_element_by_xpath(
                f'/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[{num}]/div[2]/div/a'
            ).get_attribute('href')
            
            return element
    
    def iteration_elements_in_catalog(self, driver):
        '''Этот метод проходит по всем товарам на странице, по дефолту их 34
            и внутри этого метода, мы вызываем поиск элемента,
            который вернет ссылку на товар и добавим его в нашу data'''
        amount_of_elements = 34

        for num in range(1, 1 + amount_of_elements):

            self.data['urls'].append(self.find_element_url(driver, num))

    def iteration_url_for_driver(self):
        '''В этом методе мы перебираем ссылки на страницы с товарами
            и передаем их в наш driver чтобы дальше спарсить ссылки'''
        
        for url in self.URLS:
            
            self.driver = Firefox(executable_path=self.PATH)
            self.driver.get(url)
            self.iteration_elements_in_catalog(self.driver)
            self.driver.quit()

    def dump_data(self):
        '''В это методе мы формируем файл data.txt с ссылками'''
        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile)

    def start(self):
        '''Обьявляет старт'''
        self.iteration_url_for_driver()
        self.dump_data()

