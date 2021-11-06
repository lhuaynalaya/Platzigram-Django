from django.http import HttpResponse
from datetime import datetime
import json

def hello(request):
	now = datetime.now().strftime('%b %dth, %Y')
	return HttpResponse('hola {now}'.format(now=now))

def sort_integers(request):
	"""imprimir el request"""
	#print(request)

	#debugger
	#import pdb; pdb.set_trace()
	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Enteros ordenados'
	}

	return HttpResponse(json.dumps(data), content_type='application/json')

def hi(request, name, age):
	age = int(age)
	if age < 12:
		message = 'Sorry {}, you are allowed here'.format(name)
	else:
		message = 'Hello {}, welcome to platzigram'.format(name)

	return HttpResponse(message)
