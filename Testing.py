import pandas as pd
from PIL import Image

weapon_info = pd.read_csv('WeaponInfo.csv', sep=';')
for i in range(round(weapon_info.size/weapon_info.iloc[0].size)):
    try:
        image = Image.open('pictures/'+'_'.join(weapon_info.iloc[i]['Name'].split()).lower() + '.png')
    except Exception :
        print('!!!!!!!!!!!!!!!!!!'+'_'.join(weapon_info.iloc[i]['Name'].split()).lower())
