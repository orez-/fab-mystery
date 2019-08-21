import fabric.api


@fabric.api.task
def baz():
    """
    Calls bar.baz
    """
    print("calling bar.baz")
