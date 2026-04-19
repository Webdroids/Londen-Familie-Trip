import re

with open("src/components/MapTab.tsx", "r") as f:
    content = f.read()

# Replace dark map with Voyager
content = content.replace('url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"', 'url="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png"')

# Add legend
legend_html = """
      <div className="absolute top-4 left-4 right-4 z-[500] flex items-center justify-between pointer-events-none">
        <h1 className="text-2xl font-bold text-white drop-shadow-md">Kaartoverzicht</h1>
      </div>

      {/* Floating Legend */}
      <div className="absolute bottom-24 left-1/2 -translate-x-1/2 z-[500] bg-white dark:bg-slate-800 p-3 rounded-2xl shadow-xl border border-gray-200 dark:border-slate-700 pointer-events-auto flex gap-4 text-xs font-medium">
        <div className="flex items-center gap-2">
          <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png" alt="Blue pin" className="h-5" />
          <span className="text-slate-700 dark:text-slate-300">Ontdekken</span>
        </div>
        <div className="flex items-center gap-2">
          <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png" alt="Green pin" className="h-5" />
          <span className="text-slate-700 dark:text-slate-300">In planning</span>
        </div>
      </div>
"""
content = content.replace("""      <div className="absolute top-4 left-4 right-4 z-[500] flex items-center justify-between pointer-events-none">\n        <h1 className="text-2xl font-bold text-white drop-shadow-md">Kaartoverzicht</h1>\n      </div>""", legend_html)

with open("src/components/MapTab.tsx", "w") as f:
    f.write(content)
