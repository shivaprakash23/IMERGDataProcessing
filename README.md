# IMERGDataProcessing

This is small project that is part of bigger project where rainfall data is key. This code and tool box is specific to ESRI product. This code is useful for extarction of rainfall data from .nc file and aggregating it for a month. This tool came as necessity for processing "GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06 (GPM_3IMERGDL) at GES DISC". This data will be aggregated after 2 months and hence we need this.

Method

1. Download bulk Imerg data from Earth Search https://search.earthdata.nasa.gov/. 
2. Extract rainfall layer from .nc file
3. Keep monthwise data in folder
4. carry out numerical aggragtion to get 1 month rainfall accumulation
