import re

with open("src/components/ItineraryTab.tsx", "r") as f:
    content = f.read()


search_str = """                  <div key={`${item.id}-${idx}`} className="bg-slate-800 p-4 rounded-3xl shadow-md border border-slate-700 flex items-center cursor-pointer hover:border-slate-600 transition-colors">

                    <div className="flex-1 min-w-0" onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>"""

replace_str = """                  <div key={`${item.id}-${idx}`} className="bg-slate-800 p-4 rounded-3xl shadow-md border border-slate-700 flex items-center hover:border-slate-600 transition-colors">

                    <div className="shrink-0 cursor-pointer" onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>
                      {displayImage ? (
                        <img src={displayImage} alt={item.name} className="w-20 h-20 rounded-2xl object-cover mr-4" />
                      ) : (
                        <div className="w-20 h-20 rounded-2xl bg-slate-700 animate-pulse mr-4"></div>
                      )}
                    </div>

                    <div className="flex-1 min-w-0 cursor-pointer" onClick={() => { setSelectedAttraction(item); setCurrentImageIndex(0); }}>"""

content = content.replace(search_str, replace_str)


with open("src/components/ItineraryTab.tsx", "w") as f:
    f.write(content)
