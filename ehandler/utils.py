import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_event_code_generator(instance):
    event_new_code = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(ecode=event_new_code).exists()
    if qs_exists:
        return unique_event_code_generator(instance)
    return event_new_code
