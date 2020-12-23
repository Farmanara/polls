from rest_framework import serializers
from polls.models import Question,Choice



class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Choice
        fields=['id','choice_text']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choice_set = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model=Question
        fields=["url",'id','question_text','pub_date', "choice_set"]


class ChoiceResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Choice
        fields=['id','choice_text', "votes"]

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    choice_set = ChoiceResultSerializer(many=True, read_only=True)
    class Meta:
        model=Question
        fields=["url",'id','question_text','pub_date', "choice_set"]

class VoteSerializer(serializers.Serializer):
    choice = serializers.IntegerField()



