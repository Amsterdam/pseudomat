from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets, generics

from pseudomat.models import Project
from pseudomat.serializers import UserSerializer, GroupSerializer, ProjectSerializer


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


class GroupViewSet(LoggedInMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProjectViewSet(LoggedInMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserProjects(LoggedInMixin, generics.ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(users=user)


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
