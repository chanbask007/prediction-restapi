from flask import Flask
from flask_restful import Resource, Api, reqparse

from datetime import datetime
import pickle


app = Flask(__name__)
api = Api(app)

model= pickle.load( open('model.pkl' , 'rb'))

parser= reqparse.RequestParser()
parser.add_argument('voltage',location='json')
parser.add_argument('current',location='json')
parser.add_argument('power',location='json')
parser.add_argument('powerfactor',location='json')
parser.add_argument('energy',location='json')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        now = datetime.strptime('2019-09-06 8:01:30', "%Y-%m-%d %H:%M:%S")
        timestamp = datetime.timestamp(now)
        args= parser.parse_args()
        voltage= float(args['voltage'])
        current= float(args['current'])
        energy= float(args['energy'])
        power= float(args['power'])
        powerfactor= float(args['powerfactor'])
        prediction=model.predict([[voltage,current,energy,powerfactor,timestamp]])
        # print(prediction[0])



        return {
              "prediction": round(prediction[0],2)  
            }

api.add_resource(HelloWorld, '/')



if __name__ == '__main__':
    app.run(debug=True)
