

import os
import shutil


path = input("Enter the path like (/home/anurag/Python/test) : ")




def organizer(path):

    if not os.path.exists(path) :
        print('Invalid Path')

    mpp = {
        'img' : ['.jpeg', '.jpg', '.gif', '.png'],
        'docs' : ['.pdf', '.docx', '.text'],
        'videos' : ['.mp4', '.mkv'],
        'music' : ['.mp3']
    }

   


    # Creating the folders according to map
    
    for folder in mpp:
        folder_path = os.path.join(path, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    


    # No matching the extension to the map value 
    # Moving them to into their respective folder
    for entry in os.listdir(path):

        full_Path = os.path.join(path, entry)
       
        if os.path.isfile(full_Path):
            ext = os.path.splitext(entry)[1].lower()

            # Iterating over map in key : value pair
            for folder , extensions in mpp.items():
                if ext in extensions:
                    target_path = os.path.join(path, folder, entry)

                    shutil.move(full_Path, target_path)
                    print(f"Moved  {entry} to {target_path} \n")
                    break
            # This moves other file extension to a dir name other     
            else:
                other_path = os.path.join(path, 'others')

                if not os.path.exists(other_path):
                    os.makedirs(other_path)

                target_path = os.path.join(other_path, entry)

                shutil.move(full_Path, target_path)




      
            
organizer(path)


