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

## Lost sites (`lost-sites.geojson`)
2,446 points from the **USGS GNIS Missouri file (2021-08-25)**: every school, church, post office, populated place, locale, building, mine, cemetery, bridge, dam, tower or hospital that GNIS marks "(historical)", clipped to the **EPA Level III Ozark Highlands ecoregion (39)**.

Removed as still active or well known (391 sites):
- 321 next to a same-name church, school, building or town that still exists in GNIS (within 500 m; 2 km for towns and post offices)
- 70 with their own Wikipedia article or National Register listing (Wikidata, exact name match)

- GNIS coordinates are where USGS recorded the feature, not a surveyed footprint. Expect to look around nearby.
- About 2,500 Missouri historical features have no coordinates in GNIS and are not included.

## Links
`#zoom/lat/lon` in the URL opens that spot. Add `/pin` to drop a marker, for example `#17/37.04811/-92.83101/pin`.

## Ground rules
Looking and mapping are fine. On federal land, including Mark Twain National Forest, digging or removing artifacts is a federal crime under the Archaeological Resources Protection Act. Missouri law protects unmarked graves. Get landowner permission before going onto private land.
