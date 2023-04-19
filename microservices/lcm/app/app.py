from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource
class Lcm(Resource):
 
	def get(self, num1, num2):
		num1 = int(num1)
		num2 = int(num2)
		if num1>num2:
			greater = num1
		else:
			greater = num2
		while (True):
 	 	 	if ((greater % num1 == 0) and (greater % num2 == 0)):
 	 	 	 	l = greater
 	 	 	 	break
 	 	 	greater += 1
		return {'result': l}

app = Flask(__name__)
api = Api(app)
api.add_resource(Lcm, '/<num1>/<num2>')

if __name__ =="__main__":
		app.run(
		debug=True,
		port=5061,
		host="0.0.0.0"
	)

