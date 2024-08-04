from rest_framework.serializers import ValidationError

allowed_links = ['https://www.youtube.com/', 'https://www.rutube.com']


def validate_allowed_links(value):
    if any(link in value for link in allowed_links):
        return True
    else:
        raise ValidationError(f"Допустимо использовать только ссылки на ресурсы: {*allowed_links,}")
