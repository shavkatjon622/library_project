from django.template.defaultfilters import title
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)

    def validate(self, data): # objectni barcha malumotlari list bolib qaytadi uni tekshirishimiz mumkin boladi. Pastda birgina malumotni tekshirish kiritilgan
        title = data.get("title", None)
        author = data.get('author', None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    'massage':"Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak!"
                }
            )

        # check title and author from database existance
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    'massage':"Kitob sarlavhasi va muallifi bir xil bolgan kitob mavjud"
                }
            )
        return data

    def validate_price(self, price): # objectni birgina malumotini qaytaradi uni yuklab olgach keragicha tekshirishimiz mumkin.
        if price<0 or price<9999999999999:
            raise ValidationError(
                {
                    "status": False,
                    'massage': "Notogri narx kiritilgan"
                }
            )


# ModelSerializer bilan Serializer ikkisida ham bir xil ishni qila olamiz.
# ammo serializer ni ozi modelserializerga nisbatan tezroq ishlaydi katta malumotlar bilan ishlaganda.
# serilizerni yozilishi qisqacha
# class BookSerilizer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
# va hokazo Modelseralizerni ham overwrite qilib ozimiz hohlagandek yozsak boladi. holatiga kelgan joyiga ozimizga qulayligiga qarab ikkisidan birini tanlaymiz.
