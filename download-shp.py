import geopandas as gpd
import requests, zipfile, io

# 1. Download file ZIP shapefile GADM Indonesia
url = "https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_IDN_shp.zip"
r = requests.get(url)

# 2. Ekstrak ke memori
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("gadm_idn")   # folder lokal "gadm_idn"
