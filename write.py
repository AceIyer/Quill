#Responsible for writing down the documentation into the file
#Maybe make a seperate file like or folder like Project_Documenation/Docs.md or .txt
# this is the final page where it all comes together like a master-piece 
from datetime import datetime


def get_current_time():
    """
    This should allow for quill to get the local time of every user
    """
    current_datetime_local = datetime.now()
    date_string = current_datetime_local.strftime("%Y-%m-%d %H:%M:%S")

    return date_string


def write_into_doc():
    user_input = input("Enter any information you'd like to document >>")

    with open(".quill/project_documentation.md", "a", encoding = "utf-8" ) as file:
        
        file.write(user_input + "\n")




for i in range(5):
    write_into_doc()


