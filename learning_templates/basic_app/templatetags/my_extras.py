from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')


#register.filter('cut', cut) #first argument is the name of the new filter, second argument is the new filter function itself
