import os
import glob 
from .OsfaFileObject import OsfaFileObject
from datetime import datetime

class OsfaFileBrowser:
    def __init__(self) -> None:
        self.start_path = "."
        self.list_of_objects = []
        self.base_path = 'C:/inetpub/wwwosfa/static/docs'
        #   "c:/osfa/Reports/"

    def get_browser(self, start_path):
        # start_path = self.base_path + start_path
        
        if len(start_path) == 0:
            start_path = self.base_path
        
        list_of_objects = list()

        for root, dirs, files in os.walk(start_path):
            
            for file_name in files:
                #   FILE
                full_path = start_path + "/" + file_name
                name_parts = file_name.split(".")

                if len(name_parts) == 1:
                    extension = "FILE"
                else:
                    extension = name_parts.pop().upper()
                
                string_of_size = "{:,}".format(round((os.path.getsize(full_path) + 1) / 1024)).replace(',', '')

                size = int(
                    float(
                        string_of_size
                    )
                )
                
                file_object = OsfaFileObject(
                    file_name,
                    start_path,
                    full_path,
                    size,
                    'FILE',
                    extension,
                    datetime.fromtimestamp(os.path.getmtime(full_path)).strftime("%m/%d/%Y %I:%M:%S %p")
                )
                list_of_objects.append(file_object) 

            for dir_name in dirs:
                full_path = start_path + "/" + dir_name

                dir_object = OsfaFileObject(
                    dir_name,
                    start_path,
                    full_path,
                    0,
                    'DIR',
                    '',
                    datetime.fromtimestamp(os.path.getmtime(full_path)).strftime("%m/%d/%Y %I:%M:%S %p")
                )

                list_of_objects.append(dir_object)

            break
        
        return list_of_objects
