from django import template   

register = template.Library()
    
@register.filter(name='cambia_url')
def cambia_url(url, prefijo):
    if url.startswith(prefijo):
        return url.replace(prefijo,"")
    return url