with open("src/App.tsx", "r") as f:
    content = f.read()

content = content.replace("            isDarkMode={isDarkMode}\n            setIsDarkMode={setIsDarkMode}\n          />\n        )}\n        {activeTab === 'saved'", "          />\n        )}\n        {activeTab === 'saved'")

with open("src/App.tsx", "w") as f:
    f.write(content)

with open("src/components/DiscoverTab.tsx", "r") as f:
    content2 = f.read()

content2 = content2.replace("import { Search, MapPin, Loader2, Heart, Clock, Navigation, Sun, Moon } from 'lucide-react';", "import { Search, MapPin, Loader2, Heart, Clock, Navigation, Sun, Moon, Ticket } from 'lucide-react';")

with open("src/components/DiscoverTab.tsx", "w") as f:
    f.write(content2)
