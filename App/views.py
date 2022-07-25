from django.shortcuts import render

# Function to render the Home Page.

def frontend(request):
    return render(request, 'frontend.html')
