# patch_mpl_renderer.py
import qiskit_metal.renderers.renderer_mpl.mpl_renderer as mpl_renderer
import pathlib

file_path = pathlib.Path(mpl_renderer.__file__)
print(f"Patching: {file_path}")

content = file_path.read_text(encoding="utf-8")

old_pattern = "lambda x: x[\n"  # won't match reliably due to line wrapping - see note below
count_x0 = content.count("x[0].buffer(")
count_x1 = content.count("float(x[1])")
print(f"Found {count_x0} occurrence(s) of x[0].buffer(, {count_x1} of float(x[1])")

new_content = content.replace("x[0].buffer(", "x.iloc[0].buffer(")
new_content = new_content.replace("float(x[1])", "float(x.iloc[1])")

file_path.write_text(new_content, encoding="utf-8")
print("Patch applied.")