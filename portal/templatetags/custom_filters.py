from django import template
import re

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются


#put {% load custom_filters %} into html files!

@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):  # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')  #  в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку
# {{ product.name|multiply:4 }}

@register.filter(name='censor')
def censor(text):
    bad_words = ["fuck", "FUCK", "Fuck"]
    for w in bad_words:
        text = re.sub(w, "*", text)

    return text
