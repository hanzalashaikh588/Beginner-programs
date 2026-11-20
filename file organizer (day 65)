#excercise 7 files reorganizer.
import os
def file_organizer():
    folder_path = r"c:\Users\Lenovo\OneDrive\Desktop\file 3"
    files = sorted(name for name in os.listdir(folder_path)if name.endswith(".png"))

    for number, old_name in zip(range(1,21),files):
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, f"pic number {number}.png")
        os.rename(old_path , new_path)
        #print(old_path ,"->",new_path)

file_organizer()
