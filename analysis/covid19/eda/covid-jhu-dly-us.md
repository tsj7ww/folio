# EDA - COVID-JHU-DLY-US Files 

#### Column Name [IDX] -  Dtype (Head / Tail) 
- **PROVINCE_STATE** [0] - object (Alabama / Wyoming) 
- **COUNTRY_REGION** [1] - object (US / US) 
- **LAST_UPDATE** [2] - object (2020-04-12 23:18:15 / 2020-10-01 04:30:28) 
- **LAT** [3] - float64 (32.3182 / 42.756) 
- **LONG** [4] - float64 (-86.9023 / -107.3025) 
- **CONFIRMED** [5] - int64 (3563 / 5948) 
- **DEATHS** [6] - int64 (93 / 50) 
- **RECOVERED** [7] - float64 (nan / 4791.0) 
- **ACTIVE** [8] - float64 (3470.0 / 1107.0) 
- **FIPS** [9] - float64 (1.0 / 56.0) 
- **INCIDENT_RATE** [10] - float64 (75.98802021 / 1027.71619966169) 
- **PEOPLE_TESTED** [11] - float64 (21583.0 / 101160.0) 
- **PEOPLE_HOSPITALIZED** [12] - float64 (437.0 / nan) 
- **MORTALITY_RATE** [13] - float64 (2.610159978 / 0.8406186953597848) 
- **UID** [14] - float64 (84000001.0 / 84000056.0) 
- **ISO3** [15] - object (USA / USA) 
- **TESTING_RATE** [16] - float64 (460.3001516 / 17478.777867817174) 
- **HOSPITALIZATION_RATE** [17] - float64 (12.26494527 / nan) 
- **DATA_DT** [18] - object (20200412 / 20200930) 



