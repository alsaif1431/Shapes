from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def circle(request):
    if request.method == 'POST':
        radius = float(request.POST['radius'])
        area = 3.142 * radius ** 2
        return render(request, 'circle.html', {'area': area})
    return render(request, 'circle.html')


def rectangle(request):
    if request.method == 'POST':
        length = float(request.POST['length'])
        breadth = float(request.POST['breadth'])
        area = length * breadth
        return render(request, 'rectangle.html', {'area': area})
    return render(request, 'rectangle.html')


def triangle(request):
    if request.method == 'POST':
        base = float(request.POST['base'])
        height = float(request.POST['height'])
        area = 0.5 * base * height
        return render(request, 'triangle.html', {'area': area})
    return render(request, 'triangle.html')


def sphere(request):
    if request.method == 'POST':
        radius = float(request.POST['volume'])
        area = 4 * 3.14 * radius ** 2
        return render(request, 'sphere.html', {'area': area})
    return render(request, 'sphere.html')


def frustrum(request):
    if request.method == 'POST':
        radius1 = float(request.POST['upperfrustrum'])
        radius2 = float(request.POST['lowerfrustrum'])
        height = float(request.POST['height'])
        area = 3.14 * height * (radius1 + radius2) + 3.142 * (radius1 ** 2 + radius2 ** 2)
        return render(request, 'frustrum.html', {'area': area})
    return render(request, 'frustrum.html')
    


def output(request):
    return render(request, "output.html")
