# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, Response, json
import _mysql


app = Flask(__name__)
@app.route('/add', methods=['POST'])
def events():
    event_data = request.json
    print(event_data)
    database = _mysql.connect("localhost", "root", db='projekt')
    database.set_character_set('utf8')

    database.query("""INSERT INTO `quiz` (`pytanie`, `a`, `b`, `c`, `d`, `poprawna`) VALUES(%s, %s, %s, %s, %s, %s);"""
                                                            % (event_data['pytanie'],
                                                             event_data['a'], event_data['b'],
                                                             event_data['c'], event_data['d'],
                                                             event_data['poprawna']))
    return 'ok'


@app.route("/")
def hello():
    database = _mysql.connect("localhost", "root", db='projekt')
    database.set_character_set('utf8')
    database.query("""select * from quiz""")
    resultFromDatabase = database.store_result()
    allRowFromDb = resultFromDatabase.fetch_row(maxrows=0)
    payload = []
    contentTemporary = {}
    for a, value in enumerate(allRowFromDb):
        contentTemporary = {
            'id': str(value[0]),
            'pytanie': value[1].decode('utf-8'),
            'a': value[2].decode('utf-8'),
            'b': value[3].decode('utf-8'),
            'c': value[4].decode('utf-8'),
            'd': value[5].decode('utf-8'),
            'poprawna': value[6].decode('utf-8')
        }
        payload.append(contentTemporary)
        contentTemporary = {}

    return jsonify(payload)

if __name__ == "__main__":
    app.run(debug=True)
