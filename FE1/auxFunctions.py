def langText(lang):
    if lang=='spa':
        lang_text={
        #Index 
        'index_1':'Ejemplo de Frontend para utilizar el simulador ressspi',
        'index_2':'ENTRAR',

        #Form
        'Form_1':'Crear nueva simulación',
        'Form_2':'Volver',
        'Form_3':'Parámetros de simulación',
        'Form_4':'Datos de la industria',
        'Form_62':'nombre',
        'Form_5':'nombre del responsable',
        'Form_6':'Pais',
        'Form_7':'Tamaño',
        'Form_8':'Grande',
        'Form_88':'Mediana',
        'Form_89':'Pequeña',
        'Form_9':'Micro',
        'Form_10':'Sector',
        'Form_11':'Alimentacion & Bebida',
        'Form_12':'Ganaderia & Agricultura',
        'Form_13':'Papel',
        'Form_14':'Químico',
        'Form_15':'Textil',
        'Form_16':'Minería',
        'Form_17':'Madera & Corcho',
        'Form_18':'Lavanderías',
        'Form_19':'Tratamiento aguas',
        'Form_20':'Datos financieros',
        'Form_21':'Tipo de combustible usuado actualmente',
        'Form_22':'Combustible actual',
        'Form_23':'Gas Natural',
        'Form_24':'GN licuado',
        'Form_25':'Electricidad',
        'Form_26':'Propano',
        'Form_27':'Butano',
        'Form_28':'Biomasa',
        'Form_29':'Aire propanado',
        'Form_30':'Gasóleo-B',
        'Form_31':'Gasóleo-C',
        'Form_32':'Precio',
        'Form_33':'Unidades',
        'Form_34':'Precio de tonelada de CO2',
        'Form_35':'Tipo de modelo de negocio',
        'Form_36':'Llave en mano',
        'Form_37':'Próximamente los modelos: ESCO & Renting',
        'Form_38':'Localización del sistema solar',
        'Form_39':'No encuentras la ubicación?',
        'Form_40':'Espacio en m2',
        'Form_41':'Tipo de superficie',
        'Form_42':'Terreno limpio',
        'Form_43':'Terreno con obstáculos',
        'Form_44':'Cubierta de hormigón',
        'Form_45':'Cubierta panel sandwich',
        'Form_46':'Otro tipo de cubierta',
        'Form_47':'Distancia al punto de suministro en m',
        'Form_48':'Características de la superficie',
        'Form_49':'Norte-Sur',
        'Form_50':'Próximamente: Este-Oeste',
        'Form_51':'Plano',
        'Form_52':'Próximamente: Inclinación suave y pronunciada',
        'Form_53':'Libre de sombras',
        'Form_54':'Próximamente: Sombreado mañana y tarde',
        'Form_55':'Datos de proceso',
        'Form_56':'Características del fluido',
        'Form_57':'Fluido',
        'Form_58':'Agua sobrecalentada',
        'Form_59':'Vapor',
        'Form_60':'Aceite térmico',
        'Form_61':'Presión',
        'Form_63':'Unidades',
        'Form_64':'Características del proceso',
        'Form_65':'Tipo de conexión',
        'Form_66':'A proceso directo',
        'Form_67':'Con depósito intermedio',
        'Form_68':'Principales procesos térmicos',
        'Form_69':'Tipo de proceso',
        'Form_70':'Datos de la demanda',
        'Form_71':'Consumo <b> anual </b> de energía térmica',
        'Form_72':'Demanda anual',
        'Form_73':'Unidades',
        'Form_74':'Jornada laboral',
        'Form_75':'Hora inicio',
        'Form_76':'Hora final',
        'Form_77':'Marque la casilla cuando exista demanda de energía térmica en el día o mes indicado ',
        'Form_78':'Demanda semanal (marque el día cuando exista consumo)',
        'Form_79':'Lun',
        'Form_80':'Mar',
        'Form_81':'Mier',
        'Form_82':'Jue',
        'Form_83':'Vier',
        'Form_84':'Sab',
        'Form_85':'Dom',
        'Form_86':'Demanda anual (marque el mes cuando exista consumo)',
        'Form_87':'ENVIAR',
        'Form_90':'Temperatura entrada ºC',
        'Form_91':'Temperatura salida ºC',
        'Form_92':'Temp. entrada caldera',
        'Form_93':'Temp. salida caldera',
        'Form_94':'Editar simulación',
        'Form_95':'Código del pais seleccionado',
        'Form_96':'Demanda semanal (Porcentaje semanal de demanda térmica. La suma de los 7 días debe ser igual a 1)',
        'Form_97':'Demanda mensual (Porcentaje mensual de demanda térmica. La suma de los 12 meses debe ser igual a 1)',
        'Form_98':'Ubicación',
        'Form_99':'Información sobre la ubicación',
        'Form_100':'€/litro',
        'Form_101':'Editar',
        'Form_102':'Desconocido',
        'Form_102':'Dummy',
       
        #Manual
        'Manual_1':'Simulación manual',
        'Manual_2':'Volver',
        'Manual_3':'Modificadores externos',
        'Manual_4':'Modificador inversión:',
        'Manual_5':'Modificador radiación:',
        'Manual_6':'Modif. producción:',
        'Manual_7':'Parámetros de diseño',
        'Manual_8':'Número loops:',
        'Manual_9':'Número colectores por loop:',
        'Manual_10':'Tamaño almacenamiento térmico:',
        'Manual_11':'Esquema de integración:',
        'Manual_12':'Elegir esquema',



        #Details
        'det_EUR_YEAR':'€/año',
        'det_1':'Resumen de resultados:',
        'det_2':'Ahorro solar año 1: ',
        'det_3':'Factura actual: ',
        'det_4':'Inversión:',
        'det_5':'Campo solar:',
        'det_6':'Ahorro solar medio:',
        'det_7':'Coste combustible actual',
        'det_8':'TIR:',
        'det_9':'Producción energía:',
        'det_10':'% Ahorro solar:',
        'det_11':'Retorno: ',
        'det_12':'CO2 evitado: ',
        'det_19':'año',


        
        }
    if lang=='eng':
        lang_text={
        #Index 
        'index_1':'Frontend example for using ressspi simulator',
        'index_2':'ENTER',
       
        #Form
        'Form_1':'Create new simulation',
        'Form_2':'Go back',
        'Form_3':'Simulation parameters',
        'Form_4':'Contact data',
        'Form_62':'Name',
        'Form_5':'Name of decision maker',
        'Form_6':'Country',
        'Form_7':'Size',
        'Form_8':'Big',
        'Form_88':'Medium',
        'Form_89':'Small',
        'Form_9':'Micro',
        'Form_10':'Sector',
        'Form_11':'Food & Bev',
        'Form_12':'Agro',
        'Form_13':'Paper',
        'Form_14':'Chemical',
        'Form_15':'Textile',
        'Form_16':'Minning',
        'Form_17':'Wood & Corck',
        'Form_18':'Laundry',
        'Form_19':'Sewage drying',
        'Form_20':'Financial data',
        'Form_21':'Type of fuel used now',
        'Form_22':'Fossil fuel',
        'Form_23':'Natural Gas',
        'Form_24':'LNG',
        'Form_25':'Electricity',
        'Form_26':'Propane',
        'Form_27':'Butane',
        'Form_28':'Biomass',
        'Form_29':'Propane air',
        'Form_30':'Gasoil-B',
        'Form_31':'Gasoil-C',
        'Form_32':'Price',
        'Form_33':'Units',
        'Form_34':'Price of Co2 ton',
        'Form_35':'Type of business model',
        'Form_36':'Turnkey',
        'Form_37':'Coming soon: ESCO & Renting',
        'Form_38':'Location of the solar system',
        'Form_39':'You do not find your location?',
        'Form_40':'Surface m2',
        'Form_41':'Type of surface',
        'Form_42':'Clean terrain',
        'Form_43':'Rough terrain',
        'Form_44':'Concrete rooftop',
        'Form_45':'Sandwich rooftop',
        'Form_46':'Other type of rooftop',
        'Form_47':'Distance to boiler room m',
        'Form_48':'Characteristics of the surface',
        'Form_49':'North-South',
        'Form_50':'Coming soon: East-West',
        'Form_51':'Flat',
        'Form_52':'Coming soon: soft tilt',
        'Form_53':'Free of shadows',
        'Form_54':'Comming soon: morning & afternoon shadowing',
        'Form_55':'Process data',
        'Form_56':'Fluid characteristics',
        'Form_57':'Fluid',
        'Form_58':'Pressurized water',
        'Form_59':'Steam',
        'Form_60':'Thermal oil',
        'Form_61':'Pressure',
        'Form_63':'Units',
        'Form_64':'Process characteristics',
        'Form_65':'Type of process',
        'Form_66':'Direct process',
        'Form_67':'Intermedate storage',
        'Form_68':'Main thermal process',
        'Form_69':'Type of process',
        'Form_70':'Demand data',
        'Form_71':'Thermal energy <b> annual </b> demand',
        'Form_72':'Annual demand',
        'Form_73':'Units',
        'Form_74':'Daily working days',
        'Form_75':'Starting hour',
        'Form_76':'Ending hour',
        'Form_77':'Check the box when there is a demand for thermal energy on the indicated day or month',
        'Form_78':'Weekly demand (check the day of the week when consumption exists)',
        'Form_79':'Mon',
        'Form_80':'Tues',
        'Form_81':'Wedn',
        'Form_82':'Thur',
        'Form_83':'Fri',
        'Form_84':'Sat',
        'Form_85':'Sun',
        'Form_86':'Annual demand (check the month when consumption exists)',
        'Form_87':'SEND',
        'Form_90':'Inlet temperature ºC',
        'Form_91':'Outlet temperature ºC',
        'Form_92':'Inlet temp. of the boiler',
        'Form_93':'Outlet temp. of the boiler',
        'Form_94':'Edit simulation',
        'Form_95':'Country code',
        'Form_96':'Weekly demand (Weekly percentage of thermal demand. The sum of the 7 days must be 1)',
        'Form_97':'Monthly demand (Monthly percentage of thermal demand. The sum of the 12 months must be 1)',
        'Form_98':'Place',
        'Form_99':'Information regarding the location',
        'Form_100':'€/liter',
        'Form_101':'Edit',
        'Form_102':'Unknown',
        'Form_102':'Dummy',
       
        
        #Manual
        'Manual_1':'Manual simulation',
        'Manual_2':'Go back',
        'Manual_3':'External modifiers',
        'Manual_4':'Investment modifier:',
        'Manual_5':'Radiation modifier:',
        'Manual_6':'Production modifier:',
        'Manual_7':'Design parameters',
        'Manual_8':'Number of loops:',
        'Manual_9':'Number of collectors per loop:',
        'Manual_10':'Size of thermal storage:',
        'Manual_11':'Integration concept:',
        'Manual_12':'Choose integration',
        

        #Details
        'det_EUR_YEAR':'€/year',
        'det_1':'Simulation results:',
        'det_2':'Solar savings year 1: ',
        'det_3':'Current energy bill: ',
        'det_4':'Investment:',
        'det_5':'Solar field:',
        'det_6':'Avg. solar savings:',
        'det_7':'Current price of fuel',
        'det_8':'IRR:',
        'det_9':'Energy production:',
        'det_10':'% Solar savings:',
        'det_11':'Payback: ',
        'det_12':'CO2 avoided: ',
        'det_19':'year',
        

        }

    return lang_text


