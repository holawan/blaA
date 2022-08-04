import json
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from crews.models import Crew, CrewArticle
from rest_framework import filters
from django.http import Http404
from django.db.models import Count 
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from crews.serializer.article import CrewArticleSerializer
from crews.serializer.crew import CrewCreateSerializer, CrewListSerializer, CrewSerializer



#리뷰를 작성할 가게 검색 or 가게 추가
class CrewListCreateAPIView(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = CrewCreateSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    queryset=Crew.objects.all()
    search_fields = ['crew_name']
    filterset_fields = ['is_business']

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CrewListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CrewListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(crew_leader=self.request.user)
        crew = Crew.objects.get(pk=serializer.data['crew_pk'])
        crew.crew_member.add(self.request.user)
        return serializer.data


#크루 상세조회, 크루 변경, 크루 삭제
# 변경 삭제는 크루 리더만 
class CrewRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView) :

    # authentication_classes=[]
    serializer_class = CrewSerializer
    queryset=Crew.objects.all()
    lookup_field = 'crew_pk'


    def update(self, request,crew_pk, *args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_pk)
        if request.user != crew.crew_leader :
            return Response({'message':"You do not have permission to change the user's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request,crew_pk, *args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_pk)
        if request.user != crew.crew_leader :
            return Response({'message':"You do not have permission to change the user's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CrewArticleListCreateAPIView(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = CrewArticleSerializer
    queryset=CrewArticle.objects.all()
    lookup_field = 'crew_id'

    def list(self, request, crew_id,*args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_id)
        if request.user in crew.crew_member.all() :

            queryset = CrewArticle.objects.filter(crew=crew_id).order_by('-crew_pin')
        else :
            queryset = CrewArticle.objects.filter(crew=crew_id,crew_private=False).order_by('-crew_pin')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, crew_id,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(crew_id,serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, crew_id,serializer):
        crew = Crew.objects.get(crew_pk=crew_id)
        serializer.save(user=self.request.user,crew=crew)
        return serializer.data


