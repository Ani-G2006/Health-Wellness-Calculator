
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(BASE_DIR, filename)

def save_new_entries(records, start_index, filename):
    file = open(get_path(filename), "a")
    for entry in records[start_index:]:
        pieces = []
        for key in entry:
            pieces.append(key + "=" + str(entry[key]))
        file.write("|".join(pieces) + "\n")
    file.close()

def view_file(filename):
    try:
        file = open(get_path(filename), "r")
        content = file.read()
        file.close()
        if content.strip() == "":
            print("No records saved yet.")
        else:
            print(content)
    except FileNotFoundError:
        print("No data yet — calculate this metric at least once first.")



def file_delete(filename):
    file = open(get_path(filename), "w")
    print("")
    file.close
    print("file is removed")