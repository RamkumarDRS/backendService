from rest_framework import serializers

from endpoints.models import ServiceProvider


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = "__all__"

    # service_type = serializers.IntegerField()
    # service_Provider = serializers.CharField()
    # key = serializers.CharField()
    # api1 = serializers.CharField()
    # api2 = serializers.CharField()
    # status = serializers.BooleanField()
    #
    # # def to_representation(self, instance):
    # #     representation = super().to_representation(instance)
    # #     return [ list(representation.values())]
    #
    # def create(self, validated_data):
    #     return ServiceProvider.objects.create(**validated_data)
    #
    #
    #
    #
    #
    # def update(self, instance, validated_data):
    #     instance.service_type = validated_data.get('service_type', instance.service_type)
    #     instance.service_Provider  = validated_data.get('service_Provider', instance.service_Provider)
    #     instance.key = validated_data.get('key', instance.key)
    #     instance.api1 = validated_data.get('api1', instance.api1)
    #     instance.api2 = validated_data.get('api2', instance.api2)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance

