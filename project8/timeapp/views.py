from django.shortcuts import render
import datetime

def server_time(request):
	server_time=datetime.datetime.now()

	dict={'time':server_time}
	return render(request=request,template_name='timeapp/time.html', context=dict)

# Create your views here.
