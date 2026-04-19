import re

with open("src/components/ItineraryTab.tsx", "r") as f:
    content = f.read()

# Imports
content = content.replace("import { Calendar, Plus, MapPin } from 'lucide-react';", "import React, { useState } from 'react';\nimport { Calendar, Plus, MapPin, Trash2, ArrowRightLeft } from 'lucide-react';")
content = content.replace("import React from 'react';\nimport React", "import React")


# Props
content = content.replace("imageDictionary: Record<string, string>;", "imageDictionary: Record<string, string>;\n  removeFromItinerary: (day: string, attraction: Attraction) => void;\n  moveItineraryItem: (fromDay: string, toDay: string, attraction: Attraction) => void;")

content = content.replace("imageDictionary\n}: ItineraryTabProps) {", "imageDictionary,\n  removeFromItinerary,\n  moveItineraryItem\n}: ItineraryTabProps) {")


# State for modal
content = content.replace("return (\n    <div className=\"p-4 pb-24 h-full overflow-y-auto\">", "const [moveModalItem, setMoveModalItem] = useState<{ attraction: Attraction, fromDay: string } | null>(null);\n\n  return (\n    <div className=\"p-4 pb-24 h-full overflow-y-auto\">")


# Buttons and modal
search_str = """                    <div className="flex-1 min-w-0">
                      <h3 className="font-bold text-white text-lg truncate">{item.name}</h3>
                      <p className="text-xs text-slate-400 flex items-center mt-2 truncate">
                        <MapPin className="w-3 h-3 mr-1 shrink-0" /> <span className="truncate">{item.location.split(',')[0]}</span>
                      </p>
                    </div>
                  </div>"""

replace_str = """                    <div className="flex-1 min-w-0" onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>
                      <h3 className="font-bold text-white text-lg truncate">{item.name}</h3>
                      <p className="text-xs text-slate-400 flex items-center mt-2 truncate">
                        <MapPin className="w-3 h-3 mr-1 shrink-0" /> <span className="truncate">{item.location.split(',')[0]}</span>
                      </p>
                    </div>
                    <div className="flex flex-col space-y-2 ml-2">
                      <button
                        onClick={(e) => { e.stopPropagation(); setMoveModalItem({ attraction: item, fromDay: day }); }}
                        className="p-2 bg-slate-700 hover:bg-blue-600 rounded-full transition-colors text-white"
                      >
                        <ArrowRightLeft className="w-4 h-4" />
                      </button>
                      <button
                        onClick={(e) => { e.stopPropagation(); removeFromItinerary(day, item); }}
                        className="p-2 bg-slate-700 hover:bg-red-600 rounded-full transition-colors text-white"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>"""
content = content.replace(search_str, replace_str)


# Ensure the onClick is moved from the main div to the text div
content = content.replace("""                  <div key={`${item.id}-${idx}`} className="bg-slate-800 p-4 rounded-3xl shadow-md border border-slate-700 flex items-center cursor-pointer hover:border-slate-600 transition-colors" onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>""", """                  <div key={`${item.id}-${idx}`} className="bg-slate-800 p-4 rounded-3xl shadow-md border border-slate-700 flex items-center cursor-pointer hover:border-slate-600 transition-colors">""")

content = content.replace("onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>\n                    {displayImage", ">\n                    <div className=\"shrink-0 cursor-pointer\" onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>\n                    {displayImage ? (\n                      <img src={displayImage} alt={item.name} className=\"w-20 h-20 rounded-2xl object-cover mr-4\" />\n                    ) : (\n                      <div className=\"w-20 h-20 rounded-2xl bg-slate-700 animate-pulse mr-4\"></div>\n                    )}\n                    </div>")

content = re.sub(r"\{\s*displayImage \?\s*\(\s*<img[^>]*>\s*\)\s*:\s*\(\s*<div[^>]*>\s*</div>\s*\)\s*\}", "", content)


# Move modal HTML
modal_str = """      {Object.entries(itinerary).map(([day, items]) => ("""

modal_replace = """      {moveModalItem && (
        <div className="fixed inset-0 bg-black/60 z-[1050] flex items-center justify-center p-4 backdrop-blur-sm">
          <div className="bg-slate-800 rounded-3xl p-6 w-full max-w-sm border border-slate-700 shadow-2xl">
            <h3 className="text-xl font-bold text-white mb-4 text-center">Verplaats naar dag</h3>
            <div className="grid grid-cols-2 gap-3">
              {Object.keys(itinerary).map(d => (
                <button
                  key={d}
                  onClick={() => {
                    moveItineraryItem(moveModalItem.fromDay, d, moveModalItem.attraction);
                    setMoveModalItem(null);
                  }}
                  className={`py-3 rounded-xl font-medium transition-colors border ${d === moveModalItem.fromDay ? 'bg-blue-600 text-white border-blue-500 cursor-not-allowed opacity-50' : 'bg-slate-700 hover:bg-blue-600 text-white border-slate-600 hover:border-blue-500'}`}
                  disabled={d === moveModalItem.fromDay}
                >
                  {d}
                </button>
              ))}
            </div>
            <button
              onClick={() => setMoveModalItem(null)}
              className="mt-6 w-full bg-slate-900 hover:bg-slate-950 text-slate-300 py-3 rounded-xl font-bold transition-colors border border-slate-800"
            >
              Annuleren
            </button>
          </div>
        </div>
      )}

      {Object.entries(itinerary).map(([day, items]) => ("""

content = content.replace(modal_str, modal_replace)


with open("src/components/ItineraryTab.tsx", "w") as f:
    f.write(content)
