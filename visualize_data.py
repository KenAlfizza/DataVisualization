# import libraries
import circlify
import matplotlib.pyplot as plt

import geopy
import pandas as pd
import pycountry


# libraries
from mpl_toolkits.basemap import Basemap
import numpy as np



def get_geolocations(countries) -> list[geopy.location.Location]:
    # calling the Nominatim tool and create Nominatim class
    for i in range(0, len(countries)):
        if 'Congo' in countries[i]:
            countries[i] = 'Congo'
        if 'Hispanophone' in countries[i]:
            countries[i] = 'Mexico'
        if 'Czech' in countries[i]:
            countries[i] = 'Czech'

    loc = geopy.Nominatim(user_agent="Geopy Library")

    geolocs = []

    for country in countries:
        try:
            country_code = pycountry.countries.get(name=country).alpha_2
            # Due to Nominatim issue, Hong Kong country code HK is replaced with CN
            if country_code == 'HK':
                country_code = 'CN'

        except AttributeError:
            country_code = ""

        geolocs.append(loc.geocode(country, country_codes=country_code))

    return geolocs


def visualise_region(countries: list):
    # Map with connection, Works but not good for large dataset

    geolocs = get_geolocations(countries)

    lons = []
    lats = []
    for geoloc in geolocs:
        lons.append(geoloc.longitude)
        lats.append(geoloc.latitude)

    print(len(lons))
    print(len(lats))
    # Set the plot size for this notebook:
    plt.rcParams["figure.figsize"] = 15, 12

    # Background map
    m = Basemap(llcrnrlon=-179, llcrnrlat=-60, urcrnrlon=179, urcrnrlat=70, projection='merc')
    m.drawmapboundary(fill_color='white', linewidth=0)
    m.fillcontinents(color='#f2f2f2', alpha=0.7)
    m.drawcoastlines(linewidth=0.1, color="white")

    # Add a connection between China and Region of Focus
    # China's Geolocation
    startlat = 35.000074
    startlon = 104.999927

    # Target Geolocation
    for i in range(0, len(countries)):
        # Draw Connection
        if startlon - lons[i] > 0 and startlat - lats[i] > 0:
            m.drawgreatcircle(startlon, startlat, lons[i], lats[i], linewidth=2, color='orange')

    for i in range(0, len(countries)):
        # Annotate Country
        if startlon - lons[i] > 0 and startlat - lats[i] > 0:
            plt.annotate(countries[i], xy=m(lons[i] + 3, lats[i]), verticalalignment='center')

    # Annotate China
    plt.annotate('China', xy=m(startlon + 3, startlat), verticalalignment='center')

    plt.show()


def visualise_region2(countries: list):
    geolocs = get_geolocations(countries)

    lons = []
    lats = []
    for geoloc in geolocs:
        lons.append(geoloc.longitude)
        lats.append(geoloc.latitude)

    # Set the dimension of the figure
    plt.rcParams["figure.figsize"] = 15, 10

    # Make the background map
    m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
    m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
    m.fillcontinents(color='grey', alpha=0.3)
    m.drawcoastlines(linewidth=0.1, color="white")

    # prepare a color for each point depending on the continent.
    country_colors = plt.get_cmap(countries)

    # Add a point per position
    m.scatter(
        x=lons,
        y=lats,
        s=36 / 6,
        alpha=0.4,
        c=country_colors,
        cmap="Set1"
    )


def visualize_parent_entity(data):
    # Compute circle positions thanks to the circlify() function
    circles = circlify.circlify(
        data,
        show_enclosure=False,
        target_enclosure=circlify.Circle(x=0, y=0, r=1)
    )

    # Create just a figure and only one subplot
    fig, ax = plt.subplots(figsize=(14,14))

    # Title
    ax.set_title('China State Media Parent Entities')

    # Remove axes
    ax.axis('off')

    # Find axis boundaries
    lim = max(
        max(
            abs(circle.x) + circle.r,
            abs(circle.y) + circle.r,
        )
        for circle in circles
    )
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)

    # Print circle the highest level (continents):
    for circle in circles:
        if circle.level != 2:
          continue
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="lightblue"))

    # Print circle and labels for the highest level:
    for circle in circles:
        if circle.level != 3:
          continue
        x, y, r = circle
        label = circle.ex["id"]
        ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="#69b3a2"))
        plt.annotate(label, (x, y), ha='center', color="white")

    # Print labels for the continents
    for circle in circles:
        if circle.level != 2:
          continue
        x, y, r = circle
        label = circle.ex["id"]
        plt.annotate(label, (x, y), va='center', ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

    plt.show()


def visualize_parent_entity2(data: pd.DataFrame):
    # Visualize the parent entities to a bubble chart

    # Sort the values before visualising it
    # As when circlify is creating the circle, it sorts the values lists

    circles = circlify.circlify(
        data=data['value'].tolist(),
        show_enclosure=False,
        target_enclosure=circlify.Circle(x=0, y=0, r=1)
    )

    fig, ax = plt.subplots(figsize=(10, 10))

    # Title
    ax.set_title('China State Media Parent Entities')

    # Remove axes
    ax.axis('off')

    # Find axis boundaries
    lim = max(
        max(
            abs(circle.x) + circle.r,
            abs(circle.y) + circle.r,
        )
        for circle in circles
    )
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)

    labels = data['name'].tolist()

    # print circles
    for circle, label in zip(circles, labels):
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r * 0.7, alpha=0.9, linewidth=2, facecolor="#69b2a3", edgecolor="black"))

        line_break_limit = 16
        last_space = 0
        for i in range(1, len(label)):
            if label[i] == ' ':
                last_space = i

            if i % line_break_limit == 0:
                label = label[0:last_space] + '\n' + label[last_space+1:len(label)]

        print(r)

        ax.text(x, y-r*0.75, label, ha='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5)).set_fontsize('8')

    plt.show()



