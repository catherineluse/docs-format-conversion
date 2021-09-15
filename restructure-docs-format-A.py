import os
import shutil

# This script converts the Rancher docs structure into this format for Docusaurus:

# ```
# folder
#   _category_.json
#   child_page_folder1.md
#   child_page_folder2.md
#   folder.md
# ```

# and the `_category_.json` file looks like:

# ```
# {
#   "label": "Title that appears in sidebar",
#   "position": 2
# }
# ```

#  The `label` is like `shortTitle` in Hugo, and `position` is like `weight` in Hugo.

current_dir = os.path.dirname(os.path.realpath(__file__))

temp_dir = "/Users/catherineluse/Documents/rancher-docs/docusaurus/docs-format-conversion/temp"
destination_dir = "/Users/catherineluse/Documents/rancher-docs/docusaurus/docs-format-conversion/docs-after"

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
        # If there are no subdirectories, 
        print('found no subdirectories in ' + path_string)

        def moveFile(new_temp_name):
          # Then place it in the destination folder
          # at the level where its parent folder was.
          print('copying this item: ' + new_temp_name)
          destination_path = "/".join(path[:-1])
          destination_name = os.path.join(destination_dir, destination_path) + "/" + parent_folder + ".md"
          print('to this destination: ' + destination_name)
          shutil.copy(new_temp_name, destination_name)

        def rename(currentName, parent_folder):
          print('currentName ' + currentName)
          print('parent_folder' + parent_folder)
          temp_name = temp_dir + "/" + currentName + ".md"
          new_temp_name = temp_dir + "/" + parent_folder + ".md"
          print('created new temp name ' + new_temp_name)
          os.rename(temp_name, new_temp_name)

        # Copy the _index.md file to a temporary directory.
        if os.path.exists(path_string + "/_index.md"):
          shutil.copy(path_string + "/_index.md", temp_dir)
          # Then rename the file using its parent folder name.
          rename("_index", parent_folder)

        # Or copy the index.md file to a temporary directory.
        if os.path.exists(path_string + "/index.md"):
          shutil.copy(path_string + "/index.md", temp_dir)
          # Then rename the file using its parent folder name.
          rename("index", parent_folder)

        # Then move the new file from the temp folder to the 'after' folder.
        new_temp_name = temp_dir + "/" + parent_folder + ".md"
        moveFile(new_temp_name)

        # Then remove the temporary directory.
        os.remove(new_temp_name)
