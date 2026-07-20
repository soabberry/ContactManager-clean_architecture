from src.interface_adapters.controllers.contact_controller import ContactController
from src.interface_adapters.repositories.inMemoryContact import InMemoryContactRepository
from src.use_cases.create_contact import CreateContactInput
from src.use_cases.get_contact import GetContactInput
from src.use_cases.delete_contact import DeleteContactInput
from src.use_cases.update_contact import UpdateContactInput
from src.use_cases.list_contacts import ListContactsInput


class Colors:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    CYAN = "\033[36m"


def banner() -> None:
    print("\n" + "=" * 50)
    print("     CLEAN ARCHITECTURE CONTACT MANAGER")
    print("=" * 50 + "\n")


def show_result(result: dict) -> None:
    """Prints controller results with real line breaks instead of a raw dict repr."""

    if "message" in result:
        print(result["message"])

    if "deleted" in result:
        print("Deleted" if result["deleted"] else "Not deleted")

    if result.get("contact"):
        print()
        print(result["contact"])

    if "contacts" in result:
        contacts = result["contacts"]
        total = result.get("total", len(contacts))
        print(f"\nTotal: {total}\n")
        for i, contact in enumerate(contacts, start=1):
            print(f"[{i}]")
            print(contact)
            print()


def run_cli() -> None:

    repository = InMemoryContactRepository()
    controller = ContactController(repository)

    while True:

        banner()

        print("1. Create Contact")
        print("2. Get Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("0. Exit")

        choice = input("\nChoice: ").strip()

        try:

            if choice == "1":

                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")

                result = controller.create_contact(
                    CreateContactInput(
                        name=name,
                        phone=phone,
                        email=email,
                    )
                )

                show_result(result)

            elif choice == "2":

                contact_id = input("Contact ID: ")

                result = controller.get_contact(
                    GetContactInput(
                        contact_id=contact_id
                    )
                )

                show_result(result)

            elif choice == "3":

                contact_id = input("Contact ID: ")

                name = input("New name (blank to skip): ")
                phone = input("New phone (blank to skip): ")
                email = input("New email (blank to skip): ")

                result = controller.update_contact(
                    UpdateContactInput(
                        contact_id=contact_id,
                        name=name or None,
                        phone=phone or None,
                        email=email or None,
                        status=input("New status (1: Created, 2: Activated, 3: Blocked, blank to skip): ") or None
                    )
                )

                show_result(result)

            elif choice == "4":

                contact_id = input("Contact ID: ")

                result = controller.delete_contact(
                    DeleteContactInput(
                        contact_id=contact_id
                    )
                )

                show_result(result)

            elif choice == "5":

                result = controller.list_contacts(
                    ListContactsInput()
                )

                show_result(result)

            elif choice == "0":

                print("\nGoodbye!")
                break

            else:

                print("Invalid choice")

        except Exception as exc:

            print(f"Error: {exc}")