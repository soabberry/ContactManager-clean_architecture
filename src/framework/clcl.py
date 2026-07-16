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

                print(result)

            elif choice == "2":

                contact_id = input("Contact ID: ")

                result = controller.get_contact(
                    GetContactInput(
                        contact_id=contact_id
                    )
                )

                print(result)

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
                    )
                )

                print(result)

            elif choice == "4":

                contact_id = input("Contact ID: ")

                result = controller.delete_contact(
                    DeleteContactInput(
                        contact_id=contact_id
                    )
                )

                print(result)

            elif choice == "5":

                result = controller.list_contacts(
                    ListContactsInput()
                )

                print(result)

            elif choice == "0":

                print("\nGoodbye!")
                break

            else:

                print("Invalid choice")

        except Exception as exc:

            print(f"Error: {exc}")