from annoying.decorators import render_to


@render_to('upload.html')
def upload(request):
    return {}
