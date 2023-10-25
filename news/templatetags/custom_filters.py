from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value):
    """ * maker censor """
    unwanted_words = [ 'хрен']
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))
    return value
