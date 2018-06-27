from django.shortcuts import render
from django.db.models import Max, Min
import random
from rest_framework import permissions, viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
import backend.models as app_models
import backend.serializers as app_serializers
from django.db.models import Count


import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'backend/templates/')

def index(request):
    return render(request, 'index.html')


def https_view_1(request):
    return HttpResponse(open(XMLFILES_FOLDER + 'iJWaUiJulIuA-b5RZgxdxuSl8AjrNH57GnEKJzf0d2Y', "rb").read(), content_type="text/xml")


def https_view_2(request):
    return HttpResponse(open(XMLFILES_FOLDER + 'KHbZ7N85wkULa9I997i886bGodd0jHfERLtHyNA0ObU', "rb").read(), content_type="text/xml")


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = app_models.Tag.objects.all()

    def get_all_tags(self, request, *args, **kwargs):

        try:
            tag_objects = self.queryset.exclude(name="miscellaneous").order_by("name")
            tag_serializer = app_serializers.TagSerializer(tag_objects, many=True)
            return JsonResponse({"tags": tag_serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DialogueViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = app_models.Dialogues.objects.all()

    def search_results(self, request, *args, **kwargs):
        try:
            query = str(request.GET['query'])
        except:
            return JsonResponse({"error": "Bad Parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            return_obj = []
            success = False
            if len(query.strip()):
                movie_objects = app_models.Dialogues.objects.filter(movie_name__icontains=query).order_by().values_list('movie_name', 'movie_year').distinct()
                actor_objects = app_models.Dialogues.objects.filter(star__icontains=query).order_by().values_list('star').distinct()
                for each_obj in movie_objects:
                    return_obj.append({
                        'name': '{name}_{year}'.format(name=str(each_obj[0]), year=str(each_obj[1])),
                        'value': '{name}|{year}'.format(name=str(each_obj[0]), year=str(each_obj[1])),
                        'text': "{name} ({year})".format(name=str(each_obj[0]), year=str(each_obj[1])),
                        'type': "movie"
                    })
                for each_obj in actor_objects:
                    return_obj.append({
                        'name': str(each_obj[0]),
                        'value': str(each_obj[0]),
                        'text': str(each_obj[0]),
                        'type': "star"
                    })
            if len(return_obj) != 0:
                success = True
            return JsonResponse({"success": success, "results": return_obj}, status=status.HTTP_200_OK)
        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_dialogues(self, request, *args, **kwargs):

        # Get All Parameters
        try:
            # limit = int(request.GET["limit"])
            include_tags = list(map(lambda tag: int(tag), request.GET["include_tags"].strip().split(',')))
            year_min = int(request.GET["year_min"])
            year_max = int(request.GET["year_max"])
            movie_name = str(request.GET['movie_name']).strip()
            movie_year = str(request.GET['movie_year']).strip()
            star = str(request.GET['star']).strip()
        except:
            return JsonResponse({"error": "Bad Parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:

            if movie_name != '0':
                dialogue_objects = self.queryset.filter(movie_name__icontains=movie_name, movie_year=movie_year)
            elif star != '0':
                dialogue_objects = self.queryset.filter(star__icontains=star)
            else:
                dialogue_objects = self.queryset.filter(movie_year__gte=year_min, movie_year__lte=year_max)

                # Filter by tags
                if include_tags[0] != 0:
                    dialogue_objects = dialogue_objects.filter(tag__in=include_tags)

            dialogue = random.choice(dialogue_objects)
            dialogue_ser = app_serializers.DialogueSerializer(dialogue)
            return JsonResponse({"dialogue": dialogue_ser.data}, status=status.HTTP_200_OK)

        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_dialogue(self, request, *args, **kwargs):

        # Get All Parameters
        try:
            dialogue_id = str(request.GET['dialogue_id']).strip()
        except:
            return JsonResponse({"error": "Bad Parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:

            dialogue_objects = self.queryset.filter(id=dialogue_id)

            dialogue_ser = app_serializers.DialogueSerializer(dialogue_objects[0])
            return JsonResponse({"dialogue": dialogue_ser.data}, status=status.HTTP_200_OK)

        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def add_emoji(self, request, *args, **kwargs):

        # Get All Parameters
        try:
            dialogue = request.data["dialogue"]
            mood = request.data["mood"]
        except:
            return JsonResponse({"error": "Bad Parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Check If Emotion is present
        dialogue_obj = app_models.Dialogues.objects.get(id=dialogue)
        emotion_objects = app_models.Emotion.objects.filter(mood=mood, dialogue=dialogue_obj)
        if len(emotion_objects) == 0:
            emotion_object = app_models.Emotion.objects.create(mood=mood, dialogue=dialogue_obj)
        else:
            emotion_object = emotion_objects[0]
            emotion_object.count = emotion_object.count + 1
            emotion_object.save()

        return JsonResponse({"message": "Mood Added"}, status=status.HTTP_200_OK)

    def remove_emoji(self, request, *args, **kwargs):

        # Get All Parameters
        try:
            dialogue = request.data["dialogue"]
            mood = request.data["mood"]
        except:
            return JsonResponse({"error": "Bad Parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Check If Emotion is present
        dialogue_obj = app_models.Dialogues.objects.get(id=dialogue)
        emotion_objects = app_models.Emotion.objects.filter(mood=mood, dialogue=dialogue_obj)
        if len(emotion_objects) == 0:
            return JsonResponse({"error": "Mood or Dialogue not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            emotion_object = emotion_objects[0]

            # Check emotion count
            count = emotion_object.count
            if count == 1:
                emotion_object.delete()
            else:
                emotion_object.count = emotion_object.count - 1
                emotion_object.save()

        return JsonResponse({"message": "Mood Removed"}, status=status.HTTP_200_OK)

    def get_year_range(self, request, *args, **kwargs):
        try:
            min_year = self.queryset.aggregate(Min('movie_year'))['movie_year__min']
            max_year = self.queryset.aggregate(Max('movie_year'))['movie_year__max']
            return JsonResponse({"min_year": min_year, "max_year": max_year}, status=status.HTTP_200_OK)
        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_counts(self, request, *args, **kwargs):
        try:
            dialogue_count = self.queryset.count()
            movies = self.queryset.order_by().values('movie_name').distinct()
            return JsonResponse({"dialogues": dialogue_count, "movies": len(movies)}, status=status.HTTP_200_OK)
        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DialogueSlackViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = app_models.Dialogues.objects.all()

    def get_dialogue(self, request, *args, **kwargs):

        try:
            dialogue_objects = self.queryset
            # if movie_name != '0':
            #     dialogue_objects = self.queryset.filter(movie_name__icontains=movie_name, movie_year=movie_year)
            # else:
            #     dialogue_objects = self.queryset.filter(movie_year__gte=year_min, movie_year__lte=year_max)
            #
            #     # Filter by tags
            #     if include_tags[0] != 0:
            #         dialogue_objects = dialogue_objects.filter(tag__in=include_tags)

            dialogue = random.choice(dialogue_objects)
            dialogue_ser = app_serializers.DialogueSerializer(dialogue)
            star_name = ""
            for each in dialogue_ser.data['star'].strip().split(" "):
                star_name += each.capitalize() + " "
            data = {
                "response_type": "in_channel",
                "attachments": [
                    {
                        "title": dialogue_ser.data['dialogue'],
                        "text": "{star}, {movie_name} ({movie_year})".format(star=star_name[:-1], movie_name=dialogue_ser.data['movie_name'], movie_year=dialogue_ser.data['movie_year']),
                        "color": "#E8E8E8",
                        "footer": "Posted using /filmyquote",
                    }
                ]
            }
            if dialogue_ser.data['star_image_url'].strip() != "":
                data["attachments"][0]["thumb_url"] = "https://image.tmdb.org/t/p/w500_and_h500_face/{poster}".format(poster=dialogue_ser.data['star_image_url'])
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            print str(e)
            return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

