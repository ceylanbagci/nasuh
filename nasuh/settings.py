from .environment import *

try:
    if ENVIRONMENT == "PRODUCTION":
        from nasuh.environments.production import *
    elif ENVIRONMENT == "DEVELOPMENT":
        from nasuh.environments.development import *

    print("{} settings loaded..".format(ENVIRONMENT))
except ImportError as e:
    print("{} settings could not loaded..".format(ENVIRONMENT))
    print(e)
    pass
