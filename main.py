
import pandas as pd

import process_data

if __name__ == '__main__':
    DATA = pd.read_excel(r'CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx', sheet_name='FULL')
    print(process_data.find_possible_regions(DATA))



















