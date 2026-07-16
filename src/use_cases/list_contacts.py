from src.entities.contact import Contact, ContactStatus
from src.use_cases.interface.contact_repository import ContactRepository
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ListContactsInput:
    status_filter: Optional[ContactStatus] = None

@dataclass
class ListContactsOutput:
    contacts: List[Contact] = field(default_factory=list)
    total: int = 0

    def __post_init__(self):
        self.total = len(self.contacts)


class ListContactsUseCase:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self, input_data: ListContactsInput) -> ListContactsOutput:
        if input_data.status_filter is not None:
            contacts = self.repository.find_by_status(input_data.status_filter)
        else:
            contacts = self.repository.find_all()

        contacts_sorted = sorted(contacts, key=lambda t: t.created_at, reverse=True)

        return ListContactsOutput(contacts=contacts_sorted)