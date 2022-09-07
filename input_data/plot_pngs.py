import matplotlib.pyplot as plt
import pyart
import cartopy
import cartopy.crs as ccrs                   # for projections
import cartopy.feature as cfeature           # for features
import cartopy.io.shapereader as shapereader
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.feature.nightshade import Nightshade
def plot_data(infilename, outpng):
  radar = pyart.io.read_nexrad_archive(infilename)
  display = pyart.graph.RadarMapDisplay(radar)
  fig = plt.figure(figsize=(10, 10))
  display.plot_ppi_map('reflectivity')
  fig.savefig(outpng)
if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='plot some radar data')
  parser.add_argument('ar2v', help="volume scan filename")
  parser.add_argument('png', help="output png filename")
  args = parser.parse_args()

  print("Plotting {} into {}".format(args.ar2v, args.png))
  plot_data(args.ar2v, args.png)