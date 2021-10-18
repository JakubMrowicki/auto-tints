from django.shortcuts import render

# Create your views here.

def faq(request):
    """ Return FAQ page """

    return render(request, 'pages/faq.html')
