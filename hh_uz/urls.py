from django.urls import path

from hh_uz.views import ProfessionTypeApiView, CompanyListApiView, JobFilterListApiView, \
    CustomJobListView, JobDetailApiView, SimilarJobListApiView

urlpatterns = [
    path('job-filter/', JobFilterListApiView.as_view()), # 👌
    path('recommended/', CustomJobListView.as_view()), # 👌
    path('profession-type/', ProfessionTypeApiView.as_view()), # 👌
    path('job-detail/<int:pk>', JobDetailApiView.as_view()), # 👌
    path('similar-jobs/<str:similar_job>', SimilarJobListApiView.as_view()), # 👌
    path('job-list/', JobDetailApiView.as_view())




    # path('companies/', CompanyListApiView.as_view()),
    # path('experiences/', ExperienceListApiView.as_view())

]



