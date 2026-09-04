from abc import ABC, abstractmethod

class observer(ABC):
    @abstractmethod
    def actualiser(self, sujet) -> None:
        pass