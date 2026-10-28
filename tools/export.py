"""Build hidden-sites.gpx and hidden-sites.kml from hidden-sites.json.

Run from the repo root:  python3 tools/export.py
Exact sites become waypoints. Approximate sites become a waypoint at the
center plus a closed track tracing the search circle.
"""
import json, math
from xml.sax.saxutils import escape

sites = json.load(open('hidden-sites.json', encoding='utf-8'))

def circle(lat, lon, r_m, n=48):
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        dlat = (r_m * math.cos(a)) / 111320
        dlon = (r_m * math.sin(a)) / (111320 * math.cos(math.radians(lat)))
        pts.append((lat + dlat, lon + dlon))
    return pts

def desc(s):
    loc = 'Exact spot' if s['exact'] else f"Approximate area, {s['radius']/1609:.1f} mi radius"
    src = '\n'.join(f"{x['t']}: {x['u']}" for x in s['sources'])
    return f"{loc}\n\n{s['where']}\n\n{s['story']}\n\nAccess: {s['access']}\n\nSources:\n{src}"

# GPX (OsmAnd, Organic Maps, most GPS apps)
g = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<gpx version="1.1" creator="Ozarks Explorer" xmlns="http://www.topografix.com/GPX/1/1">',
     '<metadata><name>Ozarks Hidden Sites</name></metadata>']
for s in sites:
    g.append(f'<wpt lat="{s["lat"]:.6f}" lon="{s["lon"]:.6f}"><name>{escape(s["name"])}</name>'
             f'<desc>{escape(desc(s))}</desc><type>{"Exact" if s["exact"] else "Area"}</type></wpt>')
for s in sites:
    if not s['exact']:
        pts = ''.join(f'<trkpt lat="{a:.6f}" lon="{b:.6f}"/>' for a, b in circle(s['lat'], s['lon'], s['radius']))
        g.append(f'<trk><name>{escape(s["name"])} (search area)</name><trkseg>{pts}</trkseg></trk>')
g.append('</gpx>')
open('hidden-sites.gpx', 'w', encoding='utf-8').write('\n'.join(g))

# KML (Organic Maps bookmarks, Google Earth)
k = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Ozarks Hidden Sites</name>',
     '<Style id="exact"><IconStyle><color>ff0f56b8</color></IconStyle></Style>',
     '<Style id="area"><IconStyle><color>ffffffff</color></IconStyle><LineStyle><color>ff0f56b8</color><width>3</width></LineStyle></Style>']
for s in sites:
    sid = 'exact' if s['exact'] else 'area'
    k.append(f'<Placemark><name>{escape(s["name"])}</name><description>{escape(desc(s))}</description>'
             f'<styleUrl>#{sid}</styleUrl><Point><coordinates>{s["lon"]:.6f},{s["lat"]:.6f}</coordinates></Point></Placemark>')
    if not s['exact']:
        coords = ' '.join(f'{b:.6f},{a:.6f}' for a, b in circle(s['lat'], s['lon'], s['radius']))
        k.append(f'<Placemark><name>{escape(s["name"])} (search area)</name><styleUrl>#area</styleUrl>'
                 f'<LineString><coordinates>{coords}</coordinates></LineString></Placemark>')
k.append('</Document></kml>')
open('hidden-sites.kml', 'w', encoding='utf-8').write('\n'.join(k))
print(f'{len(sites)} sites -> hidden-sites.gpx, hidden-sites.kml')
