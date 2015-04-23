# google map downloader
## Introduction
A tool besed on python can download google map and merge small map images to big images.

## Require
python 2.7
PIL

## Usage
Set location region. Change the variable `L_long`,`R_long`,`T_lat`,`B_lat` values, which means the longitude of left top, right bottom 
and latitude of left top and right bottom.

  (L_long, T_lat)-----------------------------------------
  |                                                       |
  |                                                       |
  |                                                       |
  |                                                       |
  ------------------------------------------(R_long, B_lat)
  
You can also change the `zoom` value to get different resolution, see google map api.

use `python googlemap.py` command to download all small images we need,
and `python imgmerge.py` to merge those small images to a big images.




