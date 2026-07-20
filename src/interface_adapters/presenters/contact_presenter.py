from src.entities.contact import Contact

class ContactPresenter:

    @staticmethod
    def to_cli_detail(contact: Contact) -> str:
        lines = [
            f"  ID          : {contact.id}",
            f"  Name        : {contact.name}",
            f"  Phone       : {contact.phone}",
            f"  Email       : {contact.email}",
            f"  Status      : {contact.status.value}",
            f"  Created     : {contact.created_at}",
            f"  Updated     : {contact.updated_at}",
        ]
        return "\n".join(lines)
