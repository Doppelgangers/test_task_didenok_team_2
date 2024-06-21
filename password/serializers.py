from rest_framework import serializers

from password.models import PasswordStorage


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordStorage
        fields = ('service_name', 'password')

    def save(self, **kwargs):
        service_name = self.validated_data.get('service_name')
        password = self.validated_data.get('password')

        # Попробуем найти запись по service_name
        try:
            password_storage = PasswordStorage.objects.get(service_name=service_name)
            # Если запись найдена, обновляем пароль
            password_storage.password = password
            password_storage.save()
        except PasswordStorage.DoesNotExist:
            # Если запись не найдена, создаем новую
            password_storage = PasswordStorage(service_name=service_name, password=password)
            password_storage.save()

        return password_storage


class PasswordReadSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='decoded_password')

    class Meta:
        model = PasswordStorage
        fields = ('service_name', 'password')


class SearchPasswordSerializer(serializers.Serializer):
    service_name = serializers.CharField(min_length=3, max_length=64)
