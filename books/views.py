from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# class view larni def yozib ichki methodlarini tahrirlab olsa boladi
# class BookListApiView(generics.ListAPIView): # Objectlarni barchasini list korinishida chiqarish uchun
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView): # generics.ListAPIview larni o'rniga tushunish oson bolishi uchun

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data  # .data berilmagan holatda qaytgan malumot object boladi uni json ga .data orqali otkazamiz
        data = {
            "status" : f"Returned {len(books)} books",
            "books" : serializer_data,
        }
        print(data)
        return Response(data)



class BookDetailApiView(generics.RetrieveAPIView): # id orqali birgina objectni olish uchun
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(APIView):

     def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status": "Succesfully",
                "book": serializer_data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status": "Does not found",
                    "massage": 'Book is not found'
                }, status=status.HTTP_404_NOT_FOUND
            )




# class BookDeleteApiView(generics.DestroyAPIView): # id orqali objectni ochirish uchun
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
     def delete(self, request, pk):
         try:
             book = Book.objects.get(id=pk) # get_object_or_404 tekshir
             book.delete()
             return Response(
                 {
                     "status":True,
                     "massage":"Successfully deleted"
                 }, status=status.HTTP_200_OK
             )
         except Exception:
             return Response(
                 {
                     "status": False,
                     "massage":'Book is not found'
                 }, status=status.HTTP_400_BAD_REQUEST
             )





# class BookUpdateApiView(generics.UpdateAPIView): # id orqali objectni tahrirlash uchun
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer



class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

            return Response(
                {
                    'status': True,
                    "massage":f"Book {book_saved} updated successfully"
                }
            )



# class BookCreateApiview(generics.CreateAPIView): #post request yangi object yaratish uchun
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateApiview(APIView): # generic viewni almashtirib APIviewdan foydalandik

    def post(self, request):
        data  = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': 'Books are saved to the database',
                'books': data
            }
            return Response(data)
        else:
            return Response(
                {
                    "status": False,
                    "massage": "Serializer is not found"
                }, status=status.HTTP_400_BAD_REQUEST
            )



class BookListCreateApiView(generics.ListCreateAPIView): # objectlar royxatini korsatadi shu bilan birga post methodi bilan object qoshishga ham imkon beradi
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView): # bir dona object ni olib update delete hamda get methodlaridan foydalanish imkoniyatini beradi
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




# function viewdan hozirda ommamiy foydalinishmaydi shu sababdan best practise sifatida class view ishlatgan yaxshiroq
@api_view(['GET'])  # function view ni dekorator bilan yoziladi
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()   # class ga tegishli barcha obyectlarni database dan oladi
    serializer = BookSerializer(books, many=True) # serializer ko`plab object larni qabul qilishi uchun many=True qilindi
    return Response(serializer.data)