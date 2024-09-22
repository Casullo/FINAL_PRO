from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: black;
            color: white;
            }
    </style>
    <title>Document</title>
</head>
<body>
<h1>hola mundo!</h1>
<p>Esto es párrafo </p>
<ul>
    <li>1. Hola asd</li>
    <li>2. Hola fgh</li>
    <li>3. Hola jkl</li>
    <li>4. Hola qwe</li>
</ul>
</body>
</html>
                        """
    )