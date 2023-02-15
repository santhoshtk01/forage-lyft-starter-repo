from abc import ABC, abstractmethod


class Engine(ABC):
    """Interface for Engine subclasses."""
    @abstractmethod
    def needs_service(self) -> bool:
        pass
