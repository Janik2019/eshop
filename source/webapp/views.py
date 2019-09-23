from django.shortcuts import render, get_object_or_404
from webapp.models import Product


def index_view(request):
    # примеры фильтрации по совпадению значений и сортировки есть в раздатке #43.
    # здесь приведён пример фильтрации по другому критерию: "больше, чем".
    # в Django другие критерии фильтрации обозначаются с помощью т.н. "лукапов"
    # (англ. "lookup"), специальных слов, которые пишутся после названия полей
    # через двойное подчёркивание - "__". Например, лукап "gt" обозначает "greater than" -
    # "больше, чем", и таким образом Django будет искать записи, у которых поле amount
    # больше, чем заданное значение (0).
    # Список лукапов приведён в документации Django здесь:
    # https://docs.djangoproject.com/en/2.2/topics/db/queries/#field-lookups.
    # Также PyCharm при правильной настройке начинает подсказывать, что вы можете
    # записать в аргументах filter() для той или иной модели.
    products = Product.objects.filter(amount__gt=0)
    return render(request, 'index.html', context={
        'products': products
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })
