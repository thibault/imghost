from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def full_img_url(context, url):
    request = context['request']
    clean_url = url.replace('/media/i/', '/i/')
    return request.build_absolute_uri(clean_url)
