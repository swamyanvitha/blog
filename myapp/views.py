from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person
# Create your views here.
def index(request):
	r = Person.objects.all()
	for i in r:
		a = i.name
	context = {'a':a}
	return render(request,'index.html',context)
	