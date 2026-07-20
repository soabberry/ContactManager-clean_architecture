from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.contact import Contact, ContactStatus

#Abstract class
class ContactRepository(ABC):

    @abstractmethod
    def create(self, contact: Contact) -> Contact:
        ... #Abstract method for creation

    @abstractmethod
    def update(self, contact: Contact) -> Contact:
        ... #Abstract method for updating

    @abstractmethod
    def delete(self, contact_id: str) -> bool:
        ... #Abstract method for deleting

    @abstractmethod
    def find_by_id(self, contact_id: str) -> Optional[Contact]:
        ... #Abstract method for finding by id

    @abstractmethod
    def find_all(self) ->List[Contact]:
        ... #Abstract method for finding all

    @abstractmethod
    def list_by_status(self, status: ContactStatus) -> List[Contact]:
        ... #Abstract method for listing by status