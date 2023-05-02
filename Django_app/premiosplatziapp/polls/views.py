from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    html_response = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hola Mundo</title>
            <style>
                body {
                    background-color: #fdfd96;
                    font-family: Arial, sans-serif;
                    font-size: 24px;
                    color: #333;
                    text-align: center;
                    margin-top: 50px;
                }
                h1 {
                    font-size: 48px;
                    margin-bottom: 50px;
                }
            </style>
        </head>
        <body>
            <h1>Hola Mundo</h1>
            <p>¡Bienvenido al maravilloso mundo de la programación!</p>
        </body>
        </html>
    """
    return HttpResponse(html_response)
