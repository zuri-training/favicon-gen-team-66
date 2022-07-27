from django.shortcuts import render

# to test django connection to the template and static files
def home_page(request):
    return render(request, "account/home.html")
