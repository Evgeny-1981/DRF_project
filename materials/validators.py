from rest_framework.serializers import ValidationError

# Создаем список разрешенных рессурсов
allowed_links = [
    "https://www.youtube.com/",
    "https://youtube.com/",
    "https://www.rutube.com",
    "https://rutube.com",
]


def validate_allowed_links(value):
    """Метод проверяет введенную ссылку на соответсвие тем, что заданы в спмске разрешенных ссылок"""
    if any(link in value for link in allowed_links):
        return True
    else:
        raise ValidationError(
            f"Допустимо использовать только ссылки на следующие ресурсы: {*allowed_links,}"
        )
