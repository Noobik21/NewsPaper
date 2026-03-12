<<<<<<< HEAD
from django import template

register = template.Library()

BAD_WORDS = ['редиска', 'плохой']

@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Фильтр "censor" применяется только к строкам')

    for word in BAD_WORDS:
        value = value.replace(word, word[0] + '*' * (len(word) - 1))
        value = value.replace(word.capitalize(), word[0] + '*' * (len(word) - 1))

=======
from django import template

register = template.Library()

BAD_WORDS = ['редиска', 'плохой']

@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Фильтр "censor" применяется только к строкам')

    for word in BAD_WORDS:
        value = value.replace(word, word[0] + '*' * (len(word) - 1))
        value = value.replace(word.capitalize(), word[0] + '*' * (len(word) - 1))

>>>>>>> d694537e88001b783309c247ae3642d947d0a82a
    return value