from rest_framework import serializers
import backend.models as app_models


class TagSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        (tag_obj, created) = app_models.Tag.objects.get_or_create(**validated_data)
        return tag_obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = app_models.Tag
        fields = ('id', 'name')


class DialogueSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    emotions = serializers.SerializerMethodField()
    star_image_url = serializers.SerializerMethodField()

    def get_star_image_url(self, obj):
        return obj.poster

    def get_tags(self, obj):
        tag_mapping_objs = obj.tag_set.all()
        return list(map(lambda tag_mapping_obj: tag_mapping_obj.name, tag_mapping_objs))

    def get_emotions(self, obj):
        emotion_objs = app_models.Emotion.objects.filter(dialogue=obj)
        return_obj = [
            {
                'mood': 'heart_eyes',
                'count': 0
            },
            {
                'mood': 'joy',
                'count': 0
            },
            {
                'mood': 'flushed',
                'count': 0
            },
            {
                'mood': 'pensive',
                'count': 0
            },
            {
                'mood': 'rage',
                'count': 0
            }
        ]
        for each_obj in emotion_objs:
            for each_ret in return_obj:
                if each_ret['mood'] == each_obj.mood:
                    each_ret['count'] = each_obj.count

        return return_obj


    def create(self, validated_data):
        dialogue_obj= app_models.Dialogues.objects.create(**validated_data)
        return dialogue_obj

    def update(self, instance, validated_data):
        instance.dialogue = validated_data.get('dialogue', instance.dialogue)
        instance.movie_name = validated_data.get('movie_name', instance.movie_name)
        instance.movie_year = validated_data.get('movie_year', instance.movie_year)
        instance.star = validated_data.get('star', instance.star)
        instance.save()
        return instance

    class Meta:
        model = app_models.Dialogues
        fields = ('id', 'dialogue', 'movie_name', 'star', 'movie_year', 'tags', 'emotions', 'star_image_url')
