from django.shortcuts import render
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

# from .serializers import VacanciesListSerializer, VacanciesDetailSerializer, CreateRequestForPracticeSerializer, ResumeSerializer, CreatePracticeSerializer, DeletePracticeSerializer
from .models import Realty


class RealtyView(View):
    def get(self, request):
        realty = Realty.objects.all()
        return render(request, "realty_list.html", {"realty_list": realty})

# class VacanciesListAPIView(APIView):
#     def get(self, request):
#         vacancies = Vacancies.objects.order_by("title")
#         serializer = VacanciesListSerializer(vacancies, many=True)
#         return Response(serializer.data)


# class VacanciesDetailView(View):
#     def get(self, request, pk):
#         vacancy = Vacancies.objects.get(id=pk)
#         return render(request, "vacancy_detail.html", {"vacancy": vacancy})


# class VacanciesDetailAPIView(APIView):
#     def get(self, request, pk):
#         vacancy = Vacancies.objects.get(id=pk)
#         serializer = VacanciesDetailSerializer(vacancy)
#         return Response(serializer.data)

# class RequestCreateView(APIView):
#     def post(self, request):
#         requestPractice = CreateRequestForPracticeSerializer(data=request.data)
#         if requestPractice.is_valid():
#             requestPractice.save()
#         return Response(status=201) 

# class AddPracticeView(APIView):
#     def post(self, request):
#         serializer = CreatePracticeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         else:
#             return Response(status=400)

# class DeletePracticeView(APIView):
#     def delete(self, request, pk):
#         serializer = DeletePracticeSerializer(data=pk)
#         if serializer.is_valid():
#             return Response(status=201)
#         else:
#             return Response(status=400)