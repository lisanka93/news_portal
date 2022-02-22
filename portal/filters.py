from django_filters import FilterSet, DateFilter # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post
from django import forms




# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    #time_post = DateFromToRangeFilter()

    time_post = DateFilter(
    lookup_expr='gte',
    widget=forms.DateInput(
        attrs={
            'type': 'date'
        }
    )
)

    class Meta:
        model = Post
        #fields = ['time_post']  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)

        fields = {
            'title': ["icontains"],
            'author': ['exact'],  # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            #'time_post': ['gte'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'category': ['exact'],  # цена должна быть меньше или равна тому, что указал пользователь
        }
        #row_date = DateFilter(widget=DateInput(attrs={'type': 'date'}))
