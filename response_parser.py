import re

def find_text_in_angle_brackets(filepath):

    try:
        with open(filepath, 'r') as file:
            text_content = file.read()

            matches = re.findall(r'<(.*?)>', text_content)
            return matches
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

if __name__ == "__main__":
    file_path = "./model_response.txt"
    extracted_texts = find_text_in_angle_brackets(file_path)

    if extracted_texts:
        for text in extracted_texts:
            print(f"- {text}")
    else:
        print("\nNo text found within angle brackets in the file.")
