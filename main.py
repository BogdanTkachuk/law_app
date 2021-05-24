import requests
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
import sys
from window import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UiMainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


Host = 'https://zakon.rada.gov.ua/'
URL_laws = 'https://zakon.rada.gov.ua/laws/main/tt1001'
URLS_CMU = 'https://zakon.rada.gov.ua/laws/main/tt2002'
URLS_CMU2 = 'https://zakon.rada.gov.ua/laws/main/tt2006'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
              'signed-exchange;v=b3;q=0.9',
    'userAgent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


# Функція, що отримує веб сторінку та дозвільні атребути
def get_html(url, params=''):
    r = requests.get(url, headers=headers, params=params)
    return r.text


# отримуємо посилання та усі сторінки
def get_all_links(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('a', class_='page-link',
                           title='в кінець').get('href')
    page_links_list = [url]
    counter = 1
    for page in range(int(pagination[-3:]) - 1):
        page_links_list.append(url + '/page' + str(counter))
        counter += 1
    return page_links_list


def get_page_data(html):  # визначаємо елемети, що мають спарситись
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='doc')
    lar_list = []
    for item in items:
        lar_list.append(
            [
                item.find('a').get_text(strip=True),
                item.find('a').get('href'),
                item.find('a').get('alt'),
                'від ' + item.find('span').get_text(),
            ]
        )
    return lar_list


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    return data


# збір фнформація та фільтрація відповідно до запиту
def _filter(search, page_links_list):
    lar = ThreadPool(15).imap_unordered(make_all, page_links_list)
    search_list = []
    for i in lar:
        for item in i:
            if search.lower() in str(item).lower():
                search_list.extend(item)
                search_list.extend('\n')
    if search_list:
        return '\n'.join(map(str, search_list))
    else:
        return 'Нічого не знайдено, cпробуйте ще раз.'


def button():
    ui.plainTextEdit.clear()
    search = ui.lineEdit.text()
    ui.lineEdit.clear()
    page_links_list = get_all_links(get_html(URL_laws), URL_laws)
    ui.plainTextEdit.appendPlainText(_filter(search, page_links_list))


def button_2():
    ui.plainTextEdit.clear()
    search = ui.lineEdit.text()
    ui.lineEdit.clear()
    page_links_list = get_all_links(get_html(URLS_CMU), URLS_CMU)
    ui.plainTextEdit.appendPlainText(_filter(search, page_links_list))


def button_3():
    ui.plainTextEdit.clear()
    search = ui.lineEdit.text()
    ui.lineEdit.clear()
    page_links_list = get_all_links(get_html(URLS_CMU2), URLS_CMU2)
    ui.plainTextEdit.appendPlainText(_filter(search, page_links_list))


def main():
    ui.pushButton.clicked.connect(button)
    ui.pushButton_2.clicked.connect(button_2)
    ui.pushButton_3.clicked.connect(button_3)


if __name__ == '__main__':
    main()
    sys.exit(app.exec_())

