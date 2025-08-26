"""
File Handling and Exception Handling in Python

"""

def modify_content(content: str) -> str:
    """
    Modify the file content before writing to a new file.
    For this demo, we’ll simply make all text uppercase.
    You can change this logic to anything (e.g., add line numbers).
    """
    return content.upper()


def main():
    try:
        # Ask user for input file name
        input_filename = input("Enter the filename to read from: ").strip()

        # Try to open the file
        with open(input_filename, "r", encoding="utf-8") as infile:
            original_content = infile.read()

        # Modify content
        modified_content = modify_content(original_content)

        # Create output file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)

        print(f"✅ File successfully read and modified version saved as '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied when accessing the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
