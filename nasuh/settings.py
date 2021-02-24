from .environment import *

try:
    if ENVIRONMENT == "PRODUCTION":
        from .environments.production import *
    elif ENVIRONMENT == "DEVELOPMENT":
        from .environments.development import *
    elif ENVIRONMENT == "DEVELOPMENT_YAZU":
        from .environments.development_yazu import *
    elif ENVIRONMENT == "TEST":
        from .environments.test import *

    print("{} settings loaded..".format(ENVIRONMENT))
except ImportError as e:
    print("{} settings could not loaded..".format(ENVIRONMENT))
    print(e)
    pass
