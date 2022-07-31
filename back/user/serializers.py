from rest_framework  import serializers
from .models import User, Shop



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 
                'username',
                'created',
                )


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name_shop', 
                    'unp',
                    'user',
                    )


class RegisterSerializer(serializers.Serializer):
    # model = User
    # username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_submit = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = [
            "email",
            "password",
            "password_submit",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_submit"]:
            raise serializers.ValidationError("Passwords unmatched")
        return super().validate(attrs)

    def create(self, validated_data, **kwargs):
        validated_data.pop("password_submit")
        print(validated_data)
        return User.objects.create_user(**validated_data)