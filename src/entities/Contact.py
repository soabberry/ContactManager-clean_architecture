from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import re
import uuid

#Method for getting the current UTC time
def _now() -> datetime:
    return datetime.now(timezone.utc)

#This class defines the possible states of a Contact in our business domain.
class ContactStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

#This class represents a Contact entity with attributes and methods to manage its state and validate its data.
@dataclass
class Contact:
    #Attributes of the Contact entity
    name : str
    phone : str
    email : str
    id : str = field(default_factory=lambda: str(uuid.uuid4())) #Id is generated automatically using UUID
    status : ContactStatus = field(default=ContactStatus.PENDING) #Default status is PENDING
    created_at : datetime = field(default_factory=_now) #Creation timestamp is set to current

    def __post_init__(self) -> None:
        
        #Validation of the attribute 'name' after initialization 
        if not self.name or not self.name.strip():
            raise ValueError("Contact name cannot be empty")
        self.name = self.name.strip()

        #Validation of the attribute 'phone' after initialization 
        if not self.phone or not self.phone.strip():
            raise ValueError("Contact phone cannot be empty")
        if not self.phone.isdigit() or len(self.phone) < 10 or len(self.phone) > 15:
            raise ValueError("Enter a valid phone number")
        self.phone = self.phone.strip()

        #Validation of the attribute 'email' after initialization 
        if not self.email or not self.email.strip():
            raise ValueError("Contact email cannot be empty")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Enter a valid email address") 
        self.email = self.email.strip()

    def start(self) -> None:
        if self.status != ContactStatus.PENDING:
            raise ValueError(
                f"Cannot start a contact that is '{self.status}'. "
                "Only PENDING contacts can be started."
            )
        self.status = ContactStatus.IN_PROGRESS
        self.updated_at = _now()

    def complete(self) -> None:
        if self.status == ContactStatus.COMPLETED:
            raise ValueError("Contact is already completed.")
        self.status = ContactStatus.COMPLETED
        self.updated_at = _now()

    def update(self, name: str = None, phone: str = None, email: str = None) -> None:
        if name is not None:
            if not name.strip():
                raise ValueError("Contact name cannot be empty")
            self.name = name.strip()

        if phone is not None:
            if not phone.strip():
                raise ValueError("Contact phone cannot be empty")
            if not self.phone.isdigit() or len(self.phone) < 10 or len(self.phone) > 15:
                raise ValueError("Enter a valid phone number")
            self.phone = phone.strip()

        if email is not None:
            if not email.strip():
                raise ValueError("Contact email cannot be empty")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                raise ValueError("Enter a valid email address")
            self.email = email.strip()

        self.updated_at = _now()

    def is_completed(self) -> bool:
        return self.status == ContactStatus.COMPLETED

    def is_pending(self) -> bool:
        return self.status == ContactStatus.PENDING

    def is_in_progress(self) -> bool:
        return self.status == ContactStatus.IN_PROGRESS


    
