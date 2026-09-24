import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "assets.json"

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


def load_assets():
    """Load assets from the JSON data file."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_assets(assets):
    """Save assets to the JSON data file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(assets, file, indent=4)


def get_required_input(prompt):
    """Read a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")


def get_choice(prompt, choices):
    """Read a value from a fixed list of choices."""
    while True:
        print(f"\n{prompt}")
        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice}")

        value = input("Enter choice: ").strip()

        if value.isdigit() and 1 <= int(value) <= len(choices):
            return choices[int(value) - 1]

        # Also accept the exact text value.
        for choice in choices:
            if value.lower() == choice.lower():
                return choice

        print("Error: Invalid choice. Please select a valid option.")


def validate_ip(ip_address):
    """Basic IPv4 validation."""
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 and str(int(part)) == part for part in parts)
    except ValueError:
        return False


def get_ip_address():
    while True:
        ip = get_required_input("IP Address: ")
        if validate_ip(ip):
            return ip
        print("Error: Enter a valid IPv4 address, e.g. 192.168.1.10")


def find_asset_index(assets, asset_id):
    for index, asset in enumerate(assets):
        if asset["asset_id"].lower() == asset_id.lower():
            return index
    return -1


def add_asset(assets):
    print("\n========== ADD ASSET ==========")
    asset_id = get_required_input("Asset ID: ")

    if find_asset_index(assets, asset_id) != -1:
        print("Error: Asset ID already exists.")
        return

    asset = {
        "asset_id": asset_id,
        "asset_name": get_required_input("Asset Name: "),
        "asset_type": get_choice("Asset Type", ASSET_TYPES),
        "ip_address": get_ip_address(),
        "operating_system": get_required_input("Operating System: "),
        "department": get_required_input("Department: "),
        "risk_level": get_choice("Risk Level", RISK_LEVELS),
        "security_status": get_choice("Security Status", SECURITY_STATUSES),
    }

    assets.append(asset)
    save_assets(assets)
    print("Asset added successfully!")


def display_asset(asset):
    print("-" * 41)
    print(f"Asset ID     : {asset['asset_id']}")
    print(f"Asset Name   : {asset['asset_name']}")
    print(f"Asset Type   : {asset['asset_type']}")
    print(f"IP Address   : {asset['ip_address']}")
    print(f"OS           : {asset['operating_system']}")
    print(f"Department   : {asset['department']}")
    print(f"Risk Level   : {asset['risk_level']}")
    print(f"Status       : {asset['security_status']}")


def display_assets(assets):
    print("\n=========================================")
    print("       CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No assets found.")
    else:
        for asset in assets:
            display_asset(asset)

    print("=========================================")
    print(f"Total Assets       : {len(assets)}")
    print(f"Critical Assets    : {count_by(assets, 'risk_level', 'Critical')}")
    print(f"High Risk Assets   : {count_by(assets, 'risk_level', 'High')}")
    print(f"Medium Risk Assets : {count_by(assets, 'risk_level', 'Medium')}")
    print(f"Low Risk Assets    : {count_by(assets, 'risk_level', 'Low')}")
    print(f"Vulnerable Assets  : {count_by(assets, 'security_status', 'Vulnerable')}")
    print("=========================================")


def search_asset(assets):
    print("\n========== SEARCH ASSET ==========")
    keyword = get_required_input("Enter Asset ID or Asset Name: ").lower()

    matches = [
        asset for asset in assets
        if keyword in asset["asset_id"].lower()
        or keyword in asset["asset_name"].lower()
    ]

    if not matches:
        print("No matching asset found.")
        return

    for asset in matches:
        display_asset(asset)


def update_asset(assets):
    print("\n========== UPDATE ASSET ==========")
    asset_id = get_required_input("Enter Asset ID to update: ")
    index = find_asset_index(assets, asset_id)

    if index == -1:
        print("Error: Asset not found.")
        return

    asset = assets[index]
    print("Press Enter to keep the existing value.")

    name = input(f"Asset Name [{asset['asset_name']}]: ").strip()
    if name:
        asset["asset_name"] = name

    print("\nChoose new Asset Type or keep current.")
    asset["asset_type"] = get_optional_choice(asset["asset_type"], ASSET_TYPES)

    while True:
        ip = input(f"IP Address [{asset['ip_address']}]: ").strip()
        if not ip:
            break
        if validate_ip(ip):
            asset["ip_address"] = ip
            break
        print("Error: Invalid IPv4 address.")

    os_name = input(f"Operating System [{asset['operating_system']}]: ").strip()
    if os_name:
        asset["operating_system"] = os_name

    department = input(f"Department [{asset['department']}]: ").strip()
    if department:
        asset["department"] = department

    asset["risk_level"] = get_optional_choice(asset["risk_level"], RISK_LEVELS)
    asset["security_status"] = get_optional_choice(
        asset["security_status"], SECURITY_STATUSES
    )

    save_assets(assets)
    print("Asset updated successfully!")


def get_optional_choice(current, choices):
    while True:
        print(f"Current value: {current}")
        print("0. Keep current")
        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice}")

        value = input("Enter choice: ").strip()

        if value == "":
            return current
        if value == "0":
            return current
        if value.isdigit() and 1 <= int(value) <= len(choices):
            return choices[int(value) - 1]

        print("Error: Invalid choice.")


def delete_asset(assets):
    print("\n========== DELETE ASSET ==========")
    asset_id = get_required_input("Enter Asset ID to delete: ")
    index = find_asset_index(assets, asset_id)

    if index == -1:
        print("Error: Asset not found.")
        return

    deleted = assets[index]
    confirm = input(
        f"Delete {deleted['asset_id']} - {deleted['asset_name']}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        assets.pop(index)
        save_assets(assets)
        print("Asset deleted successfully!")
    else:
        print("Delete operation cancelled.")


def count_by(assets, field, value):
    return sum(1 for asset in assets if asset.get(field) == value)


def security_summary(assets):
    print("\n========== SECURITY SUMMARY ==========")
    print(f"Total Assets : {len(assets)}")
    print(f"Secure       : {count_by(assets, 'security_status', 'Secure')}")
    print(f"Warning      : {count_by(assets, 'security_status', 'Warning')}")
    print(f"Vulnerable   : {count_by(assets, 'security_status', 'Vulnerable')}")
    print("\nRisk Levels")
    for level in RISK_LEVELS:
        print(f"{level:<10}: {count_by(assets, 'risk_level', level)}")
    print("=======================================")


def main():
    assets = load_assets()

    while True:
        print("\n=========================================")
        print("     CYBERSECURITY ASSET INVENTORY")
        print("=========================================")
        print("1. Add Asset")
        print("2. Display All Assets")
        print("3. Search Asset")
        print("4. Update Asset")
        print("5. Delete Asset")
        print("6. Security Summary")
        print("7. Exit")
        print("=========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            security_summary(assets)
        elif choice == "7":
            print("Thank you for using Cybersecurity Asset Inventory System.")
            break
        else:
            print("Error: Please enter a choice from 1 to 7.")


if __name__ == "__main__":
    main()
