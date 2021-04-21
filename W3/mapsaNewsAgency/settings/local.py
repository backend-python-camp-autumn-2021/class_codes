from .base import *


DEBUG = True

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
print(MIDDLEWARE)

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': '/tmp/django.log',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         # 'django': {
#         #     'handlers': ['console'],
#         #     'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#         #     'propagate': False,
#         # },
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['file'],
#         }
#     }
# }

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
