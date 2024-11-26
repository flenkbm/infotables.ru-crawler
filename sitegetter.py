from pywebcopy import save_webpage
from re import match
from os import mkdir
from time import sleep


def get_site():
    print("\033[1m\033[31m{}\033[0m".format(
        'ВНИМАНИЕ! Для корректной работы необходимо соединение с интернетом.'))

    localpath = input(
        'Введите локальный путь вашего компьютера до данного файла ' +
        'в формате С:/a/b/ (!слеш в конце обязателен!): ')
    if (localpath[-1] != '/'):
        localpath += '/'
    localpath = localpath.replace('\\', '/')
    mkdir(localpath+'tempfiles')
    with open('tempfiles/localpath.txt', 'w') as f:
        f.write(localpath)

    siteurl = input('Введите адрес страницы с сайта infotables.ru: ')

    with open('tempfiles/sitepath.txt', 'w') as f:
        f.write(siteurl[8:])

    if (match('https://infotables.ru/', siteurl) is None):
        print("\033[1m\033[31m{}\033[0m".format(
            'ОШИБКА! Введённая ссылка указывает на неправильный сайт!'))
        raise ValueError

    pages = int(input('Введите кол-во страниц таблицы: '))
    with open('tempfiles/pages.txt', 'w') as f:
        f.write(str(pages))
    print()
    for i in range(pages):
        print('Начато скачивание страницы №'+str(i+1)+'...')
        try:
            save_webpage(
                url=siteurl+'?start='+str(i),
                project_folder=localpath + 'tempfiles/',
                project_name='site',
                bypass_robots=False,
                debug=False,
                open_in_browser=False,
                delay=None,
                threaded=False,
            )
            print('Скачивание закончено.\n')
        except TypeError:
            print('Скачивание прервано из-за ошибки.\n')
            break
        sleep(0.5)
    mkdir('tempfiles/result')


get_site()
