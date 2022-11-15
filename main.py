from create_data import Data
from compiling import CompilingResult
from config import PATH, URLS

def main(path, urls):
    d = Data(urls, path)
    c = CompilingResult(path)
    d.start()
    c.start()


if __name__ == '__main__':
    main(PATH, URLS)
