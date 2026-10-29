"""Rebuild ../index.html from template.html, embedding every image in art/ as a data URI.
Run from the repo root:  python3 src/build.py"""
import base64, pathlib
src = pathlib.Path(__file__).parent
t = (src / "template.html").read_text()
for img in sorted((src / "art").glob("*.webp")):
    data = base64.b64encode(img.read_bytes()).decode()
    t = t.replace(f"__IMG_{img.stem}__", f"data:image/webp;base64,{data}")
assert "__IMG_" not in t, "template references an image missing from src/art"
(src.parent / "index.html").write_text(t)
print("wrote index.html")
