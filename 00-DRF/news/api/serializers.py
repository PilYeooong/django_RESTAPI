from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist, JobOffer
    


 

class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer(read_only=True)
    
    class Meta:
        model = Article
        exclude = ("id",) # 정의한 부분은 빼서나옴
        # fields = "__all__" # we want all the fields of our model
        # fields = ("title", "description", "body") # 골라서 할때
    
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """ check thtat description and title are different """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another.")
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 chars long")
        return value
    
    
class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")
    # articles = ArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Journalist
        fields = "__all__"

class JobOfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobOffer
        fields = "__all__"
        
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)  # 아이디는 보통 수정안하기때문에 
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get("author", instance.author)
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.body = validated_data.get("body", instance.body)
#         instance.location = validated_data.get("location", instance.location)
#         instance.publication_date = validated_data.get("publication_date", instance.publication_data)
#         instance.active = validated_data.get("active", instance.active)
        
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         """ check thtat description and title are different """
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be different from one another.")
#         return data

#     def validate_title(self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError("The title has to be at least 60 chars long")
#         return value
