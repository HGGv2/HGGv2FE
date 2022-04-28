from django.shortcuts import render

# Create your views here.
def homehome(request):
  return render(request, 'mainmain.html')

def home(request):
  return render(request, 'index.html')

def category(request):
  return render(request, 'category.html')