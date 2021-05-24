#!/usr/bin/env python3
import os
import sys
import yaml

import matplotlib.pyplot as plt
from typing import List

import numpy as np
from matplotlib.pyplot import figure
import random
import geopandas as gpd

def create_map(sentiment: List[float], countries: List[str], label: str, file: str) -> str:
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    gdf['sentiment'] = 0

    for i, j in zip(countries, sentiment):
        gdf['sentiment'].loc[gdf['name'] == i] = j

    fig, ax = plt.subplots(figsize=(12, 8), dpi=200)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    gdf.plot(ax=ax, column='sentiment', cmap='RdYlGn', legend=True,
            legend_kwds={'label': label, 'orientation': "horizontal"})

    fig.savefig(file)
    return file

if __name__ == "__main__":
    command = sys.argv[1]
    argument_file = os.environ["FILE"]
    argument_label = os.environ["LABEL"]
    argument_sentiment = [float(os.environ[f"SENTIMENT_{i}"]) for i in range(int(os.environ["SENTIMENT"]))]
    argument_countries = [str(os.environ[f"COUNTRIES_{i}"]) for i in range(int(os.environ["COUNTRIES"]))]
    functions = {
        "create_map": create_map,
    }
    output = functions[command](argument_sentiment, argument_countries, argument_label, argument_file)
    print("--> START CAPTURE")
    print(yaml.dump({"output": output}))
    print("--> END CAPTURE")
