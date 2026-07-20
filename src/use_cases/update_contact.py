from src.entities.contact import Contact, ContactStatus
from src.use_cases.interface.contact_repository import ContactRepository
from dataclasses import dataclass

STATUS_CODE_MAP = {
    "1": ContactStatus.CREATED,
    "2": ContactStatus.ACTIVATED,
    "3": ContactStatus.BLOCKED,
}

@dataclass
class UpdateContactInput:
    contact_id: str
    name: str | None = None
    phone: str | None = None
    email: str | None = None
    status: str | None = None  # "1" (Created), "2" (Activated), "3" (Blocked)

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
        if input_data.name is None and input_data.phone is None and input_data.email is None and input_data.status is None:
            raise ValueError("At least one field (name, phone, email, status) must be provided for update")

        new_status = None
        if input_data.status is not None:
            new_status = STATUS_CODE_MAP.get(input_data.status)
            if new_status is None:
                raise ValueError(f"Invalid status code '{input_data.status}' (expected 1, 2, or 3)")

        success = contact.update(
            name=input_data.name,
            phone=input_data.phone,
            email=input_data.email,
            status=new_status,
        )
        if not success:
            raise ValueError("Update failed: one or more provided fields were invalid")

        updated_contact = self.repository.update(contact)
        return UpdateContactOutput(contact=updated_contact, message="Contact updated successfully")
