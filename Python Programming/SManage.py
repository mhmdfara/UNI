import sqlite3

def initialize_database():
    connection = sqlite3.connect('settings.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    connection.commit()
    connection.close()

def save_setting():
    key = input("Enter the key for the setting: ").strip()
    value = input("Enter the value for the setting: ").strip()

    connection = sqlite3.connect('settings.db')
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', (key, value))
        connection.commit()
        print("Setting saved.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def display_all_settings():
    connection = sqlite3.connect('settings.db')
    cursor = connection.cursor()

    cursor.execute('SELECT key, value FROM settings')
    settings = cursor.fetchall()

    for key, value in settings:
        print(f'{key}: {value}')

    connection.close()

def display_setting():
    key = input("Enter the key for the setting you want to view: ").strip()

    connection = sqlite3.connect('settings.db')
    cursor = connection.cursor()

    cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
    result = cursor.fetchone()

    if result:
        print(f'{key}: {result[0]}')
    else:
        print("not exist.")

    connection.close()

def remove_setting():
    key = input("Enter the key for the setting you want to delete: ").strip()

    connection = sqlite3.connect('settings.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM settings WHERE key = ?', (key,))

    if cursor.rowcount > 0:
        print("deleted succefuly!")
    else:
        print("not exist.")

    connection.commit()
    connection.close()

def main():
    initialize_database()
    functionality_counter = 0

    while True:
        print("\nWhat would you like to do?\n1. Save setting\n2. Display all settings\n3. Display setting\n4. Remove setting\n5. Exit")

        choice = input("> ").strip()

        if choice == '1':
            save_setting()
            functionality_counter += 1
        elif choice == '2':
            display_all_settings()
            functionality_counter += 1
        elif choice == '3':
            display_setting()
            functionality_counter += 1
        elif choice == '4':
            remove_setting()
            functionality_counter += 1
        elif choice == '5':
            print("Bye Bye!")
            functionality_counter += 1
            break
        else:
            print("Not valid.")

    print(f"\nTotal functionality implemented: {functionality_counter} out of 5")

if __name__ == "__main__":
    main()
