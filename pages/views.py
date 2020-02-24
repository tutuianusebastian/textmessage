from django.shortcuts import render

def home(request):
	context = {'title': 'SPECIAL'}
	return render(request, 'home.html', context)