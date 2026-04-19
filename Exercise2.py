try:
    Message = input("Enter a short note/message: ")

    with open("notes.txt", "w") as file:
        file.write(Message)

    print("\nMessage saved successfully!\n")

except Exception as e:
    print("Error writing to file:", e)


try:
    print("Reading file:")
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error reading file:", e)


try:
    new_note = input("\nEnter another note: ")

    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    print("\nUpdated file content:")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print(updated_content)

except Exception as e:
    print("Error while appending to file:", e)