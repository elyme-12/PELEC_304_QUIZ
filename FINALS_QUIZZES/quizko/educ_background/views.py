from django.shortcuts import render
from .forms import StudentForm

def elementary(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'success.html')
    else:
        form = StudentForm()
    return render(request, 'elementary.html', {'form':form})

def highschool(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'success.html')
    else:
        form = StudentForm()
    return render(request, 'highschool.html', {'form':form})

def seniorhigh(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'success.html')
    else:
        form = StudentForm()
    return render(request, 'seniorhigh.html', {'form':form})

# def studentback3(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render (request, 'Success.html')
#     else:
#         form = StudentForm()
#     return render(request, 'ledub.html', {'form':form})


