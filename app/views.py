from django.shortcuts import render

# Create your views here.
def conditions(request):
    d = {'name': 'Ram', 'age': 25, 'marks': 90}
    return render(request, 'conditions.html', context=d)
