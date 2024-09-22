from django.shortcuts import render
from django.http import HttpResponse  
from django.utils import timezone  

def hello_world(request):  
    current_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')  
    greeting_message = f"Привіт, я Ваш асистент! А це Шарій Єгор. Час відповіді: {current_time}"  
    return HttpResponse(greeting_message)
