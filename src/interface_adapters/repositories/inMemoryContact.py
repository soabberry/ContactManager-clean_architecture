import copy
from typing import Dict, List, Optional

from src.entities.contact import Contact, ContactStatus
from src.use_cases.interface.contact_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):

    def __init__(self, ) -> None:
        self._store: Dict[str, Contact] = {}

    def create(self, contact: Contact) -> Contact:
        if contact.id in self._store:
            raise ValueError(f"Contact with id '{contact.id}' already exists")
        self._store[contact.id] = copy.deepcopy(contact)
        return copy.deepcopy(self._store[contact.id])

    def find_by_id(self, contact_id: str) -> Optional[Contact]:
        contact = self._store.get(contact_id)
        return copy.deepcopy(contact) if contact else None

    def find_all(self) -> List[Contact]:
        return [copy.deepcopy(t) for t in self._store.values()]

    def list_by_status(self, status: ContactStatus) -> List[Contact]:
        return [copy.deepcopy(c) for c in self._store.values() if c.status == status]

    def update(self, contact: Contact) -> Contact:
        if contact.id not in self._store:
            raise ValueError(f"contact with id '{contact.id}' not found, cannot update")
        self._store[contact.id] = copy.deepcopy(contact)
        return copy.deepcopy(self._store[contact.id])

    def delete(self, contact_id: str) -> bool:
        if contact_id not in self._store:
            return False
        del self._store[contact_id]
        return True