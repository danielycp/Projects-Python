#!/usr/bin/env python
# coding: utf-8

# HDB Resale Data Analytics
# ===
# ---

# Background of HDB Resale Project
# ---
# 
# Getting a HDB is probably one of the biggest financial decisions many Singaporeans have to make, given its exhorbitant cost. Making a wrong decision could set you back several years in terms of opportunity cost & time value of money. 
# 
# <img src='data:image/webp;base64,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
# '/>
# 
# In this project, we seek to build data visualisation to shed light on the HDB resale market, and provide key consideration parameters to help us make better decisions in choosing a: <br>
# 
# (1) HDB Resale flat, or <br>
# (2) BTO flats that are likely to appreciate in the resale market

# Loading the Dataset
# ---
# 
# We start by first loading the CSV data of Singapore HDB listings (73320 rows × 14 columns) into a nested list, <code>hdb_resale_listings</code>.
# 

# In[1]:


import csv

hdb_resale_listings = []

with open('data/HDB_Resale_With_Geocoordinates.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        hdb_resale_listings.append(row)

    hdb_resale_listings_headers = hdb_resale_listings[0]
    hdb_resale_listings = hdb_resale_listings[1:]
    
print(hdb_resale_listings[0]) # Print first row of data


# For our visualisation, we display a snippet of the <code>hdb_resale_listings</code> nested list in a tabular format. 

# In[2]:


import pandas as pd

hdb_resale_df = pd.read_csv("data/HDB_Resale_With_Geocoordinates.csv")
hdb_resale_df


# Data Cleaning
# ---
# 
# We now write a loop to iterate through the data to perform some cleaning. The data columns we will be cleaning are:
# - <code>floor_area_sqm</code> (convert to float)
# - <code>remaining_lease</code> (extract only the years & convert it to float)
# - <code>resale_price</code> (convert to float)
# - <code>longitude</code> (convert to float)
# - <code>latitude</code> (convert to float)
# 

# In[25]:


for row in hdb_resale_listings:
    
    floor_area_sqm = row[6]
    lease_remaining = row[9]                 
    resale_price = row[10]
    longitude = row[12]
    latitude = row[13]
    
    row[6] = float(floor_area_sqm)
    
    if isinstance(lease_remaining,str):
        row[9] = int(lease_remaining[:2]) # Get years of lease remaining with slicing, and convert it to int type
   
    row[10] = float(resale_price)
    
    if longitude == '':
        row[12] = 0
    else:
        row[12] = float(longitude)
        
    if latitude == '':
        row[13] = 0
    else:
        row[13] = float(latitude)

print(hdb_resale_listings[:5]) # Print first 5 rows of data


# For our visualisation, we display a snippet of the cleaned data stored in the variable <code>hdb_resale_listings</code> in a tabular format. 

# In[4]:


hdb_resale_df = pd.DataFrame(hdb_resale_listings, columns = hdb_resale_listings_headers)
hdb_resale_df.head()


# ***
# 
# 
# Data Preparation & Visualisation
# ===
# ***

# Calculate the Number of Resale Flats in Each Town 
# ---
# 
# <br>

# In[6]:


resale_counts_by_town = {}  

for row in hdb_resale_listings:
    
    town = row[1]
    
    if town in resale_counts_by_town:        
        resale_counts_by_town[town] += 1  
    
    else: resale_counts_by_town[town] = 1   

import operator
print(dict(sorted(resale_counts_by_town.items(), key=operator.itemgetter(1),reverse=True)))


# We next visualise the Number of Resale Flats in Each Town in a simple bar chart
# ---
# 
# <br>
# 

# In[7]:



resale_counts_sorted_desc = {'SENGKANG': 5731, 'WOODLANDS': 5585, 'JURONG WEST': 5535, 'YISHUN': 5449, 'TAMPINES': 4679, 'PUNGGOL': 4520, 'BEDOK': 3912, 'HOUGANG': 3443, 'ANG MO KIO': 3313, 'CHOA CHU KANG': 3035, 'BUKIT MERAH': 2873, 'BUKIT PANJANG': 2836, 'BUKIT BATOK': 2724, 'TOA PAYOH': 2425, 'PASIR RIS': 2148, 'KALLANG/WHAMPOA': 2112, 'SEMBAWANG': 1946, 'QUEENSTOWN': 1927, 'GEYLANG': 1759, 'JURONG EAST': 1627, 'CLEMENTI': 1600, 'SERANGOON': 1473, 'BISHAN': 1427, 'CENTRAL AREA': 604, 'MARINE PARADE': 430, 'BUKIT TIMAH': 207}

import matplotlib.pyplot as plt

resale_town = list(resale_counts_sorted_desc.keys())
resale_flats = list(resale_counts_sorted_desc.values())

#------------------------
fig, ax = plt.subplots()
ax.bar(resale_town, resale_flats)

ax.set_xticklabels(resale_town, rotation=90)
ax.set_xlabel('Town')
ax.set_ylabel('Number of Resale Flats')
ax.set_title('Count of Resale Flats from Jan 2017 to June 2020')

plt.show()


# We observe that developing estates such as **Sengkang, Punggol, and Woodlands** tend to have a much higher volume of resale flats compared to mature estates such as Bishan and Marine Parade, which do not have as much land parcels available for development. 
# 
# These difference in resale volume could be due to:
# - **Young couples upgrading from their initial BTOs** in nearby areas (more prevalent in areas such as Sengkang, Punggol, Woodlands)
# - **Potential for housing appreciation** in developing estates like Sengkang and Punggol due to new amenities being developed

# We want to calculate the Total Sale Value in Each Town 
# ---
# 
# <br>

# In[9]:


town_resale_value_total = {} 

for row in hdb_resale_listings:
    
    town = row[1]

    if town in town_resale_value_total:        
        town_resale_value_total[town] += float(row[10]) 
    
    else:        
        town_resale_value_total[town] = float(row[10])  
    
print(town_resale_value_total)


# We want to calculate the Average Resale Value in Each Town 
# ---
# 
# <br>
# 

# In[10]:


# Expected output from Q1, sorted in alphabetical order
town_num_resale = {'ANG MO KIO': 3313, 'BEDOK': 3912, 'BISHAN': 1427, 'BUKIT BATOK': 2724, 'BUKIT MERAH': 2873, 'BUKIT PANJANG': 2836, 'BUKIT TIMAH': 207, 'CENTRAL AREA': 604, 'CHOA CHU KANG': 3035, 'CLEMENTI': 1600, 'GEYLANG': 1759, 'HOUGANG': 3443, 'JURONG EAST': 1627, 'JURONG WEST': 5535, 'KALLANG/WHAMPOA': 2112, 'MARINE PARADE': 430, 'PASIR RIS': 2148, 'PUNGGOL': 4520, 'QUEENSTOWN': 1927, 'SEMBAWANG': 1946, 'SENGKANG': 5731, 'SERANGOON': 1473, 'TAMPINES': 4679, 'TOA PAYOH': 2425, 'WOODLANDS': 5585, 'YISHUN': 5449}

# Expected output from Q3
town_resale_value_total = {'ANG MO KIO': 1357482312.0, 'BEDOK': 1601193885.0, 'BISHAN': 916235793.0, 'BUKIT BATOK': 1028796332.75, 'BUKIT MERAH': 1620070583.88, 'BUKIT PANJANG': 1209331600.0, 'BUKIT TIMAH': 147040354.0, 'CENTRAL AREA': 372667936.0, 'CHOA CHU KANG': 1171810776.0, 'CLEMENTI': 753674417.0, 'GEYLANG': 752338254.0, 'HOUGANG': 1485745756.88, 'JURONG EAST': 672843405.0, 'JURONG WEST': 2152691662.6400003, 'KALLANG/WHAMPOA': 1043695205.0, 'MARINE PARADE': 220658748.0, 'PASIR RIS': 1056249716.0, 'PUNGGOL': 2048804431.88, 'QUEENSTOWN': 1069608566.76, 'SEMBAWANG': 737883437.88, 'SENGKANG': 2496125484.76, 'SERANGOON': 722415279.0, 'TAMPINES': 2215182529.0, 'TOA PAYOH': 1189419991.0, 'WOODLANDS': 2105555068.88, 'YISHUN': 1977662848.0}


town_resale_average = {} # Populate this dictionary with Q4 answers

## Write your code below

for town_name, town_sales in town_resale_value_total.items():    
   
    average_resale_value = town_sales / town_num_resale[town_name]    
    town_resale_average[town_name] = round(average_resale_value)

import operator
sorted_resale = dict(sorted(town_resale_average.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_resale)


# We want to visualise the Average Resale Value in Each Town in a simple bar chart
# ---
# 

# In[11]:


town_resale_average = {'BUKIT TIMAH': 710340, 'BISHAN': 642071, 'CENTRAL AREA': 617000, 'BUKIT MERAH': 563895, 'QUEENSTOWN': 555064, 'MARINE PARADE': 513160, 'KALLANG/WHAMPOA': 494174, 'PASIR RIS': 491736, 'TOA PAYOH': 490482, 'SERANGOON': 490438, 'TAMPINES': 473431, 'CLEMENTI': 471047, 'PUNGGOL': 453275, 'SENGKANG': 435548, 'HOUGANG': 431527, 'GEYLANG': 427708, 'BUKIT PANJANG': 426422, 'JURONG EAST': 413548, 'ANG MO KIO': 409744, 'BEDOK': 409303, 'JURONG WEST': 388924, 'CHOA CHU KANG': 386099, 'SEMBAWANG': 379180, 'BUKIT BATOK': 377679, 'WOODLANDS': 377002, 'YISHUN': 362941}

town_avg_list = list(town_resale_average.keys())
average_list = list(town_resale_average.values())

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(town_avg_list, average_list)

ax.set_xticklabels(town_avg_list, rotation=90)
ax.set_xlabel('Town')
ax.set_ylabel('Average Resale Value')
ax.set_title('Average Resale Value in Each Town')

plt.show()


# Unsurprisingly, **HDB flats in central areas like Bukit Timah and Bishan have some of the highest resale values**. The convenience of living in these areas also contribute to the huge demand of BTO flats there; getting a BTO in these areas is almost like striking the lottery!
# 
# One interesting observation is the surprisingly high resale value of Punggol flats relative to other towns. While some may have the impression that Punggol flats are inaccessible and not desirable, the average resale value tells a different story. Observe that Punggol's resale value is markedly higher than areas like Ang Mo Kio and Bedok. In addition, the average resale value of Punggol flats is not that far off from matured estates like Clementi, Tampines & Serangoon.
# 
# A potential follow-up visualisation would be a time-series analysis of the Punggol HDB resale values over the years, and one might discover significant capital appreciation opportunities for Punggol BTO owners in the resale market!
# <p>
# <p>

# We want to know if the Lease is an Important Factor in the HDB Resale Price 
# ---
# 
# <br>
# 
# <div class="alert alert-block alert-info">
#     
# <b>Background:</b>
#     
# - Some claim that HDB is an appreciating asset, yet, you often wonder how this can be true when the remaining lease period of HDB flats shortens over the years.
# - We want to visualise the relationship between HDB resale prices and remaining lease periods using a line plot, to assess if lease remaining could serve as an important consideration factor when buying a HDB for investment.
# 
# </div>    

# In[12]:


average_resale_for_lease_year_remaining = {45: 226042, 46: 242145, 47: 246401, 48: 254636, 49: 260232, 50: 269885, 51: 296375, 52: 325913, 53: 354740, 54: 364082, 55: 366896, 56: 379482, 57: 362915, 58: 358926, 59: 361077, 60: 363807, 61: 363912, 62: 368609, 63: 386043, 64: 389136, 65: 401178, 66: 405131, 67: 409869, 68: 423459, 69: 431147, 70: 446439, 71: 488230, 72: 502543, 73: 513224, 74: 509820, 75: 485555, 76: 480516, 77: 467435, 78: 461030, 79: 457907, 80: 458187, 81: 448684, 82: 458495, 83: 452845, 84: 457780, 85: 475330, 86: 539646, 87: 572114, 88: 563815, 89: 536062, 90: 639708, 91: 596058, 92: 579430, 93: 521120, 94: 453963, 95: 451161, 96: 679590}

lease = list(average_resale_for_lease_year_remaining.keys())
average_resale_value = list(average_resale_for_lease_year_remaining.values())

fig, ax = plt.subplots()

ax.scatter(lease,average_resale_value)
ax.plot(lease,average_resale_value, marker='D', linestyle='solid')

ax.set_xlabel("Lease Remaining")                      
ax.set_ylabel("Resale Value")  
ax.set_title("Average Resale Value for Lease Years Remaining")
plt.show()


# Despite Minister Mah Bow Tan's [sweeping claim](https://omh.sg/blog/post/minister-lawrence-wongs-comments-how-story-unfolded) in 2011 that HDB is an asset that will appreciate in value over time, the above chart clearly shows that this is a flawed notion. This line plot illustrates a close correlation between the remaining lease period and the resale value of flats sold after 2017, which can be corroborated with Minister Lawrence Wong's [blog post](https://mndsingapore.wordpress.com/2017/03/24/choosing-a-home-for-life/) in March 2017. If you are looking for a resale flat, it is important to exercise caution for HDB resale flats with short leases.
# 
# Another observation from this chart is that, BTO owners who sell their flats near the Minimum Occupancy Period (MOP), with about 90 years of lease remaining, are likely to gain maximum resale value out of on their subsidised flats!
# <p>
# <p>

# We want to investigate examine and visualise the relationship between floor area and HDB resale prices in a simple table.
# ---
# 
# <br>

# In[13]:


hdb_resale_df.head(3)


# In[14]:


floor_area_sqm = []
resale_price = []

for row in hdb_resale_listings:
    floor_area_sqm.append(row[6])
    resale_price.append(row[10])

fig, ax = plt.subplots(figsize=(18,12))

scatter_plot_obj = ax.scatter(floor_area_sqm, resale_price)

plt.title('Relationship Between Floor Area & Resale Price')

plt.xlabel('Floor Area (in square metres)')
plt.ylabel('Sale Price (in million SGD)')

plt.show()


# The scatterplot above shows that <b>floor area is closely and positively correlated with HDB resale prices</b>, with some variance that can likely be attributed to their locations (as investigated above). If you're looking for a large HDB flat, be prepared to pay!
# <p>

# Comparing Selected 4 Room Flats in Singapore 
# ---
# <br>
# 
# <div class="alert alert-block alert-info">
#     
# <b>Background:</b>
#     
# - I am interested in buying a 4-room flat and have shortlisted a few housing estates of interest: Punggol, Tampines, Woodlands, Clementi and Yishun. As such, I wish to investigate the price distribution of 4-room HDB resale flats in these select towns.
#     
# </div>

# In[15]:


punggol = []
tampines = []
woodlands = []
clementi = []
yishun = []

for row in hdb_resale_listings:
    
    if row[2] == '4 ROOM':        
        town = row[1]        
        if town == 'PUNGGOL':
            punggol.append(row[10])
            
        elif town == 'TAMPINES':
            tampines.append(row[10])
            
        elif town == 'WOODLANDS':
            woodlands.append(row[10])
            
        elif town == 'CLEMENTI':
            clementi.append(row[10])
            
        elif town == 'YISHUN':
            yishun.append(row[10])  

print(punggol[:5])
print(tampines[:5])
print(woodlands[:5])
print(clementi[:5])
print(yishun[:5])


# In[16]:


fig, ax = plt.subplots()
ax.boxplot([punggol, tampines, woodlands, clementi, yishun])

ax.set_xticklabels(["Punggol", "Tampines", "Woodlands", "Clementi", "Yishun"])  
ax.set_ylabel("Resale Value (in SGD)")

plt.title('Resale Value of 4-Room flats in Jan 2017 to Jun 2020')

plt.show()


# From the boxplot, we see that **4-room resale flats in Clementi tend to cost more and can have a huge variance in price**. If you're on a very tight budget, a resale flat in Woodlands may be the optimal choice. 4-room resales flats in Punggol and Tampines have similar prices, so **it would be helpful to zoom into Punggol & Tampines estates and compare the amenities available** to specific flats and sub-areas in each town, in order to make a more informed decision. 
# 
# <br>

# We want to construct a Heatmap to visualise the density of 4-rooms HDB resale listings across different towns in Singapore.
# ---
# 

# In[20]:


import folium
from folium.plugins import HeatMap

lat_long_4_room = []

for row in hdb_resale_listings:
    
    if row[2] == '4 ROOM':
        lat_long_4_room.append([row[13],row[12]])
    
map_folium = folium.Map([1.357,103.826], height=350, width=800, zoom_start=11.4)

HeatMap(lat_long_4_room, radius=8, gradient={0.2:'blue', 0.4:'purple', 0.6:'orange', 1.0:'red'}).add_to(map_folium)

display(map_folium)


# <p>
# 
# We next construct a Folium Marker Cluster to visualise the geographical distribution & resales prices of all 4-rooms HDB resale listings in Singapore. 
# ---
# 

# In[24]:


from folium.plugins import MarkerCluster

def extract_lat_long_price(database, room_type):
    
    lat_long_4_room = []
    resale_price = []

    for row in database:        
        if row[2] == room_type:
            lat_long_4_room.append([row[13],row[12]])
            resale_price.append(row[10])      
    return lat_long_4_room, resale_price

lat_long_4_room, resale_price = extract_lat_long_price(hdb_resale_listings, '4 ROOM')


from folium.plugins import MarkerCluster

map_folium = folium.Map([1.357,103.826], height=550, width=900, zoom_start=11.5)

marker_cluster = MarkerCluster().add_to(map_folium)


for i in range(0,len(lat_long_4_room)):
    
    lat_long_of_one_listing = lat_long_4_room[i]    
    pop_display_price = '$' + str(resale_price[i]) 
        
    folium.Marker(
        location=lat_long_of_one_listing,
        popup=pop_display_price,
        icon=None,
    ).add_to(marker_cluster)

display(map_folium)

