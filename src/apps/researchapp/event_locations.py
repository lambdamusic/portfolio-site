"""
Coordinates for the places where talks happened, for the map on /events/.

`Publication.pubplace` is free text typed over twenty years - "London, UK",
"Pacifico Yokohama, Yokohama, Japan", "Ancona University". Rather than
geocode that at request time (a network call per page render, and a
different answer whenever the upstream gazetteer changes), the lookup is
frozen here: the map is then deterministic, works offline, and the
wget-mirrored static site has no runtime dependency on anyone's API.

Provenance: geocoded once against OpenStreetMap Nominatim on 2026-09-23,
then hand-corrected where the first hit was wrong or too coarse:

    Arlington, USA          Nominatim picked Arlington, Texas; the talk was
                            at the Office of Naval Research in Virginia.
    Maryland, USA           was the state centroid; DH09 was at the
                            University of Maryland, College Park.
    Kirchberg, Austria      picked Kirchberg in Carinthia; the Ludwig
                            Wittgenstein Symposium is at Kirchberg am Wechsel.
    Royal Holloway, London  resolved to central London; the college is in
                            Egham, Surrey.
    Trento, Italy           was the province centroid, moved to the city.
    Ancona University       and The Technical University of Denmark did not
                            resolve at all; set by hand.

ADDING A NEW EVENT: if its `pubplace` string is not a key here the event
still lists normally, it just gets no dot on the map. Add the string with
its coordinates - `tools/geocode-event-places` prints the missing ones.

Third value is the resolved place name, kept only so a human reviewing this
file can see what each coordinate pair actually refers to.
"""

