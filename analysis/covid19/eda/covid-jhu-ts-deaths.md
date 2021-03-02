# EDA - COVID-JHU-TS-DEATHS Files 

#### Column Name [IDX] -  Dtype (Head / Tail) 
- **UID** [0] - int64 (16 / 84070020) 
- **ISO2** [1] - object (AS / US) 
- **ISO3** [2] - object (ASM / USA) 
- **CODE3** [3] - int64 (16 / 840) 
- **FIPS** [4] - float64 (60.0 / nan) 
- **ADMIN2** [5] - object (nan / Weber-Morgan) 
- **PROVINCE_STATE** [6] - object (American Samoa / Utah) 
- **COUNTRY_REGION** [7] - object (US / US) 
- **LAT** [8] - float64 (-14.270999999999999 / 41.27116049) 
- **LONG** [9] - float64 (-170.132 / -111.9145117) 
- **COMBINED_KEY** [10] - object (American Samoa, US / Weber-Morgan, Utah, US) 
- **POPULATION** [11] - int64 (55641 / 0) 
- **RECORD_DT** [12] - datetime64[ns] (2020-01-22 00:00:00 / 2021-02-28 00:00:00) 
- **DEATHS** [13] - int64 (0 / 180) 



#### Head / Tail [n=20] Sample 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UID</th>
      <th>ISO2</th>
      <th>ISO3</th>
      <th>CODE3</th>
      <th>FIPS</th>
      <th>ADMIN2</th>
      <th>PROVINCE_STATE</th>
      <th>COUNTRY_REGION</th>
      <th>LAT</th>
      <th>LONG</th>
      <th>COMBINED_KEY</th>
      <th>POPULATION</th>
      <th>RECORD_DT</th>
      <th>DEATHS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-23</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-24</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-26</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-27</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-29</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-30</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-01-31</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-01</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-02</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-03</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-04</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-05</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-06</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-07</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-08</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-09</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>16</td>
      <td>AS</td>
      <td>ASM</td>
      <td>16</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>American Samoa</td>
      <td>US</td>
      <td>-14.271000</td>
      <td>-170.132000</td>
      <td>American Samoa, US</td>
      <td>55641</td>
      <td>2020-02-10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1349340</th>
      <td>84070002</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Dukes and Nantucket</td>
      <td>Massachusetts</td>
      <td>US</td>
      <td>41.406747</td>
      <td>-70.687635</td>
      <td>Dukes and Nantucket,Massachusetts,US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1349341</th>
      <td>84070005</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Federal Correctional Institution (FCI)</td>
      <td>Michigan</td>
      <td>US</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>Federal Correctional Institution (FCI), Michigan, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1349342</th>
      <td>84070004</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Michigan Department of Corrections (MDOC)</td>
      <td>Michigan</td>
      <td>US</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>Michigan Department of Corrections (MDOC), Michigan, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>148</td>
    </tr>
    <tr>
      <th>1349343</th>
      <td>84070003</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Kansas City</td>
      <td>Missouri</td>
      <td>US</td>
      <td>39.099700</td>
      <td>-94.578600</td>
      <td>Kansas City,Missouri,US</td>
      <td>488943</td>
      <td>2021-02-27</td>
      <td>515</td>
    </tr>
    <tr>
      <th>1349344</th>
      <td>84070015</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Bear River</td>
      <td>Utah</td>
      <td>US</td>
      <td>41.521068</td>
      <td>-113.083282</td>
      <td>Bear River, Utah, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1349345</th>
      <td>84070016</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Central Utah</td>
      <td>Utah</td>
      <td>US</td>
      <td>39.372319</td>
      <td>-111.575868</td>
      <td>Central Utah, Utah, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>54</td>
    </tr>
    <tr>
      <th>1349346</th>
      <td>84070017</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Southeast Utah</td>
      <td>Utah</td>
      <td>US</td>
      <td>38.996171</td>
      <td>-110.701396</td>
      <td>Southeast Utah, Utah, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1349347</th>
      <td>84070018</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Southwest Utah</td>
      <td>Utah</td>
      <td>US</td>
      <td>37.854472</td>
      <td>-111.441876</td>
      <td>Southwest Utah, Utah, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>232</td>
    </tr>
    <tr>
      <th>1349348</th>
      <td>84070019</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>TriCounty</td>
      <td>Utah</td>
      <td>US</td>
      <td>40.124915</td>
      <td>-109.517442</td>
      <td>TriCounty, Utah, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>29</td>
    </tr>
    <tr>
      <th>1349349</th>
      <td>84070020</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Weber-Morgan</td>
      <td>Utah</td>
      <td>US</td>
      <td>41.271160</td>
      <td>-111.914512</td>
      <td>Weber-Morgan, Utah, US</td>
      <td>0</td>
      <td>2021-02-27</td>
      <td>179</td>
    </tr>
    <tr>
      <th>1349350</th>
      <td>84070002</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Dukes and Nantucket</td>
      <td>Massachusetts</td>
      <td>US</td>
      <td>41.406747</td>
      <td>-70.687635</td>
      <td>Dukes and Nantucket,Massachusetts,US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1349351</th>
      <td>84070005</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Federal Correctional Institution (FCI)</td>
      <td>Michigan</td>
      <td>US</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>Federal Correctional Institution (FCI), Michigan, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1349352</th>
      <td>84070004</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Michigan Department of Corrections (MDOC)</td>
      <td>Michigan</td>
      <td>US</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>Michigan Department of Corrections (MDOC), Michigan, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>148</td>
    </tr>
    <tr>
      <th>1349353</th>
      <td>84070003</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Kansas City</td>
      <td>Missouri</td>
      <td>US</td>
      <td>39.099700</td>
      <td>-94.578600</td>
      <td>Kansas City,Missouri,US</td>
      <td>488943</td>
      <td>2021-02-28</td>
      <td>514</td>
    </tr>
    <tr>
      <th>1349354</th>
      <td>84070015</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Bear River</td>
      <td>Utah</td>
      <td>US</td>
      <td>41.521068</td>
      <td>-113.083282</td>
      <td>Bear River, Utah, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1349355</th>
      <td>84070016</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Central Utah</td>
      <td>Utah</td>
      <td>US</td>
      <td>39.372319</td>
      <td>-111.575868</td>
      <td>Central Utah, Utah, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>54</td>
    </tr>
    <tr>
      <th>1349356</th>
      <td>84070017</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Southeast Utah</td>
      <td>Utah</td>
      <td>US</td>
      <td>38.996171</td>
      <td>-110.701396</td>
      <td>Southeast Utah, Utah, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1349357</th>
      <td>84070018</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Southwest Utah</td>
      <td>Utah</td>
      <td>US</td>
      <td>37.854472</td>
      <td>-111.441876</td>
      <td>Southwest Utah, Utah, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>232</td>
    </tr>
    <tr>
      <th>1349358</th>
      <td>84070019</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>TriCounty</td>
      <td>Utah</td>
      <td>US</td>
      <td>40.124915</td>
      <td>-109.517442</td>
      <td>TriCounty, Utah, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>29</td>
    </tr>
    <tr>
      <th>1349359</th>
      <td>84070020</td>
      <td>US</td>
      <td>USA</td>
      <td>840</td>
      <td>NaN</td>
      <td>Weber-Morgan</td>
      <td>Utah</td>
      <td>US</td>
      <td>41.271160</td>
      <td>-111.914512</td>
      <td>Weber-Morgan, Utah, US</td>
      <td>0</td>
      <td>2021-02-28</td>
      <td>180</td>
    </tr>
  </tbody>
</table>