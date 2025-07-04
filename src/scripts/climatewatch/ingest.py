import requests
from collections import defaultdict
from pprint import pprint

# ClimateWatch data id
data_source_id = 214
gasses = {
    "all-ghg": 473,
    "co2": 474,
    "ch4": 475,
    "n2o": 476,
    "f-gas": 477,
}

session = requests.Session()

base_url = 'https://www.climatewatchdata.org/api/v1/data/historical_emissions'
base_year = 2022

sectors = {}
sector_slugs = [
    "total-excluding-lucf",
    "total-including-lucf",
    "total-excluding-lulucf",
    "total-including-lulucf",
    "transportation",
    "energy",
    "electricity-heat",
    "industrial-processes",
    "agriculture",
    "land-use-change-and-forestry",
    "building",
    "manufacturing-construction",
    
    "waste",
    "bunker-fuels",
    "other-fuel-combustion",
    "fugitive-emissions",   
]


from collections import defaultdict

def build_sector_hierarchy(sector_data):
    # Filter sectors with data_source_id = 214
    sector_data = [sector for sector in sector_data if sector['data_source_id'] == data_source_id]

    # Create a dictionary for storing hierarchical data
    sector_hierarchy = {}

    # Create a map for quick access by id
    sector_map = {sector['id']: sector for sector in sector_data}

    # Iterate through the sectors and build the hierarchy
    for sector in sector_data:
        if sector['parent_id'] is None:
            # Root node
            sector_hierarchy[sector['slug']] = {
                'name': sector['name'],
                'id': sector['id'],
                'children': {}
            }
        else:
            # Child node
            parent = sector_map.get(sector['parent_id'])
            if parent:
                # Navigate to the parent's place in the hierarchy
                parent_slug = parent['slug']
                parent_entry = sector_hierarchy.get(parent_slug, {})
                if 'children' in parent_entry:
                    parent_entry['children'][sector['slug']] = {
                        'name': sector['name'],
                        'id': sector['id'],
                        'children': {}
                    }

    return sector_hierarchy


def get_raw_sectors():
    url = f'{base_url}/sectors'
    response = session.get(url)
    data = response.json()
    return data["data"]

raw_sectors = get_raw_sectors()

hierarchy = build_sector_hierarchy(raw_sectors)
pprint(hierarchy, indent=2, width=120, compact=True)




