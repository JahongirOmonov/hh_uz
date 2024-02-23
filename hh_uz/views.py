from django.db.models import Count
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProfessionType, Company, Job
from .serializers import ProfessionTypeSerializer, CompanySerializer, JobSerializer, \
    CustomJobSerializer, JobDetailSerializer, SimilarJobSerializer, JobListSerializer


# class ExperienceListApiView(generics.ListAPIView):
#     queryset = Experience.objects.all()
#     serializer_class = ExperienceSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class CompanyListApiView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class JobFilterListApiView(generics.ListAPIView):
    queryset = Job.objects.all().select_related("company", "experience")
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        "price_from",
        "price_to",
        "career",
        "company",
        "region"
    )
    search_fields = ("title", "company__title", "experience__title")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class JobDetailApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer








class CustomJobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = CustomJobSerializer



class ProfessionTypeApiView(ListModelMixin, GenericAPIView):
    serializer_class = ProfessionTypeSerializer
    queryset = ProfessionType.objects.annotate(job_count=Count('jobs'))


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SimilarJobListApiView(generics.ListAPIView):
    serializer_class = SimilarJobSerializer

    def get_queryset(self):
        similar_job = self.kwargs['similar_job']
        return Job.objects.filter(profession_type__title=similar_job)

class JobsListApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer


