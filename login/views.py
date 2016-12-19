from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def login(request):
	# SET YOUR PASSWORD HERE!
	your_password = 'put_your_password_here'
	if request.method == 'POST':
		if request.POST['password'] == your_password:
			return render_to_response('success.html', context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', context_instance=RequestContext(request))
