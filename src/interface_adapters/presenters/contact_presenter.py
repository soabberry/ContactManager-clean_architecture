from typing import Any, Dict, List
from src.entities.contact import Contact

class ContactPresenter:

    @staticmethod
    def to_dict(contact: Contact) -> Dict[str, Any]:

        return {
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
            "status" : contact.status.value,
            "created_at" : contact.created_at.isoformat(),
            "updated_at": contact.updated_at.isoformat() if contact.updated_at else None,
        }

    @staticmethod
    def to_list(contacts: List[Contact]) -> List[Dict[str, Any]]:
        return [ContactPresenter.to_dict(t) for t in contacts]