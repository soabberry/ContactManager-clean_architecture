#IMPORTS
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import re
import uuid

#Method to get the time
def _now() -> datetime:
    return datetime.now(timezone.utc)

#Class to create different states of a contact
class ContactStatus(str, Enum):
    CREATED = "created"
    ACTIVATED = "activated"
    BLOCKED = "blocked"


@dataclass
class Contact:
    name: str
    phone: str
    email: str
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: ContactStatus = field(default=ContactStatus.CREATED)
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)
    def __post_init__(self):

        if not self.name or not self.name.strip():
            raise ValueError("Contact name cannot be empty")
        self.name = self.name.strip()

        if not self.phone or not self.phone.strip():
            raise ValueError("Contact phone cannot be empty")
        self.phone = self.phone.strip()
        if not self.phone.isdigit():
            raise ValueError("Invalid phone number")

        if not self.email or not self.email.strip():
            raise ValueError("Contact email cannot be empty")
        self.email = self.email.strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Invalid email address")
        

    def activate(self) -> bool:
        if self.status != ContactStatus.CREATED:
            return False
        self.status = ContactStatus.ACTIVATED
        self.updated_at = _now()
        return True

    def block(self) -> bool:
        if self.status == ContactStatus.BLOCKED:
            return False
        self.status = ContactStatus.BLOCKED
        self.updated_at = _now()
        return True

    def update(self, name: str | None = None, phone: str | None = None, email: str | None = None, status: "ContactStatus | None" = None) -> bool:
        if name is not None: 
            if not name.strip():
                return False
            self.name = name.strip()

        if phone is not None:
            phone = phone.strip()
            if not phone.isdigit():
                return False
            self.phone = phone

        if email is not None:
            email = email.strip()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return False
            self.email = email

        if status is not None:
            if not isinstance(status, ContactStatus):
                try:
                    status = ContactStatus(status)
                except ValueError:
                    return False
            self.status = status

        self.updated_at = _now()
        return True
    
    def is_created(self) -> bool:
        return self.status == ContactStatus.CREATED

    def is_activated(self) -> bool:
        return self.status == ContactStatus.ACTIVATED

    def is_blocked(self) -> bool:
        return self.status == ContactStatus.BLOCKED