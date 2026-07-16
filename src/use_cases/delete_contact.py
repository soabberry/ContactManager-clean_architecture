from src.entities.contact import Contact
from src.use_cases.interface.contact_repository import ContactRepository
from dataclasses import dataclass

@dataclass
class DeleteContactInput:
    contact_id: str

@dataclass
class DeleteContactOutput:
    deleted: bool
    message: str

class DeleteContactUseCase:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self, input_data: DeleteContactInput) -> DeleteContactOutput:
        contact = self.repository.find_by_id(input_data.contact_id)
        if contact is None:
            raise ValueError(f"Contact with ID '{input_data.contact_id}' not found")    
        self.repository.delete(input_data.contact_id)
        return DeleteContactOutput(deleted=True, message=f"Contact deleted successfully")