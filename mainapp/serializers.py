from rest_framework import serializers
from .models import Review, Post, Ship, Box


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'updated_at')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     print(instance)
    #     instance.width = validated_data.get('width', instance.width)
    #     instance.depth = validated_data.get('depth', instance.depth)
    #     instance.height = validated_data.get('height', instance.height)
    #     instance.weight = validated_data.get('weight', instance.weight)
    #     instance.underWaterVolume = validated_data.get('underWaterVolume', instance.underWaterVolume)
    #     instance.globalShipPosition = validated_data.get('globalShipPosition', instance.globalShipPosition)
    #     instance.shipAttitude = validated_data.get('shipAttitude', instance.shipAttitude)
    #     instance.localCOG = validated_data.get('localCOG', instance.localCOG)
    #     instance.globalCOG = validated_data.get('globalCOG', instance.globalCOG)
    #     instance.localCOB = validated_data.get('localCOB', instance.localCOB)
    #     instance.globalCOB = validated_data.get('globalCOB', instance.globalCOB)
    #     instance.draft = validated_data.get('draft', instance.draft)
    #     instance.heel = validated_data.get('heel', instance.heel)
    #     instance.trim = validated_data.get('trim', instance.trim)
    #     return instance


