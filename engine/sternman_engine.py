from .engine_interface import Engine


class SternmanEngine(Engine):
    """
    :param warning_light_is_on : Indication on the car either `True` or `False`(on or off).
    """
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        """Return `True` if the `warning_light_is_on` is on(True). Otherwise, `False`."""
        if self.warning_light_is_on:
            return True
        else:
            return False
