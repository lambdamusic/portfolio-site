# world-atlas

Vendored so the events map is fully self-contained: no CDN, no tile server,
no API key, and the wget-mirrored static site keeps working offline.

| file | source | version | licence |
|---|---|---|---|
| `countries-110m.json` | [topojson/world-atlas](https://github.com/topojson/world-atlas) | 2.0.2 | ISC (see `LICENSE`) |
| `topojson-client.min.js` | [topojson/topojson-client](https://github.com/topojson/topojson-client) | 3.1.0 | ISC |

Both are Michael Bostock's, both ISC. Rendered with the d3 v4 bundle already
in `libs/d3-v4/` (that build predates `geoNaturalEarth1`, hence the map uses
`geoEquirectangular`).
