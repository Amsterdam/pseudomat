from django.contrib.auth.models import User, Group
from rest_framework import serializers

from pseudomat.models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'name', 'users', 'vao_ip', 'upload_dir')
        depth = 0
