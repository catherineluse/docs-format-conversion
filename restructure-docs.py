import os
import shutil

# This script converts the Rancher docs structure from this format:

# folder
# child_page_folder1
#   _index.md
# child_page_folder2
#   _index.md
# _index.md

# To this format:

# folder
# child_page_folder1.md
# child_page_folder2.md
# _index.md

current_dir = os.path.dirname(os.path.realpath(__file__))
temp_dir = "/Users/catherineluse/rancher-docs/mkdocs-experiment/temp"
destination_dir = "/Users/catherineluse/rancher-docs/mkdocs-experiment/docs-after"

for root, dirs, files in os.walk("docs-before"):
    path = root.split(os.sep)
    parent_folder = path[-1]
    path_string = "/".join(path)

    if len(dirs) > 0:
        # Create folder structure
        new_directory = destination_dir + "/" + path_string
        print("creating new directory because it does contain more folders: " + new_directory)
        os.mkdir(new_directory)

        # Copy the index file into the new directory
        if os.path.exists(path_string + "/_index.md"):
            print("copying index file.")
            shutil.copy(path_string + "/_index.md", destination_dir + "/" + path_string + "/index.md")
        
    else:
        # If there are no subdirectories, copy the
        # index file to a temporary directory.
        print('found no subdirectories in ' + path_string)
        shutil.copy(path_string + "/_index.md", temp_dir)

        # Then rename it.
        temp_name = temp_dir + "/_index.md"
        new_temp_name = temp_dir + "/" + parent_folder + ".md"
        os.rename(temp_name, new_temp_name)

        # Then place it in the destination folder
        # at the level where its parent folder was.
        print('copying this item: ' + new_temp_name)
        

        destination_path = "/".join(path[:-1])
        destination_name = os.path.join(destination_dir, destination_path) + "/" + parent_folder + ".md"
        
        print('to this destination: ' + destination_name)

        shutil.copy(new_temp_name, destination_name)

        # Then remove the temporary
        os.remove(new_temp_name)
