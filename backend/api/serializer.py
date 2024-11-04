#Serialization is the process of converting complex data (like model instances) into simpler, standard formats (such as JSON or XML) that can be easily transmitted over the web or saved. Deserializer is the opposite.
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauths.models import User, Profile
from django.contrib.auth.password_validation import validate_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password = serializers.CharField(write_only=True, required=True)
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password','re_password']

    def validate(self, attr):
        if attr['password'] != attr['re_password']:
            raise serializers.ValidationError({'password': 'password fields did not match'})
        return attr
    
    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
        )
        #due to more complex oeration, so the following lines is operated outsid the objects.create()
        email_username = user.email.split('@')[0]
        user.username = email_username
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
# metadata: information that describes or provides additional context about data or objects, but it is not the actual content itself.
    class Meta:
        model = User
        #fileds will pass, so no sensitive fileds should be passed, eg opt 
        fileds = '__all__'

class ProfileSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Profile
        filed = '__all__'