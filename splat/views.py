from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from splat.models import Splat, Splatee


def splat_list(request):
    all_splats = Splat.objects.all()
    context = {"messages": all_splats}
    return render_to_response("list_splats.html", context)


def splat_detail(request, splat_id):
    try:
        splat = Splat.objects.get(id=splat_id)
    except Splat.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"splat": splat}
    return render_to_response("splat_detail.html", context)


def user_detail(request, user_id):
    try:
        splatee = Splatee.objects.get(id=user_id)
    except Splatee.DoesNotExist:
        return HttpResponseNotFound("Not Found!")
    context = {"splatee": splatee}
    return render_to_response("user_detail.html", context)
