# EDA - COVID-JHU-DLY Files 

#### Column Name [IDX] -  Dtype (Head / Tail) 
- **FIPS** [0] - object (45001 / 56045) 
- **ADMIN2** [1] - object (Abbeville / Weston) 
- **PROVINCE_STATE** [2] - object (SOUTH CAROLINA / WYOMING) 
- **COUNTRY_REGION** [3] - object (US / US) 
- **LAST_UPDATE** [4] - object (2020-05-30 02:32:48 / 2020-10-01 04:23:42) 
- **LAT** [5] - object (34.22333378 / 43.83961191) 
- **LONG** [6] - object (-82.46170658 / -104.5674881) 
- **CONFIRMED** [7] - object (39 / 39) 
- **DEATHS** [8] - object (0 / 0) 
- **RECOVERED** [9] - object (0 / 0) 
- **ACTIVE** [10] - object (39 / 39) 
- **COMBINED_KEY** [11] - object (Abbeville, South Carolina, US / Weston, Wyoming, US) 
- **DATA_DT** [12] - object (2020-05-29 / 2020-09-30) 
- **INCIDENCE_RATE** [13] - object (159.0084396787214 / 563.014291901256) 
- **CASE-FATALITY_RATIO** [14] - object (0.0 / 0.0) 



#### Head / Tail [n=20] Sample 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FIPS</th>
      <th>ADMIN2</th>
      <th>PROVINCE_STATE</th>
      <th>COUNTRY_REGION</th>
      <th>LAST_UPDATE</th>
      <th>LAT</th>
      <th>LONG</th>
      <th>CONFIRMED</th>
      <th>DEATHS</th>
      <th>RECOVERED</th>
      <th>ACTIVE</th>
      <th>COMBINED_KEY</th>
      <th>DATA_DT</th>
      <th>INCIDENCE_RATE</th>
      <th>CASE-FATALITY_RATIO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45001</td>
      <td>Abbeville</td>
      <td>SOUTH CAROLINA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>34.22333378</td>
      <td>-82.46170658</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>39</td>
      <td>Abbeville, South Carolina, US</td>
      <td>2020-05-29</td>
      <td>159.0084396787214</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22001</td>
      <td>Acadia</td>
      <td>LOUISIANA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>30.2950649</td>
      <td>-92.41419698</td>
      <td>401</td>
      <td>23</td>
      <td>0</td>
      <td>378</td>
      <td>Acadia, Louisiana, US</td>
      <td>2020-05-29</td>
      <td>646.305101136272</td>
      <td>5.7356608478802995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>51001</td>
      <td>Accomack</td>
      <td>VIRGINIA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>37.76707161</td>
      <td>-75.63234615</td>
      <td>827</td>
      <td>12</td>
      <td>0</td>
      <td>815</td>
      <td>Accomack, Virginia, US</td>
      <td>2020-05-29</td>
      <td>2559.1038494863224</td>
      <td>1.4510278113663846</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16001</td>
      <td>Ada</td>
      <td>IDAHO</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>43.4526575</td>
      <td>-116.24155159999998</td>
      <td>803</td>
      <td>22</td>
      <td>0</td>
      <td>781</td>
      <td>Ada, Idaho, US</td>
      <td>2020-05-29</td>
      <td>166.7403812810562</td>
      <td>2.73972602739726</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19001</td>
      <td>Adair</td>
      <td>IOWA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>41.33075609</td>
      <td>-94.47105874</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>Adair, Iowa, US</td>
      <td>2020-05-29</td>
      <td>125.83892617449665</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>21001</td>
      <td>Adair</td>
      <td>KENTUCKY</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>37.10459774</td>
      <td>-85.28129668</td>
      <td>97</td>
      <td>19</td>
      <td>0</td>
      <td>78</td>
      <td>Adair, Kentucky, US</td>
      <td>2020-05-29</td>
      <td>505.1557129465681</td>
      <td>19.587628865979383</td>
    </tr>
    <tr>
      <th>6</th>
      <td>29001</td>
      <td>Adair</td>
      <td>MISSOURI</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>40.19058551</td>
      <td>-92.60078167</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>Adair, Missouri, US</td>
      <td>2020-05-29</td>
      <td>197.29313814465533</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>40001</td>
      <td>Adair</td>
      <td>OKLAHOMA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>35.88494195</td>
      <td>-94.65859267</td>
      <td>85</td>
      <td>3</td>
      <td>0</td>
      <td>82</td>
      <td>Adair, Oklahoma, US</td>
      <td>2020-05-29</td>
      <td>382.9863927187528</td>
      <td>3.5294117647058822</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8001</td>
      <td>Adams</td>
      <td>COLORADO</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>39.87432092</td>
      <td>-104.3362578</td>
      <td>3142</td>
      <td>120</td>
      <td>0</td>
      <td>3022</td>
      <td>Adams, Colorado, US</td>
      <td>2020-05-29</td>
      <td>607.2424582689918</td>
      <td>3.819223424570337</td>
    </tr>
    <tr>
      <th>9</th>
      <td>16003</td>
      <td>Adams</td>
      <td>IDAHO</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>44.89333571</td>
      <td>-116.4545247</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>Adams, Idaho, US</td>
      <td>2020-05-29</td>
      <td>69.86492780624127</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>17001</td>
      <td>Adams</td>
      <td>ILLINOIS</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>39.98815591</td>
      <td>-91.18786813</td>
      <td>44</td>
      <td>1</td>
      <td>0</td>
      <td>43</td>
      <td>Adams, Illinois, US</td>
      <td>2020-05-29</td>
      <td>67.24230152059296</td>
      <td>2.272727272727273</td>
    </tr>
    <tr>
      <th>11</th>
      <td>18001</td>
      <td>Adams</td>
      <td>INDIANA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>40.7457653</td>
      <td>-84.93671406</td>
      <td>13</td>
      <td>1</td>
      <td>0</td>
      <td>12</td>
      <td>Adams, Indiana, US</td>
      <td>2020-05-29</td>
      <td>36.3361936439612</td>
      <td>7.6923076923076925</td>
    </tr>
    <tr>
      <th>12</th>
      <td>19003</td>
      <td>Adams</td>
      <td>IOWA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>41.02903567</td>
      <td>-94.69932645</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>Adams, Iowa, US</td>
      <td>2020-05-29</td>
      <td>194.3364797334814</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28001</td>
      <td>Adams</td>
      <td>MISSISSIPPI</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>31.47669768</td>
      <td>-91.35326037</td>
      <td>192</td>
      <td>15</td>
      <td>0</td>
      <td>177</td>
      <td>Adams, Mississippi, US</td>
      <td>2020-05-29</td>
      <td>625.5497996285798</td>
      <td>7.8125</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31001</td>
      <td>Adams</td>
      <td>NEBRASKA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>40.52449420000001</td>
      <td>-98.50117804</td>
      <td>268</td>
      <td>11</td>
      <td>0</td>
      <td>257</td>
      <td>Adams, Nebraska, US</td>
      <td>2020-05-29</td>
      <td>854.5100915091031</td>
      <td>4.104477611940299</td>
    </tr>
    <tr>
      <th>15</th>
      <td>39001</td>
      <td>Adams</td>
      <td>OHIO</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>38.84541072</td>
      <td>-83.4718964</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>Adams, Ohio, US</td>
      <td>2020-05-29</td>
      <td>32.493320817387534</td>
      <td>11.11111111111111</td>
    </tr>
    <tr>
      <th>16</th>
      <td>42001</td>
      <td>Adams</td>
      <td>PENNSYLVANIA</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>39.87140411</td>
      <td>-77.21610347</td>
      <td>241</td>
      <td>7</td>
      <td>0</td>
      <td>234</td>
      <td>Adams, Pennsylvania, US</td>
      <td>2020-05-29</td>
      <td>233.96013940529468</td>
      <td>2.904564315352697</td>
    </tr>
    <tr>
      <th>17</th>
      <td>53001</td>
      <td>Adams</td>
      <td>WASHINGTON</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>46.98299757</td>
      <td>-118.5601734</td>
      <td>59</td>
      <td>0</td>
      <td>0</td>
      <td>59</td>
      <td>Adams, Washington, US</td>
      <td>2020-05-29</td>
      <td>295.250963318821</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>55001</td>
      <td>Adams</td>
      <td>WISCONSIN</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>43.96974651</td>
      <td>-89.76782777</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Adams, Wisconsin, US</td>
      <td>2020-05-29</td>
      <td>19.782393669634025</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>50001</td>
      <td>Addison</td>
      <td>VERMONT</td>
      <td>US</td>
      <td>2020-05-30 02:32:48</td>
      <td>44.03217337</td>
      <td>-73.14130877</td>
      <td>62</td>
      <td>2</td>
      <td>0</td>
      <td>60</td>
      <td>Addison, Vermont, US</td>
      <td>2020-05-29</td>
      <td>168.58362563558745</td>
      <td>3.225806451612903</td>
    </tr>
    <tr>
      <th>3884</th>
      <td>56007</td>
      <td>Carbon</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>41.69357844</td>
      <td>-106.9326084</td>
      <td>231</td>
      <td>2</td>
      <td>0</td>
      <td>229</td>
      <td>Carbon, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>1560.8108108108108</td>
      <td>0.8658008658008658</td>
    </tr>
    <tr>
      <th>3885</th>
      <td>56009</td>
      <td>Converse</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>42.97272268</td>
      <td>-105.5081848</td>
      <td>132</td>
      <td>0</td>
      <td>0</td>
      <td>132</td>
      <td>Converse, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>954.9992765156996</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3886</th>
      <td>56011</td>
      <td>Crook</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>44.58855102</td>
      <td>-104.5697705</td>
      <td>47</td>
      <td>0</td>
      <td>0</td>
      <td>47</td>
      <td>Crook, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>619.7257383966245</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3887</th>
      <td>56013</td>
      <td>Fremont</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>43.04183996</td>
      <td>-108.6296893</td>
      <td>741</td>
      <td>14</td>
      <td>0</td>
      <td>727</td>
      <td>Fremont, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>1887.369144953007</td>
      <td>1.8893387314439947</td>
    </tr>
    <tr>
      <th>3888</th>
      <td>56015</td>
      <td>Goshen</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>42.08798185</td>
      <td>-104.3534743</td>
      <td>106</td>
      <td>2</td>
      <td>0</td>
      <td>104</td>
      <td>Goshen, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>802.3616683067141</td>
      <td>1.8867924528301887</td>
    </tr>
    <tr>
      <th>3889</th>
      <td>56017</td>
      <td>Hot Springs</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>43.71930657</td>
      <td>-108.4423174</td>
      <td>38</td>
      <td>0</td>
      <td>0</td>
      <td>38</td>
      <td>Hot Springs, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>861.0922275096308</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3890</th>
      <td>56019</td>
      <td>Johnson</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>44.04057166</td>
      <td>-106.5845174</td>
      <td>40</td>
      <td>1</td>
      <td>0</td>
      <td>39</td>
      <td>Johnson, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>473.6530491415039</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>3891</th>
      <td>56021</td>
      <td>Laramie</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>41.30702520000001</td>
      <td>-104.6887497</td>
      <td>718</td>
      <td>4</td>
      <td>0</td>
      <td>714</td>
      <td>Laramie, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>721.608040201005</td>
      <td>0.5571030640668524</td>
    </tr>
    <tr>
      <th>3892</th>
      <td>56023</td>
      <td>Lincoln</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>42.26376367</td>
      <td>-110.6563997</td>
      <td>208</td>
      <td>1</td>
      <td>0</td>
      <td>207</td>
      <td>Lincoln, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>1048.915784165406</td>
      <td>0.4807692307692308</td>
    </tr>
    <tr>
      <th>3893</th>
      <td>56025</td>
      <td>Natrona</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>42.96180148</td>
      <td>-106.797885</td>
      <td>603</td>
      <td>4</td>
      <td>0</td>
      <td>599</td>
      <td>Natrona, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>755.0902852563298</td>
      <td>0.6633499170812603</td>
    </tr>
    <tr>
      <th>3894</th>
      <td>56027</td>
      <td>Niobrara</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>43.05607708</td>
      <td>-104.4758896</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>Niobrara, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>169.77928692699493</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3895</th>
      <td>56029</td>
      <td>Park</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>44.52157546</td>
      <td>-109.5852825</td>
      <td>245</td>
      <td>2</td>
      <td>0</td>
      <td>243</td>
      <td>Park, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>839.2135370281565</td>
      <td>0.8163265306122449</td>
    </tr>
    <tr>
      <th>3896</th>
      <td>56031</td>
      <td>Platte</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>42.13299116</td>
      <td>-104.966331</td>
      <td>33</td>
      <td>1</td>
      <td>0</td>
      <td>32</td>
      <td>Platte, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>393.18479685452166</td>
      <td>3.0303030303030303</td>
    </tr>
    <tr>
      <th>3897</th>
      <td>56033</td>
      <td>Sheridan</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>44.79048913</td>
      <td>-106.8862389</td>
      <td>296</td>
      <td>4</td>
      <td>0</td>
      <td>292</td>
      <td>Sheridan, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>970.9693291782843</td>
      <td>1.3513513513513513</td>
    </tr>
    <tr>
      <th>3898</th>
      <td>56035</td>
      <td>Sublette</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>42.76558279</td>
      <td>-109.9130922</td>
      <td>116</td>
      <td>1</td>
      <td>0</td>
      <td>115</td>
      <td>Sublette, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>1179.9410029498524</td>
      <td>0.8620689655172413</td>
    </tr>
    <tr>
      <th>3899</th>
      <td>56037</td>
      <td>Sweetwater</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>41.65943896</td>
      <td>-108.8827882</td>
      <td>339</td>
      <td>2</td>
      <td>0</td>
      <td>337</td>
      <td>Sweetwater, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>800.604586354297</td>
      <td>0.5899705014749262</td>
    </tr>
    <tr>
      <th>3900</th>
      <td>56039</td>
      <td>Teton</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>43.93522482</td>
      <td>-110.5890801</td>
      <td>577</td>
      <td>1</td>
      <td>0</td>
      <td>576</td>
      <td>Teton, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>2459.0862598022504</td>
      <td>0.1733102253032929</td>
    </tr>
    <tr>
      <th>3901</th>
      <td>56041</td>
      <td>Uinta</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>41.2878183</td>
      <td>-110.54757820000002</td>
      <td>357</td>
      <td>2</td>
      <td>0</td>
      <td>355</td>
      <td>Uinta, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>1765.054879857609</td>
      <td>0.5602240896358543</td>
    </tr>
    <tr>
      <th>3903</th>
      <td>56043</td>
      <td>Washakie</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>43.90451606</td>
      <td>-107.68018700000002</td>
      <td>116</td>
      <td>6</td>
      <td>0</td>
      <td>110</td>
      <td>Washakie, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>1486.2267777065986</td>
      <td>5.172413793103448</td>
    </tr>
    <tr>
      <th>3904</th>
      <td>56045</td>
      <td>Weston</td>
      <td>WYOMING</td>
      <td>US</td>
      <td>2020-10-01 04:23:42</td>
      <td>43.83961191</td>
      <td>-104.5674881</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>39</td>
      <td>Weston, Wyoming, US</td>
      <td>2020-09-30</td>
      <td>563.014291901256</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>