from django.shortcuts import render

def index(request):
    heading = 'Hi, Welcome'

    datas= [
        {'id': 1, 'title': 'First Post', 'content': 'This is the first post.', "img_url": "https://picsum.photos/id/1/200/200"},
        {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.', "img_url": "https://picsum.photos/id/2/200/200"},
        {'id': 3, 'title': 'Third Post', 'content': 'This is the third post.', "img_url": "https://picsum.photos/id/3/200/200"},
        {'id': 4, 'title': 'Fourth Post', 'content': 'This is the fourth post.', "img_url": "https://picsum.photos/id/4/200/200"},
        {'id': 5, 'title': 'Fifth Post', 'content': 'This is the fifth post.', "img_url": "https://picsum.photos/id/5/200/200"},
    ]

    return render(request, 'index.html', {'heading': heading, 'datas': datas})

def details(request):
    return render(request, 'details.html')