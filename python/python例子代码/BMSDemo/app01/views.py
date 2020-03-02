from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.

from app01 import models


# def addbook(request):
#     # 添加数据
#     if request.method == "GET":
#         return render(request, 'addbook.html')
#
#     else:
#         title = request.POST.get('title')
#         pub_date = request.POST.get('pub_date')
#         price = request.POST.get('price')
#         publish = request.POST.get('publish')
#         Book.objects.create(title=title, pub_date=pub_date, price=price, publish=publish)
#         return redirect('/books')
#

def index(request):
    return render(request, 'index.html')


def book_list(request):
    book_queryset = models.Book1.objects.all()
    return render(request, 'book_list.html', locals())


def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish')
        author_list = request.POST.getlist('author')

        book_obj = models.Book1.objects.create(title=title, price=price, publish_id=publish_id)
        book_obj.authors.add(*author_list)

        return redirect('book_list')
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'addbook.html', locals())


def book_edit(request, edit_id):
    edit_obj = models.Book1.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        models.Book1.objects.filter(pk=edit_id).update(title=title, price=price,
                                                       publish_id=publish_id
                                                       )
        edit_obj.authors.set(authors_list)

        return redirect('book_list')
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    # return HttpResponse(edit_id)
    return render(request, 'book_edit.html', locals())


def book_delete(request, delete_id):
    models.Book1.objects.filter(pk=delete_id).delete()
    return redirect('book_list')


def test(request):
    l = [1, 2, 3, 45, 6, 767, 76, 8, 7]
    publish_queryset = models.Publish.objects.all()
    return render(request, 'test.html', locals())
