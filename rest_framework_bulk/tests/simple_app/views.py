from __future__ import unicode_literals, print_function
from rest_framework_bulk import generics

from .models import SimpleModel, UniqueTogetherModel
from .serializers import SimpleSerializer, UniqueTogetherSerializer


class SimpleMixin(object):
    model = SimpleModel
    queryset = SimpleModel.objects.all()
    serializer_class = SimpleSerializer


class SimpleBulkAPIView(SimpleMixin, generics.ListBulkCreateUpdateDestroyAPIView):
    pass


class FilteredBulkAPIView(SimpleMixin, generics.ListBulkCreateUpdateDestroyAPIView):
    def filter_queryset(self, queryset):
        return queryset.filter(number__gt=5)


class SimpleViewSet(SimpleMixin, generics.BulkModelViewSet):
    def filter_queryset(self, queryset):
        return queryset.filter(number__gt=5)


class UniqueTogetherViewSet(generics.BulkModelViewSet):
    model = UniqueTogetherModel
    queryset = UniqueTogetherModel.objects.all()
    serializer_class = UniqueTogetherSerializer
