from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template import loader
from django.views.generic import ListView
from labworks.models import Lab
from tasks.models import Task
from .forms import LabForm
from django.shortcuts import redirect



def admin_check(user):
    if user.groups.filter(name__in=['Students']) or user.is_superuser:
        return True
    else:
        return False

@user_passes_test(admin_check)
def create(request):
    if request.method == "POST":
        form = LabForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            labwork = form.save(commit=False)
            labwork.mark = 0
            labwork.condition = "не проверена"
            labwork.author = request.user
            labwork.task = Task.objects.get(id=2)
            labwork.save()
            return redirect ('detail', lab_id=labwork.pk)
        return render(request, 'labworks/create_lab.html', {'form': form})
    else:
        # course_id = request.GET.get('course_id', '')
        form = LabForm()
    return render(request, 'labworks/create_lab.html', {'form': form})


def detail(request, lab_id):
    # output = Course.objects.get(id=course_id)
    output = get_object_or_404(Lab, id=lab_id)
    context = {'one_lab': output}
    return render(request, 'labworks/one_lab.html', context)
