from src.entities.contact import Contact
from src.use_cases.interface.contact_repository import ContactRepository
from dataclasses import dataclass

@dataclass
class UpdateContactInput:
    contact_id: str
    name: str | None = None
    phone: str | None = None
    email: str | None = None

@dataclass
class UpdateContactOutput:
    contact: Contact
    message: str


class UpdateContactUseCase:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self, input_data: UpdateContactInput) -> UpdateContactOutput:   
        contact = self.repository.find_by_id(input_data.contact_id)
        if contact is None:
            raise ValueError(f"Contact with ID '{input_data.contact_id}' not found")
        if not input_data.name:
            return UpdateContactOutput(contact = None, status = False, message="Name is required")
        if not input_data.phone:
            return UpdateContactOutput(contact = None, status = False, message="Phone is required")
        if not input_data.email:
            return UpdateContactOutput(contact = None, status = False, message="Email is required")
        
        contact.update(
            name=input_data.name,
            phone=input_data.phone,
            email=input_data.email
        )
        updated_contact = self.repository.update(contact)
        return UpdateContactOutput(contact=updated_contact, message="Contact updated successfully")