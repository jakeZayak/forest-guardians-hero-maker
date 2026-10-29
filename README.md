# Forest Guardians Hero Maker

A character creator for the kids' D&D adventure *Secret of the Forest Guardians*. Kids pick a name, the ability they're great at, and three powers, and the hero card builds as they go.

**Live page:** `index.html` is the whole app (art embedded, no build step needed to host it).

## Features
- Player count sets power uses: fewer than 4 players means Special 6/day and Ultimate 2/day (rulebook rule)
- Great ability = 5, kid picks the 3, the last gets 1
- Hearts by Strength (house rule, rulebook +1): Strength 1 = 3, Strength 3 = 4, Strength 5 = 5
- Armor is always 15
- Powers are the rulebook list; "Make my own" lets kids write a custom power but damage is locked to the fair patterns for that tier
- Random silly name button
- Party roster saved in the browser (localStorage), with Export / Import as a JSON file
- Print layout: 4 cards per letter page

## Hosting on GitHub Pages
Settings → Pages → Deploy from a branch → `main` / root.

## Editing
Edit `src/template.html`, then run `python3 src/build.py` to regenerate `index.html`.
To change art, replace a file in `src/art/` with the same name (webp), then rebuild.

Artwork is from the *Secret of the Forest Guardians* adventure PDF. For personal/home use.
