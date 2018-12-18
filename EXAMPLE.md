# bt_scraper
BT Phonebook to CSV web scraper

Once the python modules have been installed:
```bash
pip install -r requirements.txt
```
Run this command with the below arguments:
```python
{python 3.6} bt_scrape.py -l {city or town} -n {last name}
```
Example output:
```ruby
[root@server util]# python36 bt_scrape.py -l manchester -n garcia
Name , Address , Post Code , Area , Phone Number , District , Distance from centre , Date
 * Garcia   , 3 Brownhills Ct Sandy La  , M21 8TE , Manchester   , (0161) *** **** , M21 , 2.92 miles from the centre of manchester , 15/12/18 23:59:16
 * Garcia   , 19 Thomas Street  , M32 0HX , Stretford Manchester   , (0161) *** **** , M32 , 2.72 miles from the centre of manchester , 15/12/18 23:59:16
 * Garcia   , 40 Pinnington Road  , M18 8WR , Manchester   , (0161) *** **** , M18 , 3.33 miles from the centre of manchester , 15/12/18 23:59:16
 *********** Garcia   , Flat 4 105 Wellington Rd  , M14 6AY , Fallowfield Manchester   , (0161) *** **** , M14 , 2.92 miles from the centre of manchester , 15/12/18 23:59:16
 * Garcia   , 6 Rowan Way  , M7 4EH , Salford   , (0161) *** **** , M7 , 2.08 miles from the centre of manchester , 15/12/18 23:59:16
 * Garcia   , 1208/49 Goulden St  , M4 5EN , Manchester   , (0161) *** **** , M4 , 0.81 miles from the centre of manchester , 15/12/18 23:59:16
 * Garcia-*****   , Flat 23 Regency House 36-38 Whitworth Street  , M1 3NR , Manchester   , (0161) *** **** , M1 , 0.46 miles from the centre of manchester , 15/12/18 23:59:16
 ******** Garcia********   , 3 Velour Close  , M3 6AQ , Salford   , (0161) *** **** , M3 , 1.0 miles from the centre of manchester , 15/12/18 23:59:16
 * ******* Garcia   , Ground Floor Flat 1 Cambridge Avenue  , M16 8JY , Manchester   , (01612) ****** , M16 , 2.23 miles from the centre of manchester , 15/12/18 23:59:16
 * ****** Garcia   , 82 Jackson Crescent  , M15 5AA , Manchester   , (01612) ****** , M15 , 0.67 miles from the centre of manchester , 15/12/18 23:59:16
 * *****-Garcia   , Apartment 410 35 Radium St  , M4 6AH , Manchester   , (0161) *** **** , M4 , 1.02 miles from the centre of manchester , 15/12/18 23:59:16
[root@server util]#
```
You can also select a file path with a list of names in to search for. Use the '-f' flag and then specify the file.

Example:
```ruby
[root@server util]# cat ./list.txt
Reyes
Torres
[root@server util]# python bt_scrape.py -l manchester -f list.txt
Name , Address , Post Code , Area , Phone Number , District , Distance from centre , Date
 ********* Reyes , 29 Kensington Road   , M21 9GH , Manchester  , (0161) *** **** , M21 , 2.47 miles from the centre of manchester , 18/12/18 14:19:53
 ******* Reyes *******  ,  75 Brandwood Av  , M21 7PL , Manchester  , (01616) ****** , M21 , 3.96 miles from the centre of manchester, 18/12/18 14:19:53
 ** * ******* Reyes **  , 81 Sidney Road    , M9 8AT , Manchester   , (01619) ****** , M9 , 3.04 miles from the centre of manchester, 18/12/18 14:19:53
 *** Torres , 49 Lloyd Wright Av , M11 3NJ  , Manchester    , (0161) *** **** , M11 ,   1.62 miles from the center of manchester, 18/12/18 14:19:53
 ````