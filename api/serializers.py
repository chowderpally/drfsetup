from rest_framework import serializers


class StringSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    val = serializers.CharField(min_length=9)

    def create(self, validated_data):
        return StringSerializer(**validated_data)
