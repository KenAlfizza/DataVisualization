
import pandas as pd

import process_data

import visualize_data


if __name__ == '__main__':
    DATA = pd.read_excel(r'CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx', sheet_name='FULL')


def visualize_parent_entity():

    possible_parents = process_data.get_parent_entities(DATA)
    num_of_media = 0
    parent = []
    for p in possible_parents:
        media_ids = process_data.get_media_ids_by_parent_entity(DATA, p)

        media = []
        for media_id in media_ids:
            m = {'id': process_data.get_media_name_en_by_id(DATA, media_id), 'datum': 1}
            media.append(m)

        parent.append({'id': p, 'datum': len(media_ids), 'children': media})

        num_of_media += len(media_ids)

    data = {'id': 'ALL', 'datum': num_of_media, 'children': parent}
    print(data)

    visualize_data.visualize_parent_entity([data])


def visualize_parent_entity2():
    """ Visualise the parent entity size in a bubble chart"""
    values = []
    names = []
    parents = process_data.get_parent_entities(DATA)
    for p in parents:
        media_ids = process_data.get_media_ids_by_parent_entity(DATA, p)
        names.append(p)
        values.append(len(media_ids))

    data = pd.DataFrame(data={'name': names, 'value': values}, columns=['name', 'value'])

    data = process_data.categorize_parent_independent_others(data=data, other_limit=20)

    # Sort the values before visualising it
    # As when circlify is creating the circle, it sorts the values lists
    data = data.sort_values(by='value', ascending=True)

    visualize_data.visualize_parent_entity2(data)


def visualize_parent_entity_regions_of_focus(parent_entity):
    regions = process_data.get_parent_entity_regions_of_focus(data=DATA, parent=parent_entity)

    # Visualise connected map
    visualize_data.visualise_region(regions)

    # Visualise bubble map
    # visualize_data.visualise_region2(regions)












































