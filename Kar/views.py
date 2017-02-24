from django.shortcuts import render, render_to_response


def karaoke_welcome(request):
    return render(request, 'home.html')
