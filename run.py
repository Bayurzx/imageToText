import os
import easyocr
import time

# Get the current directory
# C:\Users\USER\Downloads\ocr
# current_directory = "C:\\Users\\USER\\Downloads\\ocr"
current_directory = "C:\\Users\\USER\\Desktop\\ocr"

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

# Open a file for writing the results
output_file = open(f'output_{str(int(time.time()))}.txt', 'w')
for filename in os.listdir(current_directory):
    # Check if the file is an image (you can add more image file extensions if needed)
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Read the text from the image
        image_path = os.path.join(current_directory, filename)
        result = reader.readtext(image_path, detail=0)

        # Write the result to the output file
        output_file.write(f"File: {filename}\n")
        output_file.write(f"Text: {result}\n")
        output_file.write("\n")

        # Log the progress to the terminal
        print(f"Processed: {filename}")


# Close the output file
output_file.close()
