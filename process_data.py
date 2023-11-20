import pandas as pd
def get_media_name_en_by_id(data, id):
    """Returns the english name of media"""
    if id < data.shape[0]:
        return data['Name (English)'][id]

    return ''


def get_possible_regions(data):
    """Returns the possible region of focus from the data"""
    regions = set()
    for i in data['Region of Focus']:
        regions.add(i)

    return regions


def get_media_ids_by_region(data, region):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Region of Focus'][i] == region:
            media_ids.append(i)

    return media_ids


def get_parent_entities(data):
    """Returns the possible region of focus from the data"""
    parents = set()
    for i in data['Parent entity (English)']:
        parents.add(i)

    return parents


def get_parent_entity_regions_of_focus(data, parent):
    regions = []
    for i in range(0, data.shape[0]):
        if data['Parent entity (English)'][i] == parent:
            if data['Region of Focus'][i] not in regions:
                regions.append(data['Region of Focus'][i])

    print(regions)
    return regions


def get_region_ammount(data, region):
    """Return the amount of state media for a given region"""
    count = 0
    for i in range(0, data.shape[0]):
        if data['Region of Focus'][i] == region:
            count += 1
    return count


def get_media_ids_by_parent_entity(data, parent):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Parent entity (English)'][i] == parent:
            media_ids.append(i)

    return media_ids


def get_possible_entity_owner(data):
    """Returns the possible region of focus from the data"""
    owners = set()
    for i in data['Entity owner (English)']:
        owners.add(i)

    return owners



def get_media_ids_by_entity_owner(data, ownner):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Entity owner (English)'][i] == ownner:
            media_ids.append(i)

    return media_ids


def get_possible_language(data):
    """Returns the possible region of focus from the data"""
    language = set()
    for i in data['Language']:
        language.add(i)

    return language


def get_media_ids_by_languge(data, language):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Language'][i] == language:
            media_ids.append(i)

    return media_ids


def sort_followers(data, platform, ascending):
    """Return the sorted data DataFrame type depending on the number of followers"""
    data[platform].replace(',', '')
    return data[platform].sort_values(ascending=ascending)


def categorize_parent_independent_others(data: pd.DataFrame, other_limit) -> pd.DataFrame:
    """Returns the dataframe consists of:
        - Large parent media with media > other_limit
        - Other parent media with media < other_limit but > 1
        - Independent parent media with media == 1
    """
    values = data['value'].tolist()
    names = data['name'].tolist()

    # Finding the amount of independent and other media and remove them from the lists
    independent = 0
    others = 0
    removed_index = []
    for i in range(0, len(values)):
        if values[i] == 1:
            independent += 1
            removed_index.append(i)
        elif 1 < values[i] <= other_limit:
            others += 1
            removed_index.append(i)

    # Remove media and its amount from the lists
    removed_index.reverse()
    for i in removed_index:
        values.pop(i)
        names.pop(i)

    # Appending independent and others to the lists
    names.append('Independent')
    values.append(independent)
    names.append('Others')
    values.append(others)

    data = pd.DataFrame(data={'name': names, 'value': values}, columns=['name', 'value'])
    return data
