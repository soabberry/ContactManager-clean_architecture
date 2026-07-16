from dataclasses import dataclass
from typing import Optional

from src.entities.contact import Contact
from src.use_cases.interface.contact_repository import ContactRepository


@dataclass
class GetContactInput:
    contact_id: str

@dataclass
class GetContactOutput:
    contact: Optional[Contact]

class GetContactUseCase:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self, input_data: GetContactInput) -> GetContactOutput:
        contact = self.repository.find_by_id(input_data.contact_id)

        if contact is None:
            raise ValueError(f"Contact with ID '{input_data.contact_id}' not found")    

        return GetContactOutput(contact = contact)