
def find_possible_regions(data):
    """Returns the possible region of focus from the data"""
    regions = set()
    for i in data['Region of Focus']:
        regions.add(i)

    return regions


def find_media_ids_by_region(data, region):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Region of Focus'][i] == region:
            media_ids.append(i)

    return media_ids


def find_possible_parent_entity(data):
    """Returns the possible region of focus from the data"""
    parents = set()
    for i in data['Parent entity (English)']:
        parents.add(i)

    return parents


def find_media_ids_by_parent_entity(data, parent):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Parent entity (English)'][i] == parent:
            media_ids.append(i)

    return media_ids


def find_possible_entity_owner(data):
    """Returns the possible region of focus from the data"""
    owners = set()
    for i in data['Entity owner (English)']:
        owners.add(i)

    return owners


def find_media_ids_by_entity_owner(data, ownner):
    """Returns the id of media with the region of focus"""
    media_ids = []
    for i in range(0, data.shape[0]):
        if data['Entity owner (English)'][i] == ownner:
            media_ids.append(i)

    return media_ids


def find_possible_language(data):
    """Returns the possible region of focus from the data"""
    language = set()
    for i in data['Language']:
        language.add(i)

    return language


def find_media_ids_by_languge(data, language):
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

