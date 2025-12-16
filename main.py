import json

# כאן נשמור את כל הפתקים
notes = []

# שם הקובץ
FILE_NAME = "notes.json"


# טעינת פתקים מהקובץ (אם קיים)
def load_notes():
    global notes
    try:
        file = open(FILE_NAME, "r")
        notes = json.load(file)
        file.close()
    except:
        notes = []


# שמירת פתקים לקובץ
def save_notes():
    file = open(FILE_NAME, "w")
    json.dump(notes, file, indent=4)
    file.close()


# הוספת פתק חדש
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    tags_input = input("Enter tags separated by comma: ")
    date = input("Enter date (YYYY-MM-DD): ")

    tags = tags_input.split(",")

    note = {
        "title": title,
        "content": content,
        "tags": tags,
        "date": date
    }

    notes.append(note)
    save_notes()
    print("Note added successfully")


# הצגת כל הפתקים
def list_notes():
    if len(notes) == 0:
        print("No notes found")
        return

    for i in range(len(notes)):
        print("-----")
        print("Note number:", i + 1)
        print("Title:", notes[i]["title"])
        print("Content:", notes[i]["content"])
        print("Tags:", notes[i]["tags"])
        print("Date:", notes[i]["date"])


# חיפוש פתק לפי מילה
def search_notes():
    keyword = input("Enter word to search: ")

    found = False
    for note in notes:
        if keyword in note["title"] or keyword in note["content"]:
            print("-----")
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Tags:", note["tags"])
            print("Date:", note["date"])
            found = True

    if not found:
        print("No matching notes found")


# מחיקת פתק
def delete_note():
    list_notes()
    number = int(input("Enter note number to delete: "))

    if number > 0 and number <= len(notes):
        notes.pop(number - 1)
        save_notes()
        print("Note deleted")
    else:
        print("Invalid number")


# תפריט ראשי
def main():
    load_notes()

    while True:
        print("\nMenu:")
        print("1 - Add note")
        print("2 - List notes")
        print("3 - Search notes")
        print("4 - Delete note")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

main()
