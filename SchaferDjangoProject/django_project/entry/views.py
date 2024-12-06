from django.shortcuts import render

posts = [
    {
        'author': 'Ethan F.',
        'title': 'Mileage Entry 2024/12/06',
        'content': 'District: BCSD; School: District Office; Odometer: 101011',
        'date_posted': 'December 6th, 2024'
    },
    {
        'author': 'James M.',
        'title': 'Mileage Entry 2024/12/07',
        'content': 'District: BCSD; School: District Office; Odometer: 101012',
        'date_posted': 'December 7th, 2024'
    }
]


def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'entry/home.html', context)


def about(request):
    return render(request, 'entry/about.html', {'title': 'About'})