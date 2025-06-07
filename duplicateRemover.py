import os
import shutil

def move_repeated_files(folder_path):
    
    files = os.listdir(folder_path)
    
    name_counts = {}
    
    for f in files:
        
        if os.path.isfile(os.path.join(folder_path, f)):
            
            name = os.path.splitext(f)[0]
            
            if name in name_counts:
                
                name_counts[name].append(f)
            
            else:
                
                name_counts[name] = [f]
    
    repeated = {k:v for k, v in name_counts.items() if len(v) > 1}
    
    if not repeated:
        
        return
    
    new_folder = os.path.join(folder_path, "repeated_files")
    
    if not os.path.exists(new_folder):
        
        os.mkdir(new_folder)
    
    for file_list in repeated.values():
        
        for file_name in file_list:
            
            src = os.path.join(folder_path, file_name)
            
            dst = os.path.join(new_folder, file_name)
            
            shutil.move(src, dst)

folder = "/mnt/c/Mohit/Music/Head Bop Central"
move_repeated_files(folder)