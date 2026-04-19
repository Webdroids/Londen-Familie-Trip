with open("src/App.tsx", "r") as f:
    content = f.read()

content = content.replace("            isDarkMode={isDarkMode}\n            setIsDarkMode={setIsDarkMode}\n          />\n        )}\n      </div>", "          />\n        )}\n      </div>")

with open("src/App.tsx", "w") as f:
    f.write(content)
