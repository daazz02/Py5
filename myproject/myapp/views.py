from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_info(request):
    html = """
    <html>
    <body>
        <h2>Інформація про мене</h2>
        <table border="1" cellpadding="10">
            <tr><th>Поле</th><th>Значення</th></tr>
            <tr><td>Ім'я</td><td>Дар'я</td></tr>
            <tr><td>Прізвище</td><td>Кірковська</td></tr>
            <tr><td>Спеціальність</td><td>126</td></tr>
            <tr><td>Група</td><td>ІСД-31</td></tr>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)
