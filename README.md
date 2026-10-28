# Ozarks Explorer

Phone-friendly map for finding lost and overgrown structures in the Missouri Ozarks.

## Layers
| Layer | Source |
|---|---|
| LiDAR hillshade (multidirectional) | USGS 3DEP Elevation ImageServer |
| LiDAR slope | USGS 3DEP Elevation ImageServer |
| Oldest topo / Newest old topo | USGS Historical Topographic Map Collection (Esri-hosted) |
| Aerial today / Topo today | USGS The National Map basemaps |

Pick a ground layer, put a second layer on top, and use Blend to fade between them.

## Hidden sites (`hidden-sites.json`)
Hand-researched list of hidden or forgotten places (lost graves, battle sites, ghost towns, legend sites). Each entry has the story, sources, access notes, and whether the location is an **exact** spot (solid pin) or an **approximate area** (dashed circle).

To add a site, copy an entry in `hidden-sites.json` and edit it, then run `python3 tools/export.py` to rebuild the app files.

## Use in OsmAnd or Organic Maps
- `hidden-sites.gpx`: import into OsmAnd (or any GPS app). Approximate areas come in as circle tracks.
- `hidden-sites.kml`: import into Organic Maps as a bookmark list.
- Each pin's pop-up also has OsmAnd and Organic Maps buttons that open that spot in the app.

## Links
`#zoom/lat/lon` in the URL opens that spot. Add `/pin` to drop a marker, for example `#17/37.04811/-92.83101/pin`.

## Ground rules
Looking and mapping are fine. On federal land, including Mark Twain National Forest, digging or removing artifacts is a federal crime under the Archaeological Resources Protection Act. Missouri law protects unmarked graves. Get landowner permission before going onto private land.
