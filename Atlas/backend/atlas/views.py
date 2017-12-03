from .models import User,Cultural_Heritage,comment,tag,image_media_item as image_item,hidden_tag
from rest_framework import generics
from django.http import HttpResponse, JsonResponse,HttpRequest
from django.core import serializers
from .serializers import cultural_heritage_serializer,image_media_item_serializer,tag_serializer,comment_serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from jwt_auth.compat import json
from rest_framework.test import APIRequestFactory
from django.contrib.postgres.search import SearchVector
from .util import hidden_tag_extractor



def users(request):
    users_list= serializers.serialize('json',User.objects.order_by('-age')[:5])
    return HttpResponse(users_list,content_type='application/json')

class cultural_heritage_item(generics.ListCreateAPIView):

    queryset = Cultural_Heritage.objects.get_queryset().order_by('id')
    serializer_class = cultural_heritage_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = LimitOffsetPagination
    def perform_create(self,serializer):
        serializer.save()
    def get_queryset(self):
        return Cultural_Heritage.objects.get_queryset().order_by('id')
    def create(self, request, *args, **kwargs):
        #Get the user from the request so that we can add it to cultural heritage item model.
        #Pk is the id of the user.
        request.data['user'] = request.user.pk
        images = []
        if 'images' in request.data:
            images = request.data['images']


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if len(images) > 0 :
            id = serializer.data['id']
            for image in images:
                image['cultural_heritage_item'] = id
                image_serializer = image_media_item_serializer(data=image)
                image_serializer.is_valid(raise_exception=True)
                image_serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ImageInterceptorMixin(object):
    @property
    def current_heritage_item(self):
        cultural_heritage_id = self.kwargs.get('heritage_id')
        return get_object_or_404(Cultural_Heritage,pk=cultural_heritage_id)

class cultural_heritage_item_comment(ImageInterceptorMixin,generics.CreateAPIView):
    queryset = comment.objects.all()
    serializer_class = comment_serializer
    def create(self, request, *args, **kwargs):
        try:
            comment_data = request.data['comment']
            request.data['cultural_heritage_item'] = self.current_heritage_item.pk
            for k, v in comment_data.items():
                request.data[k] = v
            request.data['user'] =request.user.pk
            result =super(cultural_heritage_item_comment, self).create(request, *args, **kwargs)
            return result
        except BaseException as e:
            return Response(json.dumps(str(e)), status=status.HTTP_400_BAD_REQUEST)


class image_media_item(ImageInterceptorMixin,generics.CreateAPIView):
    queryset = image_item.objects.all()
    serializer_class = image_media_item_serializer
    def create(self, request, *args, **kwargs):
        try:
            for image_item_data in request.data['images']:
                 request.data['cultural_heritage_item'] = self.current_heritage_item.pk
                 for k,v in image_item_data.items():
                     request.data[k] = v
                 result =super(image_media_item, self).create(request, *args, **kwargs)
            return result
        except BaseException as e:
            return Response(json.dumps(str(e)), status=status.HTTP_400_BAD_REQUEST)

class cultural_heritage_item_view_update_delete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = cultural_heritage_serializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        data = request.data
        if 'description' in data:
            instance.hidden_tags = []
            description = data['description']
            hidden_tags = hidden_tag_extractor.extract_keywords(hidden_tag_extractor, text=description)
            for tag in hidden_tags:
                new_tag, created = hidden_tag.objects.get_or_create(name=tag)
                if created:
                    instance.hidden_tags.add(new_tag)
            instance.save()

        self.perform_update(serializer)
        return Response(serializer.data)
    def get_queryset(self):
        return Cultural_Heritage.objects.filter()

class tags(generics.ListAPIView):
    serializer_class = tag_serializer
    pagination_class =  None
    def get_queryset(self):
        return tag.objects.get_queryset().order_by('id')


class cultural_heritage_item_list_user_items(generics.ListAPIView):

    serializer_class = cultural_heritage_serializer


    def get_queryset(self):
        user=self.request.user;
        return Cultural_Heritage.objects.filter(user=user)

class cultural_heritage_item_search(generics.ListAPIView):
    serializer_class = cultural_heritage_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        query = self.kwargs.get('query')
        return Cultural_Heritage.objects.annotate(
           search=SearchVector('tags__name', 'title','description'),
        ).filter(search=query)

class cultural_heritage_item_search_autocorrect(generics.ListAPIView):
    serializer_class = cultural_heritage_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        query = self.kwargs.get('query')
        return Cultural_Heritage.objects.filter(title__icontains=query)

