

def define_env(env):
    "Hook function"

    from . import util
    util.define_env(env)

    from . import activity
    activity.define_env(env)

    from . import transitionelement
    transitionelement.define_env(env)

    from . import mitigation
    mitigation.define_env(env)
