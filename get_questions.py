import os
from requests_html import HTMLSession


def write_question_to_file(day):
    with open('sessionid.txt', 'r') as session_id:
        session_id = session_id.read()
    url = 'https://adventofcode.com/2020/day/' + day
    cookies = dict(
        session=session_id)

    session = HTMLSession()
    response = session.get(url, cookies=cookies)

    page = ('<!DOCTYPE html>'
            '<html lang="en">'
            '    <head>'
            '        <meta charset="utf-8">'
            '        <title>Advent Of Code day ' + day + '</title>'
                                                         '    </head>'
                                                         '    <body>'
                                                         '        <a href="' + url + '">Advent Of Code day ' + day + '</a>'
                                                                                                                     '        <!-- page content -->'
                                                                                                                     '    </body>'
                                                                                                                     '</html>')

    page_content = ''
    for element in response.html.find('.day-desc'):
        page_content += element.html

    page = page.replace('<!-- page content -->', page_content)

    with open('./Day' + day + '/question.html', 'w') as file:
        file.write(page)


if __name__ == '__main__':
    day = str(len([name for name in os.listdir() if name[0:3] == 'Day']))
    write_question_to_file(day)
