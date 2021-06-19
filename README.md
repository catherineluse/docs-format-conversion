# docs-format-conversion

This script converts the Rancher docs structure from this format:

folder
  child_page_folder1
    _index.md
  child_page_folder2
    _index.md
  _index.md

To this format:

folder
  child_page_folder1.md
  child_page_folder2.md
  _index.md
