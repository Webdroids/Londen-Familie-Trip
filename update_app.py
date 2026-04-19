import re

with open("src/App.tsx", "r") as f:
    content = f.read()

# Replace APP_VERSION
content = re.sub(r"const APP_VERSION = 'v0\.4\.6';", "const APP_VERSION = 'v0.5.0';", content)

# Add isDarkMode state and effect
search_str = "const [activeTab, setActiveTab] = useState<Tab>('discover');"
replace_str = """const [isDarkMode, setIsDarkMode] = useState(() => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) return savedTheme === 'dark';
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  });

  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [isDarkMode]);

  const [activeTab, setActiveTab] = useState<Tab>('discover');"""
content = content.replace(search_str, replace_str)

# Add removeFromItinerary and moveItineraryItem
search_str2 = "const openRoute = (attraction: Attraction) => {"
replace_str2 = """const removeFromItinerary = async (day: string, attraction: Attraction) => {
    // Optimistische UI update
    setItinerary(prev => ({
      ...prev,
      [day]: prev[day].filter(a => a.id !== attraction.id)
    }));
    showToast(`${attraction.name} verwijderd van ${day}`);

    try {
      const records = await pb.collection('itinerary_items').getList(1, 1, {
        filter: `attraction_id = "${attraction.id}" && day = "${day}"`
      });
      if (records.items.length > 0) {
        await pb.collection('itinerary_items').delete(records.items[0].id);
      }
    } catch (err) {
      console.error("Failed to remove itinerary item from PocketBase:", err);
      showToast("Verwijderen in de cloud mislukt.");
      // Rollback
      setItinerary(prev => ({
        ...prev,
        [day]: [...prev[day], attraction]
      }));
    }
  };

  const moveItineraryItem = async (fromDay: string, toDay: string, attraction: Attraction) => {
    if (itinerary[toDay].some(a => a.id === attraction.id)) {
      alert(`${attraction.name} staat al op ${toDay}!`);
      return;
    }

    // Optimistische UI update
    setItinerary(prev => ({
      ...prev,
      [fromDay]: prev[fromDay].filter(a => a.id !== attraction.id),
      [toDay]: [...prev[toDay], attraction]
    }));
    showToast(`${attraction.name} verplaatst naar ${toDay}`);

    try {
      const records = await pb.collection('itinerary_items').getList(1, 1, {
        filter: `attraction_id = "${attraction.id}" && day = "${fromDay}"`
      });
      if (records.items.length > 0) {
        await pb.collection('itinerary_items').update(records.items[0].id, {
          day: toDay
        });
      }
    } catch (err) {
      console.error("Failed to move itinerary item in PocketBase:", err);
      showToast("Verplaatsen in de cloud mislukt.");
      // Rollback
      setItinerary(prev => ({
        ...prev,
        [fromDay]: [...prev[fromDay], attraction],
        [toDay]: prev[toDay].filter(a => a.id !== attraction.id)
      }));
    }
  };

  const openRoute = (attraction: Attraction) => {"""
content = content.replace(search_str2, replace_str2)

# Add props to DiscoverTab and ItineraryTab
content = content.replace("imageDictionary={imageDictionary}", "imageDictionary={imageDictionary}\n            isDarkMode={isDarkMode}\n            setIsDarkMode={setIsDarkMode}")
content = content.replace("imageDictionary={imageDictionary}\n            isDarkMode={isDarkMode}\n            setIsDarkMode={setIsDarkMode}\n          />\n        )}\n        {activeTab === 'map'", "imageDictionary={imageDictionary}\n            isDarkMode={isDarkMode}\n            setIsDarkMode={setIsDarkMode}\n          />\n        )}\n        {activeTab === 'map'")

content = re.sub(
    r"(\<ItineraryTab[^>]*imageDictionary=\{imageDictionary\})([^>]*/\>)",
    r"\1\n            removeFromItinerary={removeFromItinerary}\n            moveItineraryItem={moveItineraryItem}\2",
    content,
    flags=re.MULTILINE
)


with open("src/App.tsx", "w") as f:
    f.write(content)
