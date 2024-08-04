from rest_framework.serializers import ValidationError

allowed_links = ['https://www.youtube.com/', 'https://www.rutube.com']


def validate_allowed_links(value):
    if any(link in value for link in allowed_links):
        return True
    else:
        raise ValidationError(f"В качестве ссылки допустимо использовать только ссылки на: {*allowed_links,}")