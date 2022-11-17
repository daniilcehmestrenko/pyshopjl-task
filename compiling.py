from selenium.webdriver import Firefox, FirefoxOptions
import json
import time


class CompilingResult:
    '''Этот класс собирает нужные нам данные из ссылок товаров'''

    def __init__(self, PATH):
        options = FirefoxOptions()
        options.headless = True
        self.file_name = 'data.txt' #указываем имя куда сохранили ссылки
        self.PATH = PATH
        self.items = {}

    def open_read_data(self):
        '''Читаем наши ссылки из файла'''
        with open(self.file_name) as outfile:
            self.data = json.load(outfile)

    def sorting_elements(self, driver):
        '''Составляем список тех. элементов и выбираем из них нужные
            и вызываем метод добавления элемента'''
        tech_elements = driver.find_elements_by_class_name('x5l')

        for element in tech_elements:
            if 'ГГц' in element.text:
                self.append_element(element)
                break

    def append_element(self, element):
        '''Добавляем элемент в наш словарь и ведем счет'''

        if element.text not in self.items:
            self.items[element.text] = 1
        else:
            self.items[element.text] += 1



    def iteration_url_for_driver(self):
        '''Проходим по ссылкам наших товаров'''

        for url in self.data['urls']:

            self.driver = Firefox(executable_path=self.PATH)
            self.driver.get(url)
            self.sorting_elements(self.driver)
            time.sleep(1)
            self.driver.quit()

    def dump_result(self):
        '''Сортируем наш словарь по количеству и сохраняем в файл'''

        with open('result.txt', 'w') as outfile:
            for key, value in sorted(self.items.items(),
                                     key=lambda x: x[1],
                                     reverse=True):
                outfile.write(f'{key} - {value}\n')

    def start(self):
        '''Запуск'''

        self.open_read_data()
        self.iteration_url_for_driver()
        self.dump_result()

