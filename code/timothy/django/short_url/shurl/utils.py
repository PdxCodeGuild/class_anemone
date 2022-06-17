# Storing my randomizer

from django.conf import settings
from random import choice
from string import ascii_letters, digits

size = getattr(settings, "MAXIMUM_URL_CHARS", 7)

available_chars = ascii_letters + digits

def random_code(chars=available_chars):
    return "".join(
        [choice(chars) for _ in range(size)]
    )

def shortener(model_instance):
    code = random_code()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=code).exists():
        return shortener(model_instance)

    return code