# splitter() — Step by Step

## Code

```python
def splitter(file):
    base = file.split("/")[-1]
    name, ext = base.rsplit(".", 1)
    parts = name.rsplit("_", 1)
    return parts[0], parts[1], "." + ext
```

## Input

`"/file_0.txt"` → returns `("file", "0", ".txt")`

---

## Step 1 — `base = file.split("/")[-1]`

Path may have directories before filename. Split on `/` → `["", "file_0.txt"]`. Take `[-1]` = last element = just filename. Now `base = "file_0.txt"`. Strips any path prefix.

---

## Step 2 — `name, ext = base.rsplit(".", 1)`

Need to separate `"file_0.txt"` into `"file_0"` and `"txt"`. Split on `.`. Use `rsplit` (right-to-left) with max `1` split → safe if filename had dots in it like `"my.file_0.txt"` — only splits the last dot. Result: `name="file_0"`, `ext="txt"`.

---

## Step 3 — `parts = name.rsplit("_", 1)`

Need to separate `"file_0"` into `"file"` and `"0"`. Split on `_`. Again `rsplit` max `1` → safe if name was `"my_file_0"`, only splits last underscore → `["my_file", "0"]`. Result: `parts = ["file", "0"]`.

---

## Step 4 — `return parts[0], parts[1], "." + ext`

`parts[0]` = name, `parts[1]` = version. `"." + ext` adds dot back → `.txt` not `txt`. Dot included because extension is conventionally written `.txt` not `txt`.

---

## Why `rsplit` everywhere instead of `split`

`split` goes left-to-right. `"my.file_0.txt".split(".", 1)` → `["my", "file_0.txt"]` — wrong. `rsplit` anchors to the rightmost delimiter, which is always the true extension boundary.
