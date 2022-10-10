from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Author
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    num_book = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()
    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_book': num_book,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


def authors(request):
    paginator = Paginator(Author.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    context = {
        "authors": paged_authors,
    }
    return render(request, 'authors.html', context=context)


def author(request, author_id):
    context = {
        'single_author': get_object_or_404(Author, pk=author_id),
    }
    return render(request, 'author.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Book.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    context = {
        'books': search_results,
        'query': query,
    }
    return render(request, 'search.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'


class UserBookInstanceListView(generic.ListView, LoginRequiredMixin):
    model = BookInstance
    template_name = 'user_books.html'
    context_object_name = 'instances'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(reader=self.request.user)
