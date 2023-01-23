from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.CharField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_superuser = serializers.BooleanField(read_only=True)
    is_employee = serializers.BooleanField(default=False)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"] == True:
            validated_data["is_employee"] = True
            validated_data["is_superuser"] = True

        user = User.objects.create_user(**validated_data)
        return user
