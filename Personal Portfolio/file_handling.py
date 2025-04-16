#the file that will be called to handle the users files 

from time_handling import *

def read_file(filepath): 
    with open(filepath, "r") as file:
        return file.read()
    
def write_file(filepath, new_text):
        # Read the existing content
        with open(filepath, "r") as file:
            existing_content = file.read()

        updated_content = f"{existing_content}\n{new_text}" #combinign the new and old info 

        # Calculate word count
        word_count = len(updated_content.split())

        # timestamp from otherr file 
        timestamp = get_timestamp()

        # Preparingg for final print 
        final_content = f"{updated_content}\n\nWord Count: {word_count}\nLast Updated: {timestamp}"

        # File Writing 
        with open(filepath, "w") as file:
            file.write(final_content)


if __name__ == "__main__":
    filepath = ""
    new_text=""
    read_file(filepath)
    write_file(filepath, new_text)
