# EDA - COVID-JHU-DLY Files 

#### Column Name [IDX] -  Dtype (Head / Tail) 
- **FIPS** [0] - float64 (45001.0 / nan) 
- **ADMIN2** [1] - object (Abbeville / nan) 
- **PROVINCE_STATE** [2] - object (South Carolina / nan) 
- **COUNTRY_REGION** [3] - object (US / Zimbabwe) 
- **LAST_UPDATE** [4] - object (2020-04-12 23:18:00 / 2020-10-01 04:23:42) 
- **LAT** [5] - float64 (34.22333378 / -19.015438) 
- **LONG** [6] - float64 (-82.46170658 / 29.154857) 
- **CONFIRMED** [7] - int64 (9 / 7838) 
- **DEATHS** [8] - int64 (0 / 228) 
- **RECOVERED** [9] - int64 (0 / 6303) 
- **ACTIVE** [10] - float64 (9.0 / 1307.0) 
- **COMBINED_KEY** [11] - object (Abbeville, South Carolina, US / Zimbabwe) 
- **DATA_DT** [12] - object (2020-04-12 / 2020-09-30) 
- **INCIDENCE_RATE** [13] - float64 (nan / 52.73523848969991) 
- **CASE-FATALITY_RATIO** [14] - float64 (nan / 2.9089053329931103) 



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
      <td>45001.0</td>
      <td>Abbeville</td>
      <td>South Carolina</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>34.223334</td>
      <td>-82.461707</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>9.0</td>
      <td>Abbeville, South Carolina, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22001.0</td>
      <td>Acadia</td>
      <td>Louisiana</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>30.295065</td>
      <td>-92.414197</td>
      <td>99</td>
      <td>5</td>
      <td>0</td>
      <td>94.0</td>
      <td>Acadia, Louisiana, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>51001.0</td>
      <td>Accomack</td>
      <td>Virginia</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>37.767072</td>
      <td>-75.632346</td>
      <td>15</td>
      <td>0</td>
      <td>0</td>
      <td>15.0</td>
      <td>Accomack, Virginia, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16001.0</td>
      <td>Ada</td>
      <td>Idaho</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>43.452658</td>
      <td>-116.241552</td>
      <td>517</td>
      <td>6</td>
      <td>0</td>
      <td>511.0</td>
      <td>Ada, Idaho, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19001.0</td>
      <td>Adair</td>
      <td>Iowa</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>41.330756</td>
      <td>-94.471059</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>Adair, Iowa, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>21001.0</td>
      <td>Adair</td>
      <td>Kentucky</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>37.104598</td>
      <td>-85.281297</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>11.0</td>
      <td>Adair, Kentucky, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>29001.0</td>
      <td>Adair</td>
      <td>Missouri</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>40.190586</td>
      <td>-92.600782</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>11.0</td>
      <td>Adair, Missouri, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>40001.0</td>
      <td>Adair</td>
      <td>Oklahoma</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>35.884942</td>
      <td>-94.658593</td>
      <td>27</td>
      <td>2</td>
      <td>0</td>
      <td>25.0</td>
      <td>Adair, Oklahoma, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8001.0</td>
      <td>Adams</td>
      <td>Colorado</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>39.874321</td>
      <td>-104.336258</td>
      <td>647</td>
      <td>26</td>
      <td>0</td>
      <td>621.0</td>
      <td>Adams, Colorado, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>16003.0</td>
      <td>Adams</td>
      <td>Idaho</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>44.893336</td>
      <td>-116.454525</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>Adams, Idaho, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>17001.0</td>
      <td>Adams</td>
      <td>Illinois</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>39.988156</td>
      <td>-91.187868</td>
      <td>25</td>
      <td>0</td>
      <td>0</td>
      <td>25.0</td>
      <td>Adams, Illinois, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>18001.0</td>
      <td>Adams</td>
      <td>Indiana</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>40.745765</td>
      <td>-84.936714</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>4.0</td>
      <td>Adams, Indiana, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>28001.0</td>
      <td>Adams</td>
      <td>Mississippi</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>31.476698</td>
      <td>-91.353260</td>
      <td>51</td>
      <td>1</td>
      <td>0</td>
      <td>50.0</td>
      <td>Adams, Mississippi, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31001.0</td>
      <td>Adams</td>
      <td>Nebraska</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>40.524494</td>
      <td>-98.501178</td>
      <td>54</td>
      <td>0</td>
      <td>0</td>
      <td>54.0</td>
      <td>Adams, Nebraska, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>39001.0</td>
      <td>Adams</td>
      <td>Ohio</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>38.845411</td>
      <td>-83.471896</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
      <td>Adams, Ohio, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42001.0</td>
      <td>Adams</td>
      <td>Pennsylvania</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>39.871404</td>
      <td>-77.216103</td>
      <td>48</td>
      <td>1</td>
      <td>0</td>
      <td>47.0</td>
      <td>Adams, Pennsylvania, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>53001.0</td>
      <td>Adams</td>
      <td>Washington</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>46.982998</td>
      <td>-118.560173</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>36.0</td>
      <td>Adams, Washington, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>55001.0</td>
      <td>Adams</td>
      <td>Wisconsin</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>43.969747</td>
      <td>-89.767828</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>2.0</td>
      <td>Adams, Wisconsin, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>50001.0</td>
      <td>Addison</td>
      <td>Vermont</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>44.032173</td>
      <td>-73.141309</td>
      <td>55</td>
      <td>1</td>
      <td>0</td>
      <td>54.0</td>
      <td>Addison, Vermont, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>45003.0</td>
      <td>Aiken</td>
      <td>South Carolina</td>
      <td>US</td>
      <td>2020-04-12 23:18:00</td>
      <td>33.543380</td>
      <td>-81.636454</td>
      <td>50</td>
      <td>1</td>
      <td>0</td>
      <td>49.0</td>
      <td>Aiken, South Carolina, US</td>
      <td>2020-04-12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3938</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Channel Islands</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>49.372300</td>
      <td>-2.364400</td>
      <td>665</td>
      <td>48</td>
      <td>600</td>
      <td>17.0</td>
      <td>Channel Islands, United Kingdom</td>
      <td>2020-09-30</td>
      <td>390.031613</td>
      <td>7.218045</td>
    </tr>
    <tr>
      <th>3939</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>England</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>52.355500</td>
      <td>-1.174300</td>
      <td>388342</td>
      <td>37429</td>
      <td>0</td>
      <td>350913.0</td>
      <td>England, United Kingdom</td>
      <td>2020-09-30</td>
      <td>693.750313</td>
      <td>9.638154</td>
    </tr>
    <tr>
      <th>3940</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Falkland Islands (Malvinas)</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>-51.796300</td>
      <td>-59.523600</td>
      <td>13</td>
      <td>0</td>
      <td>13</td>
      <td>0.0</td>
      <td>Falkland Islands (Malvinas), United Kingdom</td>
      <td>2020-09-30</td>
      <td>373.241459</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3941</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Gibraltar</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>36.140800</td>
      <td>-5.353600</td>
      <td>396</td>
      <td>0</td>
      <td>344</td>
      <td>52.0</td>
      <td>Gibraltar, United Kingdom</td>
      <td>2020-09-30</td>
      <td>1175.388086</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3942</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Isle of Man</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>54.236100</td>
      <td>-4.548100</td>
      <td>340</td>
      <td>24</td>
      <td>315</td>
      <td>1.0</td>
      <td>Isle of Man, United Kingdom</td>
      <td>2020-09-30</td>
      <td>399.849468</td>
      <td>7.058824</td>
    </tr>
    <tr>
      <th>3943</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Montserrat</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>16.742498</td>
      <td>-62.187366</td>
      <td>13</td>
      <td>1</td>
      <td>12</td>
      <td>0.0</td>
      <td>Montserrat, United Kingdom</td>
      <td>2020-09-30</td>
      <td>260.052010</td>
      <td>7.692308</td>
    </tr>
    <tr>
      <th>3944</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Northern Ireland</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>54.787700</td>
      <td>-6.492300</td>
      <td>11693</td>
      <td>579</td>
      <td>0</td>
      <td>11114.0</td>
      <td>Northern Ireland, United Kingdom</td>
      <td>2020-09-30</td>
      <td>621.439201</td>
      <td>4.951680</td>
    </tr>
    <tr>
      <th>3945</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Saint Helena, Ascension and Tristan da Cunha</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>-7.946700</td>
      <td>-14.355900</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0.0</td>
      <td>Saint Helena, Ascension and Tristan da Cunha, United Kingdom</td>
      <td>2020-09-30</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3946</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Scotland</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>56.490700</td>
      <td>-4.202600</td>
      <td>29244</td>
      <td>2519</td>
      <td>0</td>
      <td>26725.0</td>
      <td>Scotland, United Kingdom</td>
      <td>2020-09-30</td>
      <td>535.280874</td>
      <td>8.613733</td>
    </tr>
    <tr>
      <th>3947</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Turks and Caicos Islands</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>21.694000</td>
      <td>-71.797900</td>
      <td>689</td>
      <td>6</td>
      <td>645</td>
      <td>38.0</td>
      <td>Turks and Caicos Islands, United Kingdom</td>
      <td>2020-09-30</td>
      <td>1779.534067</td>
      <td>0.870827</td>
    </tr>
    <tr>
      <th>3948</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>Unknown, United Kingdom</td>
      <td>2020-09-30</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3949</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Wales</td>
      <td>United Kingdom</td>
      <td>2020-10-01 04:23:42</td>
      <td>52.130700</td>
      <td>-3.783700</td>
      <td>23985</td>
      <td>1616</td>
      <td>0</td>
      <td>22369.0</td>
      <td>Wales, United Kingdom</td>
      <td>2020-09-30</td>
      <td>764.194227</td>
      <td>6.737544</td>
    </tr>
    <tr>
      <th>3950</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Uruguay</td>
      <td>2020-10-01 04:23:42</td>
      <td>-32.522800</td>
      <td>-55.765800</td>
      <td>2046</td>
      <td>48</td>
      <td>1791</td>
      <td>207.0</td>
      <td>Uruguay</td>
      <td>2020-09-30</td>
      <td>58.899274</td>
      <td>2.346041</td>
    </tr>
    <tr>
      <th>3951</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Uzbekistan</td>
      <td>2020-10-01 04:23:42</td>
      <td>41.377491</td>
      <td>64.585262</td>
      <td>56717</td>
      <td>470</td>
      <td>53366</td>
      <td>2881.0</td>
      <td>Uzbekistan</td>
      <td>2020-09-30</td>
      <td>169.460285</td>
      <td>0.828676</td>
    </tr>
    <tr>
      <th>3952</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Venezuela</td>
      <td>2020-10-01 04:23:42</td>
      <td>6.423800</td>
      <td>-66.589700</td>
      <td>75122</td>
      <td>628</td>
      <td>65225</td>
      <td>9269.0</td>
      <td>Venezuela</td>
      <td>2020-09-30</td>
      <td>264.179739</td>
      <td>0.835973</td>
    </tr>
    <tr>
      <th>3953</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Vietnam</td>
      <td>2020-10-01 04:23:42</td>
      <td>14.058324</td>
      <td>108.277199</td>
      <td>1094</td>
      <td>35</td>
      <td>1010</td>
      <td>49.0</td>
      <td>Vietnam</td>
      <td>2020-09-30</td>
      <td>1.123912</td>
      <td>3.199269</td>
    </tr>
    <tr>
      <th>3954</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>West Bank and Gaza</td>
      <td>2020-10-01 04:23:42</td>
      <td>31.952200</td>
      <td>35.233200</td>
      <td>39899</td>
      <td>311</td>
      <td>31743</td>
      <td>7845.0</td>
      <td>West Bank and Gaza</td>
      <td>2020-09-30</td>
      <td>782.116181</td>
      <td>0.779468</td>
    </tr>
    <tr>
      <th>3955</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Yemen</td>
      <td>2020-10-01 04:23:42</td>
      <td>15.552727</td>
      <td>48.516388</td>
      <td>2034</td>
      <td>587</td>
      <td>1286</td>
      <td>161.0</td>
      <td>Yemen</td>
      <td>2020-09-30</td>
      <td>6.819561</td>
      <td>28.859390</td>
    </tr>
    <tr>
      <th>3956</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Zambia</td>
      <td>2020-10-01 04:23:42</td>
      <td>-13.133897</td>
      <td>27.849332</td>
      <td>14759</td>
      <td>332</td>
      <td>13959</td>
      <td>468.0</td>
      <td>Zambia</td>
      <td>2020-09-30</td>
      <td>80.281959</td>
      <td>2.249475</td>
    </tr>
    <tr>
      <th>3957</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Zimbabwe</td>
      <td>2020-10-01 04:23:42</td>
      <td>-19.015438</td>
      <td>29.154857</td>
      <td>7838</td>
      <td>228</td>
      <td>6303</td>
      <td>1307.0</td>
      <td>Zimbabwe</td>
      <td>2020-09-30</td>
      <td>52.735238</td>
      <td>2.908905</td>
    </tr>
  </tbody>
</table>