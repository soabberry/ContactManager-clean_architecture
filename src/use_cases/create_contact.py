from src.entities.contact import Contact
from src.use_cases.interface.contact_repository import ContactRepository
from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateContactInput:
    name: str
    phone: str
    email: str

@dataclass
class CreateContactOutput:
    contact : Optional[Contact]
    message : str = ""

class CreateContactUseCase:

    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self, input_data: CreateContactInput) -> CreateContactOutput:
        if not input_data.name:
            return CreateContactOutput(contact = None, message="Name is required")
        if not input_data.phone:
            return CreateContactOutput(contact = None, message="Phone is required")
        if not input_data.email:
            return CreateContactOutput(contact = None, message="Email is required")
        
        contact = Contact(name = input_data.name, phone = input_data.phone, email = input_data.email)
        created_contact = self.repository.create(contact)

        return CreateContactOutput(contact = created_contact, message="Contact created succesfully")