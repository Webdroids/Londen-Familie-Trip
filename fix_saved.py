with open("src/components/SavedTab.tsx", "r") as f:
    content = f.read()

content = content.replace("bg-white dark:bg-white/50 dark:bg-slate-800/50", "bg-white/50 dark:bg-slate-800/50")
content = content.replace("hover:bg-gray-100 dark:bg-slate-700", "hover:bg-gray-100 dark:hover:bg-slate-700")

with open("src/components/SavedTab.tsx", "w") as f:
    f.write(content)
