import os
import shutil

from win32com import client


def convert_and_remove(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".doc"):
            # Full path of the input file
            input_file_path = os.path.join(input_folder, file_name)

            # Create corresponding output file path with .docx extension
            output_file_path = os.path.join(
                output_folder, f"{os.path.splitext(file_name)[0]}.docx"
            )

            # Convert .doc to .docx
            convert_to_docx(input_file_path, output_file_path)

    # Remove the input folder
    shutil.rmtree(input_folder)


def convert_to_docx(doc_file_path, docx_file_path):
    # Create a Word application object
    word_app = client.Dispatch("Word.Application")

    # Open the .doc file
    doc = word_app.Documents.Open(doc_file_path)

    # Save as .docx file
    doc.SaveAs(docx_file_path, FileFormat=12)  # 12 corresponds to .docx format

    # Close the documents
    doc.Close()

    # Make Word application invisible before quitting
    # word_app.Visible = False

    # Quit Word application
    try:
        # Quit Word application
        word_app.Quit()
    except Exception as e:
        print(f"Error while quitting Word application: {e}")


if __name__ == "__main__":
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Input and output folders
    input_folder = os.path.join(current_directory, "input")
    output_folder = os.path.join(current_directory, "output")

    convert_and_remove(input_folder, output_folder)
