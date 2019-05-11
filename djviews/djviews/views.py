from django.http import HttpResponse, HttpResponseRedirect

#
# def home(request):
#     print(request.is_ajax())
#     print(request.get_full_path())
#     return HttpResponse('<h1>Hello World</h1>')


def home(request):
    response = HttpResponse(content_type='application/json')
    # response.write("<p>Here's the text </p>")
    # response.write("<p>Here's the text </p>")
    # response.write("<p>Here's the text </p>")
    # response.write("<p>Here's the text </p>")
    response.content = '<h1>Some new content</h1>'
    response.status_code = 200
    return response


def redirect_somewhere(request):
    return HttpResponseRedirect("/")
