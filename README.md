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

To add a site, copy an entry in `hidden-sites.json` and edit it.

## Links
`#zoom/lat/lon` in the URL opens that spot. Add `/pin` to drop a marker, for example `#17/37.04811/-92.83101/pin`.

## Ground rules
Looking and mapping are fine. On federal land, including Mark Twain National Forest, digging or removing artifacts is a federal crime under the Archaeological Resources Protection Act. Missouri law protects unmarked graves. Get landowner permission before going onto private land.
