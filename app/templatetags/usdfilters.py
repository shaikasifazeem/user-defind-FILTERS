from django import template
register=template.Library()

def swap(value):
    return value.swapcase()
register.filter('swap',swap)

def lower(value):
    return value.lower()
register.filter('lower',lower)

def upper(value):
    return value.upper()
register.filter('upper',upper)

def remove(value,arg):
    return value.replace(arg,'asif')
register.filter('remove',remove)

def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:

            c=c+1
    return c 
register.filter('counting',counting)

def vijji(value,arg):
    return value.replace(arg,' ')
register.filter('vijji',vijji)



@register.filter()
def asif(value,arg):
    return value.replace(arg,'vijji DABBAFELLOW !!!!')

@register.filter()
def azeem(value,arg):

    return value.replace(arg,'vijji is very very inka WORDS LEV ANTAKUMINCHINA GIRL')
@register.filter(name='title')
def vijji1(value):
    return value.title()