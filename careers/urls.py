from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.RealtyView.as_view()),
    # path("vacancies/", views.VacanciesListAPIView.as_view()),
    # path("<int:pk>/", views.VacanciesDetailView.as_view()),
    # path("vacancies/<int:pk>", views.VacanciesDetailAPIView.as_view()),
    # path("request/", views.RequestCreateView.as_view()),
    # path("practice/", views.AddPracticeView.as_view()),
    # path("practice/<int:pk>", views.DeletePracticeView.as_view()),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)