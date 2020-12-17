from django import template

register = template.Library()

@register.filter(name='get_val')
def get_val(dict,key):
    #print("***",key)
    return dict.get(key)

@register.filter(name='get_value')
def get_value(id):
    print('***',id)
    return id