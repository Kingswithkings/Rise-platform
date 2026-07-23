class RiseError(Exception):
    """Base exception for expected RISE application errors."""


class EntityNotFoundError(RiseError):
    """Raised when a requested entity does not exist."""


class EntityConflictError(RiseError):
    """Raised when a request conflicts with an existing entity."""


class PermissionDeniedError(RiseError):
    """Raised when the current actor cannot perform an action."""
