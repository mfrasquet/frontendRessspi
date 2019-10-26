from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


fuelDict=['NG','LNG','Electricity','Propane','Butane','Biomass','Air-propane','Fueloil1','Fueloil2','Fueloil3','Gasoil-B','Gasoil-C']
fuelUnitDict=['eur_kWh','eur_litre','eur_m3','eur_kg']
businessModelDict=['turnkey','ESCO','Renting']
terrainDict=['clean_ground','dirty_ground','rooftop_concrete','rooftop_sandwich','other']
orientationDict=['NS','EW']
inclinationDict=['flat','soft-tilt','extreme-tilt']
shadowsDict=['free','morning','afternoon']
fluidDict=['water','steam','oil']
pressureUnitDict=['bar','MPa','psi']
connectionDict=['process','storage']
demandUnitDict=['kWh','MWh','KJ','BTU','kcal']
hourDayDict=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
type_integrationDict=["SL_L_P","SL_L_PS","SL_L_RF","SL_S_FW","SL_S_FWS","SL_S_PD","SL_L_S","SL_L_S3","PL_E_PM"]




class EntryForm(forms.Form):
    fuel=forms.ChoiceField(choices=list(zip(fuelDict,fuelDict)))
    fuelPrice=forms.FloatField(validators=[MinValueValidator(0)])
    co2TonPrice=forms.FloatField(required=False,validators=[MinValueValidator(0)])
    fuelUnit=forms.ChoiceField(choices=list(zip(fuelUnitDict,fuelUnitDict)))
    businessModel=forms.ChoiceField(choices=list(zip(businessModelDict,businessModelDict)))
    location=forms.CharField(max_length=200)
    location_aux=forms.CharField(required=False,max_length=50)
    surface=forms.IntegerField(required=False,validators=[MinValueValidator(0)])
    terrain=forms.ChoiceField(required=False,choices=list(zip(terrainDict,terrainDict)))
    distance=forms.IntegerField(required=False,validators=[MinValueValidator(0)])
    orientation=forms.ChoiceField(required=False,choices=list(zip(orientationDict,orientationDict)))
    inclination=forms.ChoiceField(required=False,choices=list(zip(inclinationDict,inclinationDict)))
    shadows=forms.ChoiceField(required=False,choices=list(zip(shadowsDict,shadowsDict)))
    fluid=forms.ChoiceField(choices=list(zip(fluidDict,fluidDict)))
    pressure=forms.FloatField(validators=[MinValueValidator(0)])
    pressureUnit=forms.ChoiceField(choices=list(zip(pressureUnitDict,pressureUnitDict)))
    tempIN=forms.FloatField(validators=[MinValueValidator(0)])
    tempOUT=forms.FloatField(validators=[MinValueValidator(0)])
    connection=forms.ChoiceField(required=False,choices=list(zip(connectionDict,connectionDict)))
    process=forms.CharField(required=False,max_length=150)
    
    demand=forms.FloatField(validators=[MinValueValidator(0)])
    demandUnit=forms.ChoiceField(choices=list(zip(demandUnitDict,demandUnitDict)))
    hourINI=forms.ChoiceField(choices=list(zip(hourDayDict,hourDayDict)))
    hourEND=forms.ChoiceField(choices=list(zip(hourDayDict,hourDayDict)))
    
    Mond=forms.CharField(required=False,max_length=10)
    Tues=forms.CharField(required=False,max_length=10)
    Wend=forms.CharField(required=False,max_length=10)
    Thur=forms.CharField(required=False,max_length=10)
    Fri=forms.CharField(required=False,max_length=10)
    Sat=forms.CharField(required=False,max_length=10)
    Sun=forms.CharField(required=False,max_length=10)

    Jan=forms.CharField(required=False,max_length=10)
    Feb=forms.CharField(required=False,max_length=10)
    Mar=forms.CharField(required=False,max_length=10)
    Apr=forms.CharField(required=False,max_length=10)
    May=forms.CharField(required=False,max_length=10)
    Jun=forms.CharField(required=False,max_length=10)
    Jul=forms.CharField(required=False,max_length=10)
    Aug=forms.CharField(required=False,max_length=10)
    Sep=forms.CharField(required=False,max_length=10)
    Oct=forms.CharField(required=False,max_length=10)
    Nov=forms.CharField(required=False,max_length=10)
    Dec=forms.CharField(required=False,max_length=10)

    Mond_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Tues_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Wend_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Thur_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Fri_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Sat_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Sun_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])

    Jan_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Feb_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Mar_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Apr_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    May_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Jun_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Jul_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Aug_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Sep_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Oct_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Nov_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Dec_value=forms.FloatField(required=False,validators=[MinValueValidator(0),MaxValueValidator(1)])

    mofINV=forms.FloatField(required=False,validators=[MinValueValidator(0)])
    mofDNI=forms.FloatField(required=False,validators=[MinValueValidator(0)])
    mofProd=forms.FloatField(required=False,validators=[MinValueValidator(0)])

    num_loops=forms.IntegerField(required=False,validators=[MinValueValidator(0)])
    n_coll_loop=forms.IntegerField(required=False,validators=[MinValueValidator(0)])
    type_integration=forms.ChoiceField(required=False,choices=list(zip(type_integrationDict,type_integrationDict)))
    almVolumen=forms.FloatField(required=False,validators=[MinValueValidator(0)])
    
  