import json


def load_users(file_path='users.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_users(users, file_path='users.json'):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)


def create_user(users):
    user_id = input("Enter user ID: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    new_user = {'id': user_id, 'name': name, 'email': email, 'age': age}
    users.append(new_user)
    save_users(users)
    print("User created successfully.")


def read_user(users, user_id=None):
    if user_id:
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            print(user)
        else:
            print("User not found.")
    else:
        for user in users:
            print(user)


def update_user(users):
    user_id = input("Enter the ID of the user to update: ")
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user['name'] = input(f"Enter new name (current: {user['name']}): ")
        user['email'] = input(f"Enter new email (current: {user['email']}): ")
        user['age'] = int(input(f"Enter new age (current: {user['age']}): "))
        save_users(users)
        print("User updated successfully.")
    else:
        print("User not found.")


def delete_user(users):
    user_id = input("Enter the ID of the user to delete: ")
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        users.remove(user)
        save_users(users)
        print("User deleted successfully.")
    else:
        print("User not found.")


def main():
    users = load_users()

    while True:
        print("\nChoose an option:")
        print("1. Create user")
        print("2. Display all users")
        print("3. Retrieve user by ID")
        print("4. Update user")
        print("5. Delete user")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_user(users)
        elif choice == '2':
            read_user(users)
        elif choice == '3':
            user_id = input("Enter user ID to retrieve: ")
            read_user(users, user_id)
        elif choice == '4':
            update_user(users)
        elif choice == '5':
            delete_user(users)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
