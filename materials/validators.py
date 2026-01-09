import re
from rest_framework.serializers import ValidationError


def validate_link_video(value):
    """Проверка, что ссылка на видео начинается с youtube.com/"""

    reg = re.compile(r"^youtube\.com/.*")
    match = re.match(reg, value, flags=0)
    if not match:
        raise ValidationError("Link is not ok")
