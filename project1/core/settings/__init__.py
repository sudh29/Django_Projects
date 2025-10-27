import os


def get_secret(secret_id, backup=None):
    return os.getenv(secret_id, backup)


# Keep at the end
if get_secret("PIPELINE") == "production":
    from .production import *  # noqa: F403
else:
    from .local import *  # noqa: F403
