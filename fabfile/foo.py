import fabric.api

# from .bar import baz as yes_work
from .bar import baz as no_work


@fabric.api.task
def baz():
    """
    Calls foo.baz
    """
    print("calling foo.baz")