def fuelCalculator(fuel,fuelUnit,originalFuelPrice,co2TonPrice):
    priceFactor=1
    co2factor=1

    
    #STEP 1 -> We standarize the units to €/kWh
    #http://conecta-energia.es/wp-content/uploads/2014/07/Conversor-energ%C3%ADa.pdf
    if fuel in ["NG","LNG"]:
        cp=9.02 #https://www.engineeringtoolbox.com/fossil-fuels-energy-content-d_1298.html
        co2factor=.2/1000 #TonCo2/kWh  #https://www.engineeringtoolbox.com/co2-emission-fuels-d_1085.html
        if fuelUnit=="eur_m3":
            priceFactor=1/cp 
        if fuelUnit=="eur_litre":
            priceFactor=1/(cp) 
        if fuelUnit=='eur_kg':
            priceFactor=1
    
    
    if fuel in ['Fueloil1','Fueloil2','Fueloil3','Gasoil-B','Gasoil-C']:
        cp=10.18 #https://www.engineeringtoolbox.com/fossil-fuels-energy-content-d_1298.html
        co2factor=.27/1000 #TonCo2/kWh       #https://www.engineeringtoolbox.com/co2-emission-fuels-d_1085.html    
        if fuelUnit=="eur_m3":
            priceFactor=1/cp 
        if fuelUnit=="eur_litre":
            priceFactor=1/(cp) 
        if fuelUnit=='eur_kg':
            priceFactor=1
    
    
    if fuel in ['Electricity']:
        co2factor=.385/1000 #TonCo2/kWh  #https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
        if fuelUnit!='eur_kWh':
            priceFactor=1
    
    if fuel in ['Propane','Butane','Air-propane']:
        cp=14 #https://www.engineeringtoolbox.com/fossil-fuels-energy-content-d_1298.html
        co2factor=.22/1000 #TonCo2/kWh    #https://www.engineeringtoolbox.com/co2-emission-fuels-d_1085.html  
        if fuelUnit=="eur_m3":
            priceFactor=1/cp 
        if fuelUnit=="eur_litre":
            priceFactor=1/(cp) 
        if fuelUnit=='eur_kg':
            priceFactor=1
    
    
    if fuel in ['Biomass']:
        cp=5.81 #kWh/kg #http://petromercado.com/blog/37-articulos/182-poder-calorifico-en-kw-del-gasoleo-c-butano-y-pellet.html
        co2factor=.41/1000 #TonCo2/kWh  #https://www.engineeringtoolbox.com/co2-emission-fuels-d_1085.html
        if fuelUnit=='eur_kg':
            priceFactor=1/cp 
        else:
            priceFactor=1
    
    Fuel_price=originalFuelPrice*priceFactor   #Price of fossil fuel in €/kWh
    return [Fuel_price,co2factor]


    
