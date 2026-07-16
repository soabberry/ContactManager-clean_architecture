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

    def create_contact(self, input_data: CreateContactInput) -> dict[str, any]:
        output = self.create_contact_use_case.execute(input_data)
        return {"message": output.message, "contact": ContactPresenter.to_dict(output.contact)}
    
    def update_contact(self, input_data: UpdateContactInput) -> dict[str, any]:
        output = self.update_contact_use_case.execute(input_data)
        return {"message": output.message, "contact": ContactPresenter.to_dict(output.contact)}

    def delete_contact(self, input_data: DeleteContactInput) -> dict[str, any]:
        result = self.delete_contact_use_case.execute(input_data)
        return {"deleted": result.deleted, "message": result.message}
    
    def get_contact(self, input_data: GetContactInput) -> dict[str, any]:
        output = self.get_contact_use_case.execute(input_data)
        return ContactPresenter.to_dict(output.contact)
    
    def list_contacts(self, input_data: ListContactsInput) -> dict[str, any]:
        contacts = self.list_contacts_use_case.execute(input_data)
        return {"contacts": [ContactPresenter.to_dict(contact) for contact in contacts]}
    
