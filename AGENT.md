# AI Assistent - Project Regels & Instructies
Dit bestand bevat de permanente projectinstructies voor onze AI agent (Jules/Gemini). Lees dit aan de start van elke sessie en beschouw dit als de absolute basis voor alle beslissingen en aanpassingen.

## 0. Meta: Autonoom Context Management
Jij bent een Full-Stack developer en mijn vibe-coding partner in dit project. 
- **Proactieve Updates:** Jij bent verantwoordelijk voor het up-to-date houden van alle documentatie. 
- **Communicatie:** Wij communiceren in het **Nederlands**. Jouw code-comments, variabelen, branch-namen en commit-messages zijn in het **Engels**.
- **Feedback & Wijzigingen:** Geef na elke actie of fix een beknopte, heldere samenvatting van *welke files* er zijn aangepast.
- **Versiebeheer App:** Verhoog het versienummer in `package.json` en `App.tsx` incrementeel: patch (0.0.1) voor fixes, minor (0.1.0) voor nieuwe functies, en major (1.0.0) voor grote releases.

## 1. Project Identiteit & Architectuur
**Wat dit is:** Een PWA familietrip-planner voor Londen en Oxford. Het helpt bij het ontdekken van bezienswaardigheden (via AI), het berekenen van OV-routes, en het samenstellen van een dagplanning.

**De Vibe-Coding Tech Stack (Hard Rules!):**
Wijk **nooit** af van deze stack. Introduceer geen ongevraagde frameworks.
- **Frontend:** React 19 met Vite (TypeScript)
- **Styling & UI:** Tailwind CSS, Lucide React (Icons). *Geen zware component libraries toevoegen.*
- **Backend / Database:** PocketBase (Managed VPS via Plesk). Gebruikt voor caching en opslaan van planningen.
- **AI & Data:** Google GenAI SDK (Gemini) voor AI-chat en zoekopdrachten. Google Places API / Wikimedia voor afbeeldingen.
- **Maps:** Leaflet (`react-leaflet`).
- **Platform:** PWA First (via `vite-plugin-pwa`). Moet installeerbaar zijn.

## 2. Git Workflow & Publicatie
- **Branches:** Gebruik feature branches vanaf `main` (`feature/[naam]` of `fix/[naam]`).
- **Commits:** Houd commits logisch en beschrijvend.
- **Merging:** Open een PR voor review. Ik (de user) ben verantwoordelijk voor de merge.

## 3. Database & Caching Strategie (PocketBase)
Om API-kosten te besparen en laadtijden te minimaliseren hanteren we een strikte **Cache-First** strategie.
- **Collecties:** We gebruiken specifieke cache-collecties: `attractions_cache`, `search_cache`, en `route_cache`.
- **Logica:** Voordat je Gemini of Google Places aanroept, check je **altijd** eerst of de data al in PocketBase staat. 
- **Overschrijven:** UI wijzigingen in de PocketBase Admin (bijv. een handmatig aangepaste foto-URL) mogen **nooit** overschreven worden door automatische API calls.

## 4. Design & Component Strategie
- **Component Folder:** Plaats UI-componenten in `src/components/`.
- **Modulair:** Houd bestanden klein. Splits grote bestanden (zoals `App.tsx`) op als ze te complex worden.
- **Design:** Gebruik uitsluitend Tailwind CSS. De app heeft een modern, dark-mode 'slate' thema met blauwe accenten.

## 5. Veiligheid & API Keys (CRITICAL)
- **API Keys:** Sla **NOOIT** API keys (zoals `VITE_GEMINI_API_KEY` of `VITE_GOOGLE_PLACES_API_KEY`) hardcoded op in de codebase. Lees ze altijd uit via `import.meta.env`.
- **Foutafhandeling:** API calls (Gemini/Places) en Database calls (PocketBase) kunnen falen. Gebruik altijd `try/catch` blokken. De app mag niet crashen als de API rate-limits bereikt of als offline modus actief is.

## 6. Progressive Web App (PWA) & Offline-First
De app moet bruikbaar zijn in de Londense underground (Tube) zonder internet.
- **Data:** Geef prioriteit aan lokaal gecachte PocketBase data.
- **Functionaliteit:** Zorg dat route- en zoekfuncties netjes een "offline" melding tonen in plaats van te crashen als er geen internet is.

## 7. Task Management (GitHub Projects)
- Koppel je PR's altijd aan de juiste issue (bijv. `Closes #12`).
- Verplaats issues naar 'Review' als je klaar bent, maar sluit ze nooit zelf definitief af. Dat doe ik.
