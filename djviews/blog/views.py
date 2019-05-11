from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import Q
# Create your views here.
from .models import PostModel
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm


def post_model_create_view(request):
    # if request.method == 'POST':
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)


    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # print(form.cleaned_data)
        obj.save()
        messages.success(request, 'created a new blog post!')
        return HttpResponseRedirect(f"/blog/{obj.id}/")
    context = {
        "form": form
    }
    template = "blog/create-view.html"
    return render(request, template, context)


def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        # print(form.cleaned_data)
        obj.save()
        messages.success(request, 'Updated post!')
        return HttpResponseRedirect(f"/blog/{obj.id}/")
    context = {
        "obj": obj,
        "form": form
    }
    template = "blog/update-view.html"
    return render(request, template, context)


def post_model_detail_view(request, id=None):
    object = get_object_or_404(PostModel, id=id)
    context = {
        "object": object
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


def post_model_delete_view(request, id=None):
    object = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        object.delete()
        messages.success(request, "Post delete!")
        return HttpResponseRedirect('/blog/')
    context = {
        "object": object
    }
    template = "blog/delete-view.html"
    return render(request, template, context)


def post_model_list_view(request):
    query = request.GET.get('q', None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    if request.user.is_authenticated:
        template_path = "blog/list-view.html"
    else:
        template_path = "blog/list-view-public.html"
        # raise Http404

    # return HttpResponse("some data")
    context_dictionary = {
        "object_list": qs,
        "some_dict": {"abc": 123},
        "num": 123,
        "array_list": [123, 423],
        "boolean_value": True,
    }
    return render(request, template_path, context_dictionary)
