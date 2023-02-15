from abc import ABC, abstractmethod


class Battery(ABC):
    """Interface for Battery subclasses."""
    @abstractmethod
    def needs_service(self) -> bool:
        pass
