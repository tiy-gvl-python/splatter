from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from splat.models import Splat, Splatee


def user_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2
        })
        try:
            user_form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                              {'form': user_form},
                              context_instance=RequestContext(request))


    return render_to_response("registration/create_user.html",
                              {'form': UserCreationForm()},
                              context_instance=RequestContext(request))


def splat_list(request):
    all_splats = Splat.objects.all()
    context = {"messages": all_splats}
    return render_to_response("list_splats.html", context, context_instance=RequestContext(request))

@login_required
def splat_detail(request, splat_id):
    try:
        splat = Splat.objects.get(id=splat_id)
    except Splat.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"splat": splat}
    return render_to_response("splat_detail.html", context, context_instance=RequestContext(request))


def user_detail(request, user_id):
    try:
        splatee = Splatee.objects.get(id=user_id)
    except Splatee.DoesNotExist:
        return HttpResponseNotFound("Not Found!")
    context = {"splatee": splatee}
    return render_to_response("user_detail.html", context, context_instance=RequestContext(request))
