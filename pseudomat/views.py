from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, generics

from pseudomat.models import Project
from pseudomat.serializers import UserSerializer, ProjectSerializer


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class UserViewSet(LoggedInMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=user.id)

class ProjectViewSet(LoggedInMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Project.objects.all()
        else:
            return Project.objects.filter(users=user)


def index(request):
    user = request.user
    if user.is_authenticated:
        projects = Project.objects.filter(users=user)
    else:
        projects = []

    context = {
        'user': user,
        'projects': projects,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/')
def project(request, project_id):
    user = request.user
    try:
        project = Project.objects.filter(users=user).filter(id=project_id)[:1].get()
    except ObjectDoesNotExist:
        return HttpResponse('Project does not exist or you are not allowed to view it', 404)

    context = {
        'user': user,
        'project': project
    }
    return render(request, 'project.html', context)

