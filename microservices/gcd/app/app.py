from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource
class Gcd(Resource): 
	def get(self, num1, num2):
		print(type(num1))
		num1 = int(num1)
		num2 = int(num2)
		print(type(num1))
		if num1>num2:
			smaller=num2
		else:
			smaller=num1
		for i in range(1,smaller+1):
			if((num1%i == 0) and (num2%i == 0)):
				hcf = i		
		return {'result': hcf}

					
app = Flask(__name__)
api = Api(app)
api.add_resource(Gcd, '/<num1>/<num2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5063,
		host="0.0.0.0"
	)
