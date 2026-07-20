from typing import Any

from src.use_cases.interface.contact_repository import ContactRepository
from src.use_cases.create_contact import CreateContactUseCase, CreateContactInput
from src.use_cases.update_contact import UpdateContactUseCase, UpdateContactInput
from src.use_cases.delete_contact import DeleteContactUseCase, DeleteContactInput
from src.use_cases.get_contact import GetContactUseCase, GetContactInput
from src.use_cases.list_contacts import ListContactsUseCase, ListContactsInput
from src.interface_adapters.presenters.contact_presenter import ContactPresenter

class ContactController:
    def __init__(self, contact : ContactRepository) -> None:
    
        self.create_contact_use_case = CreateContactUseCase(contact)
        self.update_contact_use_case = UpdateContactUseCase(contact)
        self.delete_contact_use_case = DeleteContactUseCase(contact)
        self.get_contact_use_case = GetContactUseCase(contact)
        self.list_contacts_use_case = ListContactsUseCase(contact)

    def create_contact(self, input_data: CreateContactInput) -> dict[str, Any]:
        output = self.create_contact_use_case.execute(input_data)
        contact_view = ContactPresenter.to_cli_detail(output.contact) if output.contact else None
        return {"message": output.message, "contact": contact_view}
    
    def update_contact(self, input_data: UpdateContactInput) -> dict[str, Any]:
        output = self.update_contact_use_case.execute(input_data)
        contact_view = ContactPresenter.to_cli_detail(output.contact) if output.contact else None
        return {"message": output.message, "contact": contact_view}

    def delete_contact(self, input_data: DeleteContactInput) -> dict[str, Any]:
        result = self.delete_contact_use_case.execute(input_data)
        return {"deleted": result.deleted, "message": result.message}
    
    def get_contact(self, input_data: GetContactInput) -> dict[str, Any]:
        output = self.get_contact_use_case.execute(input_data)
        return {"contact": ContactPresenter.to_cli_detail(output.contact)}
    
    def list_contacts(self, input_data: ListContactsInput) -> dict[str, Any]:
        output = self.list_contacts_use_case.execute(input_data)
        return {"contacts": [ContactPresenter.to_cli_detail(contact) for contact in output.contacts], "total": output.total}