#### Head / Tail [n=20] Sample 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PROVINCE_STATE</th>
      <th>COUNTRY_REGION</th>
      <th>LAST_UPDATE</th>
      <th>LAT</th>
      <th>LONG</th>
      <th>CONFIRMED</th>
      <th>DEATHS</th>
      <th>RECOVERED</th>
      <th>ACTIVE</th>
      <th>FIPS</th>
      <th>INCIDENT_RATE</th>
      <th>PEOPLE_TESTED</th>
      <th>PEOPLE_HOSPITALIZED</th>
      <th>MORTALITY_RATE</th>
      <th>UID</th>
      <th>ISO3</th>
      <th>TESTING_RATE</th>
      <th>HOSPITALIZATION_RATE</th>
      <th>DATA_DT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>32.3182</td>
      <td>-86.9023</td>
      <td>3563</td>
      <td>93</td>
      <td>NaN</td>
      <td>3470.0</td>
      <td>1.0</td>
      <td>75.988020</td>
      <td>21583.0</td>
      <td>437.0</td>
      <td>2.610160</td>
      <td>84000001.0</td>
      <td>USA</td>
      <td>460.300152</td>
      <td>12.264945</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alaska</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>61.3707</td>
      <td>-152.4044</td>
      <td>272</td>
      <td>8</td>
      <td>66.0</td>
      <td>264.0</td>
      <td>2.0</td>
      <td>45.504049</td>
      <td>8038.0</td>
      <td>31.0</td>
      <td>2.941176</td>
      <td>84000002.0</td>
      <td>USA</td>
      <td>1344.711576</td>
      <td>11.397059</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arizona</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>33.7298</td>
      <td>-111.4312</td>
      <td>3542</td>
      <td>115</td>
      <td>NaN</td>
      <td>3427.0</td>
      <td>4.0</td>
      <td>48.662422</td>
      <td>42109.0</td>
      <td>NaN</td>
      <td>3.246753</td>
      <td>84000004.0</td>
      <td>USA</td>
      <td>578.522286</td>
      <td>NaN</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arkansas</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>34.9697</td>
      <td>-92.3731</td>
      <td>1280</td>
      <td>27</td>
      <td>367.0</td>
      <td>1253.0</td>
      <td>5.0</td>
      <td>49.439423</td>
      <td>19722.0</td>
      <td>130.0</td>
      <td>2.109375</td>
      <td>84000005.0</td>
      <td>USA</td>
      <td>761.753354</td>
      <td>10.156250</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>4</th>
      <td>California</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>36.1162</td>
      <td>-119.6816</td>
      <td>22795</td>
      <td>640</td>
      <td>NaN</td>
      <td>22155.0</td>
      <td>6.0</td>
      <td>58.137726</td>
      <td>190328.0</td>
      <td>5234.0</td>
      <td>2.812020</td>
      <td>84000006.0</td>
      <td>USA</td>
      <td>485.423868</td>
      <td>22.961176</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Colorado</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>39.0598</td>
      <td>-105.3111</td>
      <td>7307</td>
      <td>289</td>
      <td>NaN</td>
      <td>7018.0</td>
      <td>8.0</td>
      <td>128.943729</td>
      <td>34873.0</td>
      <td>1376.0</td>
      <td>3.955112</td>
      <td>84000008.0</td>
      <td>USA</td>
      <td>615.389991</td>
      <td>18.831258</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Connecticut</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>41.5978</td>
      <td>-72.7554</td>
      <td>12035</td>
      <td>554</td>
      <td>NaN</td>
      <td>11481.0</td>
      <td>9.0</td>
      <td>337.560483</td>
      <td>41220.0</td>
      <td>1654.0</td>
      <td>4.603241</td>
      <td>84000009.0</td>
      <td>USA</td>
      <td>1156.148159</td>
      <td>13.743249</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Delaware</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>39.3185</td>
      <td>-75.5071</td>
      <td>1625</td>
      <td>35</td>
      <td>191.0</td>
      <td>1590.0</td>
      <td>10.0</td>
      <td>166.878217</td>
      <td>11103.0</td>
      <td>190.0</td>
      <td>2.153846</td>
      <td>84000010.0</td>
      <td>USA</td>
      <td>1140.214672</td>
      <td>11.692308</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Diamond Princess</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>49</td>
      <td>0</td>
      <td>0.0</td>
      <td>49.0</td>
      <td>888.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>84088888.0</td>
      <td>USA</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>9</th>
      <td>District of Columbia</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>38.8974</td>
      <td>-77.0268</td>
      <td>1875</td>
      <td>50</td>
      <td>493.0</td>
      <td>1825.0</td>
      <td>11.0</td>
      <td>265.675190</td>
      <td>10640.0</td>
      <td>NaN</td>
      <td>2.666667</td>
      <td>84000011.0</td>
      <td>USA</td>
      <td>1507.618148</td>
      <td>NaN</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Florida</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>27.7663</td>
      <td>-81.6868</td>
      <td>19895</td>
      <td>461</td>
      <td>NaN</td>
      <td>19434.0</td>
      <td>12.0</td>
      <td>93.700227</td>
      <td>182753.0</td>
      <td>2772.0</td>
      <td>2.317165</td>
      <td>84000012.0</td>
      <td>USA</td>
      <td>860.718651</td>
      <td>13.933149</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Georgia</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>33.0406</td>
      <td>-83.6431</td>
      <td>12452</td>
      <td>433</td>
      <td>NaN</td>
      <td>12019.0</td>
      <td>13.0</td>
      <td>122.808141</td>
      <td>54453.0</td>
      <td>2505.0</td>
      <td>3.477353</td>
      <td>84000013.0</td>
      <td>USA</td>
      <td>537.043983</td>
      <td>20.117250</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Grand Princess</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>103</td>
      <td>0</td>
      <td>0.0</td>
      <td>103.0</td>
      <td>999.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>84099999.0</td>
      <td>USA</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Guam</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>13.4443</td>
      <td>144.7937</td>
      <td>133</td>
      <td>5</td>
      <td>58.0</td>
      <td>128.0</td>
      <td>66.0</td>
      <td>80.984479</td>
      <td>826.0</td>
      <td>13.0</td>
      <td>3.759398</td>
      <td>316.0</td>
      <td>GUM</td>
      <td>502.956238</td>
      <td>9.774436</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Hawaii</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>21.0943</td>
      <td>-157.4983</td>
      <td>499</td>
      <td>9</td>
      <td>300.0</td>
      <td>490.0</td>
      <td>15.0</td>
      <td>35.245440</td>
      <td>17968.0</td>
      <td>44.0</td>
      <td>1.803607</td>
      <td>84000015.0</td>
      <td>USA</td>
      <td>1269.118355</td>
      <td>8.817635</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Idaho</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>44.2405</td>
      <td>-114.4788</td>
      <td>1407</td>
      <td>27</td>
      <td>NaN</td>
      <td>1380.0</td>
      <td>16.0</td>
      <td>87.364335</td>
      <td>14308.0</td>
      <td>131.0</td>
      <td>1.918977</td>
      <td>84000016.0</td>
      <td>USA</td>
      <td>888.421400</td>
      <td>9.310590</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Illinois</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>40.3495</td>
      <td>-88.9861</td>
      <td>20852</td>
      <td>720</td>
      <td>NaN</td>
      <td>20132.0</td>
      <td>17.0</td>
      <td>177.680782</td>
      <td>100735.0</td>
      <td>3680.0</td>
      <td>3.452906</td>
      <td>84000017.0</td>
      <td>USA</td>
      <td>858.367234</td>
      <td>17.648187</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Indiana</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>39.8494</td>
      <td>-86.2583</td>
      <td>7928</td>
      <td>343</td>
      <td>NaN</td>
      <td>7585.0</td>
      <td>18.0</td>
      <td>121.149255</td>
      <td>42489.0</td>
      <td>NaN</td>
      <td>4.326438</td>
      <td>84000018.0</td>
      <td>USA</td>
      <td>649.282380</td>
      <td>NaN</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Iowa</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>42.0115</td>
      <td>-93.2105</td>
      <td>1587</td>
      <td>41</td>
      <td>674.0</td>
      <td>1546.0</td>
      <td>19.0</td>
      <td>60.556040</td>
      <td>17592.0</td>
      <td>129.0</td>
      <td>2.583491</td>
      <td>84000019.0</td>
      <td>USA</td>
      <td>671.267705</td>
      <td>8.128544</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Kansas</td>
      <td>US</td>
      <td>2020-04-12 23:18:15</td>
      <td>38.5266</td>
      <td>-96.7265</td>
      <td>1344</td>
      <td>56</td>
      <td>NaN</td>
      <td>1288.0</td>
      <td>20.0</td>
      <td>55.116121</td>
      <td>13253.0</td>
      <td>298.0</td>
      <td>4.166667</td>
      <td>84000020.0</td>
      <td>USA</td>
      <td>543.492525</td>
      <td>22.172619</td>
      <td>20200412</td>
    </tr>
    <tr>
      <th>38</th>
      <td>North Dakota</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>47.5289</td>
      <td>-99.7840</td>
      <td>21846</td>
      <td>246</td>
      <td>17938.0</td>
      <td>3662.0</td>
      <td>38.0</td>
      <td>2866.695886</td>
      <td>613487.0</td>
      <td>NaN</td>
      <td>1.126064</td>
      <td>84000038.0</td>
      <td>USA</td>
      <td>80503.554829</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Northern Mariana Islands</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>15.0979</td>
      <td>145.6739</td>
      <td>70</td>
      <td>2</td>
      <td>29.0</td>
      <td>39.0</td>
      <td>69.0</td>
      <td>126.940374</td>
      <td>15182.0</td>
      <td>NaN</td>
      <td>2.857143</td>
      <td>580.0</td>
      <td>MNP</td>
      <td>27531.553750</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ohio</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>40.3888</td>
      <td>-82.7649</td>
      <td>153987</td>
      <td>4804</td>
      <td>132980.0</td>
      <td>16203.0</td>
      <td>39.0</td>
      <td>1317.355485</td>
      <td>3165935.0</td>
      <td>NaN</td>
      <td>3.119744</td>
      <td>84000039.0</td>
      <td>USA</td>
      <td>27084.506078</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Oklahoma</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>35.5653</td>
      <td>-96.9289</td>
      <td>87199</td>
      <td>1031</td>
      <td>73100.0</td>
      <td>13068.0</td>
      <td>40.0</td>
      <td>2203.680543</td>
      <td>1204028.0</td>
      <td>NaN</td>
      <td>1.182353</td>
      <td>84000040.0</td>
      <td>USA</td>
      <td>30428.021838</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Oregon</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>44.5720</td>
      <td>-122.0709</td>
      <td>33509</td>
      <td>559</td>
      <td>5720.0</td>
      <td>27230.0</td>
      <td>41.0</td>
      <td>794.478176</td>
      <td>685873.0</td>
      <td>NaN</td>
      <td>1.668209</td>
      <td>84000041.0</td>
      <td>USA</td>
      <td>16261.635090</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Pennsylvania</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>40.5908</td>
      <td>-77.2098</td>
      <td>164099</td>
      <td>8130</td>
      <td>130352.0</td>
      <td>25617.0</td>
      <td>42.0</td>
      <td>1281.824254</td>
      <td>2038094.0</td>
      <td>NaN</td>
      <td>4.954326</td>
      <td>84000042.0</td>
      <td>USA</td>
      <td>15920.135535</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Puerto Rico</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>18.2208</td>
      <td>-66.5901</td>
      <td>48755</td>
      <td>661</td>
      <td>NaN</td>
      <td>48094.0</td>
      <td>72.0</td>
      <td>1662.059966</td>
      <td>354727.0</td>
      <td>NaN</td>
      <td>1.355758</td>
      <td>630.0</td>
      <td>PRI</td>
      <td>12092.658096</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Rhode Island</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>41.6809</td>
      <td>-71.5118</td>
      <td>24748</td>
      <td>1114</td>
      <td>2322.0</td>
      <td>21312.0</td>
      <td>44.0</td>
      <td>2336.125268</td>
      <td>769822.0</td>
      <td>NaN</td>
      <td>4.501374</td>
      <td>84000044.0</td>
      <td>USA</td>
      <td>72668.523761</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>46</th>
      <td>South Carolina</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>33.8569</td>
      <td>-80.9450</td>
      <td>147942</td>
      <td>3378</td>
      <td>71691.0</td>
      <td>72873.0</td>
      <td>45.0</td>
      <td>2873.377702</td>
      <td>1309098.0</td>
      <td>NaN</td>
      <td>2.283327</td>
      <td>84000045.0</td>
      <td>USA</td>
      <td>25425.727667</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>47</th>
      <td>South Dakota</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>44.2998</td>
      <td>-99.4388</td>
      <td>22389</td>
      <td>223</td>
      <td>18508.0</td>
      <td>3658.0</td>
      <td>46.0</td>
      <td>2530.805655</td>
      <td>190769.0</td>
      <td>NaN</td>
      <td>0.996025</td>
      <td>84000046.0</td>
      <td>USA</td>
      <td>21564.128099</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Tennessee</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>35.7478</td>
      <td>-86.6923</td>
      <td>196139</td>
      <td>2454</td>
      <td>179322.0</td>
      <td>14363.0</td>
      <td>47.0</td>
      <td>2872.075012</td>
      <td>2884356.0</td>
      <td>NaN</td>
      <td>1.251154</td>
      <td>84000047.0</td>
      <td>USA</td>
      <td>42235.796013</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Texas</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>31.0545</td>
      <td>-97.5635</td>
      <td>773019</td>
      <td>16016</td>
      <td>664883.0</td>
      <td>92120.0</td>
      <td>48.0</td>
      <td>2665.961417</td>
      <td>6237157.0</td>
      <td>NaN</td>
      <td>2.071877</td>
      <td>84000048.0</td>
      <td>USA</td>
      <td>21510.493163</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Utah</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>40.1500</td>
      <td>-111.8624</td>
      <td>73042</td>
      <td>459</td>
      <td>55141.0</td>
      <td>17442.0</td>
      <td>49.0</td>
      <td>2278.320552</td>
      <td>829970.0</td>
      <td>NaN</td>
      <td>0.628406</td>
      <td>84000049.0</td>
      <td>USA</td>
      <td>25888.361607</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Vermont</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>44.0459</td>
      <td>-72.7107</td>
      <td>1752</td>
      <td>58</td>
      <td>1606.0</td>
      <td>88.0</td>
      <td>50.0</td>
      <td>280.774180</td>
      <td>162727.0</td>
      <td>NaN</td>
      <td>3.310502</td>
      <td>84000050.0</td>
      <td>USA</td>
      <td>26078.504589</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Virgin Islands</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>18.3358</td>
      <td>-64.8963</td>
      <td>1318</td>
      <td>20</td>
      <td>1254.0</td>
      <td>44.0</td>
      <td>78.0</td>
      <td>1228.698214</td>
      <td>20561.0</td>
      <td>NaN</td>
      <td>1.517451</td>
      <td>850.0</td>
      <td>VIR</td>
      <td>19167.878584</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Virginia</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>37.7693</td>
      <td>-78.1700</td>
      <td>148092</td>
      <td>3205</td>
      <td>17633.0</td>
      <td>127254.0</td>
      <td>51.0</td>
      <td>1735.008732</td>
      <td>2049988.0</td>
      <td>NaN</td>
      <td>2.164195</td>
      <td>84000051.0</td>
      <td>USA</td>
      <td>24017.145296</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Washington</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>47.4009</td>
      <td>-121.4905</td>
      <td>87522</td>
      <td>2126</td>
      <td>NaN</td>
      <td>85396.0</td>
      <td>53.0</td>
      <td>1149.352985</td>
      <td>1854399.0</td>
      <td>NaN</td>
      <td>2.429104</td>
      <td>84000053.0</td>
      <td>USA</td>
      <td>24352.266013</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>55</th>
      <td>West Virginia</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>38.4912</td>
      <td>-80.9545</td>
      <td>15850</td>
      <td>355</td>
      <td>11507.0</td>
      <td>3988.0</td>
      <td>54.0</td>
      <td>884.414058</td>
      <td>561568.0</td>
      <td>NaN</td>
      <td>2.239748</td>
      <td>84000054.0</td>
      <td>USA</td>
      <td>31334.929557</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Wisconsin</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>44.2685</td>
      <td>-89.6165</td>
      <td>122274</td>
      <td>1327</td>
      <td>99925.0</td>
      <td>21022.0</td>
      <td>55.0</td>
      <td>2100.049567</td>
      <td>1552370.0</td>
      <td>NaN</td>
      <td>1.085268</td>
      <td>84000055.0</td>
      <td>USA</td>
      <td>26661.873711</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Wyoming</td>
      <td>US</td>
      <td>2020-10-01 04:30:28</td>
      <td>42.7560</td>
      <td>-107.3025</td>
      <td>5948</td>
      <td>50</td>
      <td>4791.0</td>
      <td>1107.0</td>
      <td>56.0</td>
      <td>1027.716200</td>
      <td>101160.0</td>
      <td>NaN</td>
      <td>0.840619</td>
      <td>84000056.0</td>
      <td>USA</td>
      <td>17478.777868</td>
      <td>NaN</td>
      <td>20200930</td>
    </tr>
  </tbody>
</table>