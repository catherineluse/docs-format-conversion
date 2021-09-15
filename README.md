# docs-format-conversion

This script converts the Rancher docs structure from this format:

```
folder
  child_page_folder1
    _index.md
  child_page_folder2
    _index.md
  _index.md
```

To this format:

```
folder
  child_page_folder1.md
  child_page_folder2.md
  index.md
```

and the `_category_.json` file looks like:

```
{
  "label": "Title that appears in sidebar",
  "position": 2
}
```

The `label` is like `shortTitle` in Hugo, and `position` is like `weight` in Hugo.