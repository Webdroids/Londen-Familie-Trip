import os
import re

MAPPINGS = {
    # Backgrounds
    r"\bbg-slate-900\b": "bg-gray-50 dark:bg-slate-900",
    r"\bbg-slate-800\b": "bg-white dark:bg-slate-800",
    r"\bbg-slate-800/50\b": "bg-white/50 dark:bg-slate-800/50",
    r"\bbg-slate-800/90\b": "bg-white/90 dark:bg-slate-800/90",
    r"\bbg-slate-700\b": "bg-gray-100 dark:bg-slate-700",
    r"\bbg-slate-950\b": "bg-gray-200 dark:bg-slate-950",
    r"\bhover:bg-slate-950\b": "hover:bg-gray-200 dark:hover:bg-slate-950",
    r"\bhover:bg-slate-700\b": "hover:bg-gray-100 dark:hover:bg-slate-700",
    r"\bhover:bg-slate-600\b": "hover:bg-gray-200 dark:hover:bg-slate-600",

    # Texts
    r"\btext-white\b": "text-slate-900 dark:text-white",
    r"\btext-slate-200\b": "text-slate-800 dark:text-slate-200",
    r"\btext-slate-300\b": "text-slate-600 dark:text-slate-300",
    r"\btext-slate-400\b": "text-slate-500 dark:text-slate-400",
    r"\bhover:text-white\b": "hover:text-slate-900 dark:hover:text-white",
    r"\bplaceholder-slate-400\b": "placeholder-slate-500 dark:placeholder-slate-400",
    r"\bplaceholder-slate-500\b": "placeholder-slate-400 dark:placeholder-slate-500",

    # Borders
    r"\bborder-slate-700\b": "border-gray-200 dark:border-slate-700",
    r"\bborder-slate-600\b": "border-gray-300 dark:border-slate-600",
    r"\bborder-slate-800\b": "border-gray-200 dark:border-slate-800",
    r"\bhover:border-slate-600\b": "hover:border-gray-300 dark:hover:border-slate-600",
}

# Fix some specific issues manually
def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    for search, replace in MAPPINGS.items():
        # Avoid double replacing
        if replace in content:
            continue
        content = re.sub(search, replace, content)

    with open(filepath, "w") as f:
        f.write(content)

components_dir = "src/components"
for filename in os.listdir(components_dir):
    if filename.endswith(".tsx"):
        process_file(os.path.join(components_dir, filename))

process_file("src/App.tsx")
