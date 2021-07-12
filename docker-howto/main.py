from flask import Flask, json

webRespose = { "person": [{"born": "17.11.2020", "gender": "mann", "f-nr": "17912099997", "d-nr": "57912075186"}, {"born": "29.02.2020", "gender": "kvinne", "f-nr": "29822099635", "d-nr": "69822075096"}] }

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
  return json.dumps(webRespose)

if __name__ == '__main__':
    api.run(port=8080, host='0.0.0.0')