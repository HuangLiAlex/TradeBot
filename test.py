from DBManager import DBManager
import json

db_mgr = DBManager()
error, message = db_mgr.find('000001SZ', 'daily')

if error:
    print(message)
else:
    try:
        data = json.loads(message)
        with open('./data/000001SZ.json', 'w') as file:
            file.write(json.dumps(data, indent=4, sort_keys=True))

        print('Task Completed')

    except Exception as ex:
        print(ex)
