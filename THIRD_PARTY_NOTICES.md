# Third-party notices

The MIT license for original Whereabouts application code does not replace third-party licenses
or service terms. This is a concise notice for the map components currently referenced by `index.html`,
not an exhaustive inventory of every third-party right in the repository.

| Component | Version | License / terms |
| --- | --- | --- |
| Leaflet | 1.9.4 | BSD-2-Clause; copyright 2010–2023 Volodymyr Agafonkin and 2010–2011 CloudMade. [Official license](https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE) |
| Leaflet.markercluster | 1.5.3 | MIT; copyright 2012 David Leaver. [Official license](https://github.com/Leaflet/Leaflet.markercluster/blob/v1.5.3/MIT-LICENCE.txt) |
| Esri World Dark Gray Canvas tiles and underlying map data | Online service | Provider and data-source terms apply; these are not covered by this repository's MIT license. [Service information](https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer) |

Leaflet and Leaflet.markercluster are loaded from version-pinned unpkg CDN URLs. Retain their
copyright, license notices, conditions, and disclaimers when copying or redistributing those components;
consult the linked official license texts for the full terms.

The existing on-map attribution is retained unchanged:

> Tiles © Esri — Esri, HERE, Garmin, GeoTechnologies, Inc. © OpenStreetMap contributors

Preserve provider and data-source attribution when using the map. Availability without an API key
does not make the tiles or map data MIT-licensed.
