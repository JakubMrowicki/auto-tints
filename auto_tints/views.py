from django.shortcuts import render


def page_not_found_view(request, exception):
    # 404 handler
    return render(request, '404.html', status=404)


def server_error_view(request, exception):
    # 500 handler
    return render(request, '500.html', status=500)
