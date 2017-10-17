from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'survey/index.html')

def form_processing(request):
    if request.method == "POST":
    	request.session['name'] = request.POST['name']
    	request.session['location'] = request.POST['location']
    	request.session['language'] = request.POST['language']
    	request.session['comment'] = request.POST['comment']
    	# print request.POST['name']
    	# print request.POST['location']
    	# print request.POST['language']
    	# print request.POST['comment']
    	return redirect("/result")
    else:
    	return redirect("/")

def result(request):
    return render(request, 'survey/result.html')