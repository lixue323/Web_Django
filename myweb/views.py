from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'shop/index.html')

def show(request):
	return render(request,'shop/show.html')

def content(request):
	return render(request,'shop/content.html')

def denglu1(request):
	return render(request,'shop/denglu1.html')

def buycar(request):
	return render(request,'shop/buycar.html')
