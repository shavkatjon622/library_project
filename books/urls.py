from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import BookListApiView, book_list_view, BookDetailApiView, BookDeleteApiView, \
    BookUpdateApiView, BookCreateApiview, BookListCreateApiView, BookUpdateDeleteApiView, BookViewset

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('booklistcreate/', BookListCreateApiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),
    # path('books/create/', BookCreateApiview.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('book/', book_list_view),
]

urlpatterns = urlpatterns +  router.urls    # qoshimcha malumotlar django_rest frameworks class base views