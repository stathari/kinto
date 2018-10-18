"""Exceptions raised by storage backend.
"""


class BackendError(Exception):
    """A generic exception raised by storage on error.

    :param Exception original: the wrapped exception raised by underlying
        library.
    """

    def __init__(self, original=None, message=None, *args, **kwargs):
        self.original = original
        if message is None:
            message = "{}: {}".format(original.__class__.__name__, original)
        super().__init__(message, *args, **kwargs)


class ObjectNotFoundError(Exception):
    """An exception raised when a specific object could not be found.

    """

    pass


class IntegrityError(BackendError):
    pass


class UnicityError(IntegrityError):
    """An exception raised on unicity constraint violation.

    Raised by storage backend when the creation or the modification of a
    object violates the unicity constraints defined by the resource.

    """

    def __init__(self, field, object, *args, **kwargs):
        self.field = field
        self.object = object
        self.msg = "{} is not unique: {}".format(field, object)
        super().__init__(*args, **kwargs)
