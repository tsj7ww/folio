# clone JHU COVID19 data repo
# git clone https://github.com/CSSEGISandData/COVID-19.git
# folder prep
# rm -rf $INPUT
# mkdir $INPUT
# mkdir $INPUT/csse-dly
# mkdir $INPUT/csse-dly-us
# mkdir $INPUT/csse-ts
# mkdir $INPUT/who-ts
# vars
COVID=/home/tsj7ww/Github/JHU_COVID19
DATA=/home/tsj7ww/Github/folio/analysis/covid19/in/covid/jhu
# update repo
(cd $COVID && git pull)
# copy files
cp $COVID/csse_covid_19_data/csse_covid_19_daily_reports/*.csv $DATA/csse-dly
cp $COVID/csse_covid_19_data/csse_covid_19_daily_reports_us/*.csv $DATA/csse-dly-us
cp $COVID/csse_covid_19_data/csse_covid_19_time_series/*.csv $DATA/csse-ts
cp $COVID/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/*.csv $DATA/who-ts
cp $COVID/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv $DATA/csse-fips-lkup.csv # UID_ISO_FIPS_LookUp_Table