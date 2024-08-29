from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'personal/about.html')

def my_shop_view(request):
    return render(request, 'personal/my_shop.html')
