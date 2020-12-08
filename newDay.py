import os
import shutil
import requests
from get_questions import write_question_to_file

if __name__ == '__main__':
    try:
        day = str(len([name for name in os.listdir() if name[0:3] == 'Day']) + 1)
        path = './Day' + day
        os.mkdir(path)
        shutil.copy('./template/day._py', path + '/day' + day + '.py')
        shutil.copy('./template/day.test', path + '/day' + day + '.test')
        with open('./template/day_test._py', 'r') as test_file:
            content = test_file.read().replace('<day>', day)

        with open(path + '/day' + day + '_test.py', 'w') as new_file:
            new_file.write(content)

        with open('sessionid.txt', 'r') as session_id:
            session_id = session_id.read()
        with open(path + '/day' + day + '.input', 'w') as input_file:
            url = 'https://adventofcode.com/2020/day/' + day + '/input'
            cookies = dict(
                session=session_id)
            r = requests.get(url, cookies=cookies)
            input_file.write(r.text)

        write_question_to_file(day)

    except OSError as e:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