# pubplace string (verbatim, as stored) -> (lat, lon, what it resolved to)
EVENT_LOCATIONS = {
    'Ancona University':
        (43.6158, 13.5189, 'Ancona, Marche, Italy'),
    'Arlington, USA':
        (38.8816, -77.091, 'Arlington, Virginia, United States'),
    'Banff, Canada':
        (51.1751, -115.5721, 'Banff, Alberta, Canada'),
    'Basel, Switzerland':
        (47.5581, 7.5878, 'Basel, Basel-Stadt, Schweiz/Suisse/Svizzera/Svizra'),
    'Bethesda, USA':
        (38.9813, -77.1234, 'Bethesda, Montgomery County, Maryland, United States'),
    'Bethlehem, USA':
        (40.6179, -75.3787, 'Bethlehem, Northampton County, Pennsylvania, United States'),
    'Budva, Montenegro':
        (42.2886, 18.842, 'Budva, Opština Budva, Crna Gora / Црна Гора'),
    'Buenos Aires':
        (-34.6096, -58.3888, 'Buenos Aires, Comuna 1, Ciudad Autónoma de Buenos Aires, Argentina'),
    'Chicago, USA':
        (41.8756, -87.6244, 'Chicago, South Chicago Township, Cook County, Illinois, United States'),
    'Copenhagen, Denmark':
        (55.6867, 12.5701, 'København, Københavns Kommune, Region Hovedstaden, 1357, Danmark'),
    'Dublin, Ireland':
        (53.3494, -6.2606, 'Dublin, County Dublin, Leinster, Éire / Ireland'),
    'Frankfurt, Germany':
        (50.1106, 8.6821, 'Frankfurt am Main, Hessen, Deutschland'),
    'Granada':
        (37.1735, -3.5995, 'Granada, Comarca de la Vega de Granada, Granada, Andalucía, España'),
    'Hamburg, Germany':
        (53.5502, 10.0013, 'Hamburg, Deutschland'),
    'Heraklion, Crete, Greece':
        (35.3391, 25.1333, 'Ηράκλειο, Δημοτική Ενότητα Ηρακλείου, Δήμος Ηρακλείου, Περιφερειακή Ενότητα Ηρακλείου, Περιφέρεια Κρήτης, Αποκεντρωμένη Διοίκηση Κρήτης, 712 02, Ελλάς'),
    'Kirchberg, Austria':
        (47.6167, 15.9833, 'Kirchberg am Wechsel, Lower Austria, Austria'),
    'Leeds, UK':
        (53.7974, -1.5438, 'Leeds, West Yorkshire, England, LS1 6AL, United Kingdom'),
    'Leipzig':
        (51.3406, 12.3747, 'Leipzig, Sachsen, Deutschland'),
    'London, UK':
        (51.5074, -0.1278, 'Greater London, England, United Kingdom'),
    'Los Angeles, CA, USA':
        (34.0537, -118.2428, 'Los Angeles, Los Angeles County, California, United States'),
    'Los Angeles, USA':
        (34.0537, -118.2428, 'Los Angeles, Los Angeles County, California, United States'),
    'Marina Del Rey, California, USA':
        (33.9777, -118.4486, 'Marina del Rey, Los Angeles County, California, 90292, United States'),
    'Maryland, USA':
        (38.9897, -76.9378, 'University of Maryland, College Park, United States'),
    'Milton Keynes, UK':
        (52.0407, -0.7594, 'Milton Keynes, City of Milton Keynes, England, United Kingdom'),
    'Milton Keynes, United Kingdom':
        (52.0407, -0.7594, 'Milton Keynes, City of Milton Keynes, England, United Kingdom'),
    'Montpellier, France':
        (43.6112, 3.8767, 'Montpellier, Hérault, Occitanie, France métropolitaine, France'),
    'Montreal, Canada':
        (45.5032, -73.5698, 'Montréal, Agglomération de Montréal, Montréal (région administrative), Québec, Canada'),
    'Munich, Germany':
        (48.1371, 11.5754, 'München, Bayern, Deutschland'),
    'New York, USA':
        (40.7127, -74.006, 'New York, United States'),
    'Oxford, UK':
        (51.752, -1.2578, 'Oxford, Oxfordshire, England, United Kingdom'),
    'Pacifico Yokohama, Yokohama, Japan':
        (35.4575, 139.6371, 'パシフィコ横浜, 臨港幹線道路, Minato Mirai, 高島, 西区, 横浜市, 神奈川県, 231-0017, 日本'),
    'Portoroz, Slovenia':
        (45.5146, 13.591, 'Portorož / Portorose, Piran / Pirano, Upravna enota Piran / Unità amministrativa Pirano, 6320, Slovenija'),
    'Prague, Czech  Republic':
        (50.0875, 14.4213, 'Praha, Česko'),
    'Riva del Garda, Italy':
        (45.8867, 10.8458, 'Riva del Garda, Comunità Alto Garda e Ledro, Provincia di Trento, Trentino-Alto Adige/Südtirol, 38066, Italia'),
    'Rome, Italy':
        (41.8933, 12.4829, 'Roma, Roma Capitale, Lazio, Italia'),
    'Royal Holloway University, London, UK':
        (51.425, -0.5628, 'Royal Holloway, Egham, Surrey, United Kingdom'),
    'Scottsdale, AZ, USA':
        (33.4942, -111.926, 'Scottsdale, Maricopa County, Arizona, United States'),
    "Shakespeare's Globe, London, UK":
        (51.5081, -0.0972, "Shakespeare's Globe, 21, New Globe Walk, Borough Market, Bankside, Southwark, London Borough of Southwark, Greater London, England, SE1 9DT, United Kingdom"),
    'Shanghai, China':
        (31.2313, 121.47, '上海市, 中国'),
    'Stanford, USA':
        (37.4265, -122.1703, 'Stanford, Palo Alto, Santa Clara County, California, United States'),
    'Strasbourg, France':
        (48.5846, 7.7507, "Strasbourg, Bas-Rhin, Collectivité européenne d'Alsace, Grand Est, France métropolitaine, France"),
    'The Technical University of Denmark':
        (55.7861, 12.5236, 'Kongens Lyngby, Denmark'),
    'Tokyo, Japan':
        (35.6769, 139.7639, '東京都, 日本'),
    'Trento, Italy':
        (46.0679, 11.1211, 'Trento, Trentino-Alto Adige, Italy'),
    'Trondheim, Norway':
        (63.4304, 10.3952, 'Trondheim, Trøndelag, Norge'),
    'University of Strathclyde, Glasgow':
        (55.8619, -4.242, 'University of Strathclyde, Montrose Street, Merchant City, City Centre, Glasgow, Glasgow City, Alba / Scotland, G1 1RX, United Kingdom'),
    'Université de Lausanne':
        (46.5226, 6.5809, "Université de Lausanne, Allée de Dorigny, Quartier Centre, Ecublens, District de l'Ouest lausannois, Vaud, 1022, Schweiz/Suisse/Svizzera/Svizra"),
    'Washington, USA':
        (38.8951, -77.0364, 'Washington, District of Columbia, United States'),
    'Whistler, BC, Canada':
        (50.1172, -122.9543, 'Whistler Resort Municipality, Squamish-Lillooet Regional District, British Columbia, Canada'),
    'York':
        (53.9657, -1.0743, 'York, York and North Yorkshire, England, United Kingdom'),
}


def coords_for(pubplace):
    """(lat, lon) for a pubplace string, or None if it is not mapped."""
    if not pubplace:
        return None
    entry = EVENT_LOCATIONS.get(pubplace.strip())
    return (entry[0], entry[1]) if entry else None
