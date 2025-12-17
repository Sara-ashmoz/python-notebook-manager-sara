import json
from datetime import datetime

FILE_NAME = "notes.json"
notes = []


# ---------- Load notes from file ----------
def load_notes():
    global notes
    try:
        f = open(FILE_NAME, "r")
        notes = json.load(f)
        f.close()
        print("Notes loaded.")
    except:
        notes = []
        print("No saved notes found. Starting with empty list.")


# ---------- Save notes to file ----------
def save_notes():
    f = open(FILE_NAME, "w")
    json.dump(notes, f, indent=2)
    f.close()
    print("Notes saved.")


# ---------- 1) Add a new note ----------
def add_note():
    title = input("Title: ")
    content = input("Content: ")
    tags_input = input("Tags (separated): ")

    tags = tags_input.split(",")
    
    date_now = datetime.now().strftime("%Y-%m-%d")

    note = {
        "title": title,
        "content": content,
        "tags": tags,
        "date": date_now
    }

    notes.append(note)
    print("Note added.")



# ---------- 2) List all notes ----------
def list_notes():
    if len(notes) == 0:
        print("No notes found.")
        return

    for i in range(len(notes)):
        n = notes[i]
        print("-----")
        print("Index:", i + 1)  # show 1,2,3...
        print("Title:", n["title"])
        print("Content:", n["content"])
        print("Tags:", n["tags"])
        print("Date:", n["date"])


# ---------- 3) Search notes by keyword ----------
def search_notes():
    keyword = input("Enter keyword: ")
    found = False

    for i in range(len(notes)):
        n = notes[i]
        if keyword in n["title"] or keyword in n["content"]:
            found = True
            print("-----")
            print("Index:", i + 1)  # show 1,2,3...
            print("Title:", n["title"])
            print("Content:", n["content"])
            print("Tags:", n["tags"])
            print("Date:", n["date"])

    if not found:
        print("No matching notes found.")


# ---------- 4) Filter notes by tag ----------
def filter_by_tag():
    tag = input("Enter tag: ")
    found = False

    for i in range(len(notes)):
        n = notes[i]
        if tag in n["tags"]:
            found = True
            print("-----")
            print("Index:", i + 1)  # show 1,2,3...
            print("Title:", n["title"])
            print("Content:", n["content"])
            print("Tags:", n["tags"])
            print("Date:", n["date"])

    if not found:
        print("No notes with this tag.")


# ---------- 5) Edit an existing note ----------
def edit_note():
    list_notes()
    index = input("Enter index to edit: ")

    try:
        index = int(index) - 1  # convert 1-based to 0-based
    except:
        print("Invalid index.")
        return

    if index < 0 or index >= len(notes):
        print("Index out of range.")
        return

    new_title = input("New title: ")
    new_content = input("New content: ")
    new_tags = input("New tags (comma separated): ")
    new_date = datetime.now().strftime("%Y-%m-%d")

    notes[index]["title"] = new_title
    notes[index]["content"] = new_content
    notes[index]["tags"] = new_tags.split(",")
    notes[index]["date"] = new_date

    print("Note updated.")


# ---------- 6) Delete a note ----------
def delete_note():
    list_notes()
    index = input("Enter index to delete: ")

    try:
        index = int(index) - 1  # convert 1-based to 0-based
    except:
        print("Invalid index.")
        return

    if index < 0 or index >= len(notes):
        print("Index out of range.")
        return

    notes.pop(index)
    print("Note deleted.")


# ---------- Main menu ----------
def main():
    # Load notes automatically on startup
    load_notes()

    while True:
        print("\n=== Personal Notebook Manager ===")
        print("1) Add a new note")
        print("2) List all notes")
        print("3) Search notes by keyword")
        print("4) Filter notes by tag")
        print("5) Edit an existing note")
        print("6) Delete a note")
        print("7) Save notes to a file")
        print("8) Load notes from file")
        print("9) Finish")

        choice = input("Choose: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            filter_by_tag()
        elif choice == "5":
            edit_note()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            save_notes()
        elif choice == "8":
            load_notes()
        elif choice == "9":
            print("Thank GOD!!, Goodbye! XD")
        else:
            print("Invalid choice.")

main()

