class InvalidPriceError(Exception):
    """Raised when course price is zero or negative."""
    pass


class InvalidDurationError(Exception):
    """Raised when course duration is zero or negative."""
    pass


class InvalidDiscountError(Exception):
    """Raised when discount percentage is invalid."""
    pass