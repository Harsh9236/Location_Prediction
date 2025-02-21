import re

def extract_bracketed_text(filepath):
    """
    Removes everything in a text file that is not within angled brackets,
    removes the angled brackets, and saves the result to the same file.

    Args:
        filepath (str): The path to the text file.
    """
    try:
        with open(filepath, 'r') as file:
            text = file.read()

        # Regular expression to find text within angled brackets
        bracketed_texts = re.findall(r'<([^>]*)>', text)

        # Join the extracted texts (you can modify the separator if needed)
        extracted_content = "".join(bracketed_texts)

        with open(filepath, 'w') as file:
            file.write(extracted_content)

        print(f"Successfully processed file: {filepath}")

    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "/home/harsh/Location-Predictor/model_response.txt"
    extract_bracketed_text(file_path)
