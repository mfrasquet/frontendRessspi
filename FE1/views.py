from django.shortcuts import render
from .auxFunctions import *
from .forms import EntryForm

from datetime import datetime
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/ressspi_offline/')
from Ressspi import ressspiSIM
from Plot_modules.plottingRessspi import *
# Create your views here.



def index(request):
    return  render(request, 'FE1/index.html',{})

def simulator(request,lang):
    lang_text=langText(lang)

    if request.method =='POST':
        form=EntryForm(request.POST)

        if form.is_valid():
            fuel=form.cleaned_data['fuel']
            fuelPrice=form.cleaned_data['fuelPrice']
            co2TonPrice=form.cleaned_data['co2TonPrice']
            
            fuelUnit=form.cleaned_data['fuelUnit']
            businessModel=form.cleaned_data['businessModel']
            location=form.cleaned_data['location']
            surface=form.cleaned_data['surface']
            terrain=form.cleaned_data['terrain']
            distance=form.cleaned_data['distance']
            orientation=form.cleaned_data['orientation']
            inclination=form.cleaned_data['inclination']
            shadows=form.cleaned_data['shadows']
            fluid=form.cleaned_data['fluid']
            pressure=form.cleaned_data['pressure']
            pressureUnit=form.cleaned_data['pressureUnit']
            tempIN=form.cleaned_data['tempIN']
            tempOUT=form.cleaned_data['tempOUT']
            connection=form.cleaned_data['connection']
            process=form.cleaned_data['process']
            demand=form.cleaned_data['demand']
            demandUnit=form.cleaned_data['demandUnit']
            hourINI=int(form.cleaned_data['hourINI'])
            hourEND=int(form.cleaned_data['hourEND'])
            
            Mond=form.cleaned_data['Mond']
            Tues=form.cleaned_data['Tues']
            Wend=form.cleaned_data['Wend']
            Thur=form.cleaned_data['Thur']
            Fri=form.cleaned_data['Fri']
            Sat=form.cleaned_data['Sat']
            Sun=form.cleaned_data['Sun']

            Mond_value,Tues_value,Wend_value,Thur_value,Fri_value,Sat_value,Sun_value=0,0,0,0,0,0,0
            week=[Mond,Tues,Wend,Thur,Fri,Sat,Sun]
            porctDay=1/week.count('on')
            if Mond=='on':
                Mond_value=round(porctDay,3)
            if Tues=='on':
                Tues_value=round(porctDay,3)
            else:
                Tues_value=0
            if Wend=='on':
                Wend_value=round(porctDay,3)
            if Thur=='on':
                Thur_value=round(porctDay,3)
            if Fri=='on':
                Fri_value=round(porctDay,3)
            if Sat=='on':
                Sat_value=round(porctDay,3)
            if Sun=='on':
                Sun_value=round(porctDay,3)

            Jan=form.cleaned_data['Jan']
            Feb=form.cleaned_data['Feb']
            Mar=form.cleaned_data['Mar']
            Apr=form.cleaned_data['Apr']
            May=form.cleaned_data['May']
            Jun=form.cleaned_data['Jun']
            Jul=form.cleaned_data['Jul']
            Aug=form.cleaned_data['Aug']
            Sep=form.cleaned_data['Sep']
            Oct=form.cleaned_data['Oct']
            Nov=form.cleaned_data['Nov']
            Dec=form.cleaned_data['Dec']

            Jan_value,Feb_value,Mar_value,Apr_value,May_value,Jun_value,Jul_value,Aug_value,Sep_value,Oct_value,Nov_value,Dec_value=0,0,0,0,0,0,0,0,0,0,0,0
            year=[Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
            porctMonth=1/year.count('on')
            if Jan=='on':
                Jan_value=round(porctMonth,3)
            if Feb=='on':
                Feb_value=round(porctMonth,3)
            if Mar=='on':
                Mar_value=round(porctMonth,3)
            if Apr=='on':
                Apr_value=round(porctMonth,3)
            if May=='on':
                May_value=round(porctMonth,3)
            if Jun=='on':
                Jun_value=round(porctMonth,3)
            if Jul=='on':
                Jul_value=round(porctMonth,3)
            if Aug=='on':
                Aug_value=round(porctMonth,3)
            if Sep=='on':
                Sep_value=round(porctMonth,3)
            if Oct=='on':
                Oct_value=round(porctMonth,3)
            if Nov=='on':
                Nov_value=round(porctMonth,3)
            if Dec=='on':
                Dec_value=round(porctMonth,3)

           

            num_loops=form.cleaned_data['num_loops']
            n_coll_loop=form.cleaned_data['n_coll_loop']
            type_integration=form.cleaned_data['type_integration']
            almVolumen=form.cleaned_data['almVolumen']

            [Fuel_price,co2factor]=fuelCalculator(fuel,fuelUnit,fuelPrice,co2TonPrice)
            
            
            #Put everything in a dict for ressspi
            inputsDjango={'date':datetime.now().strftime('%Y-%m-%d'),'name':'frontEndExample', 
            'email':'na','industry':'na','sectorIndustry':'na','fuel':fuel,
            'fuelPrice':Fuel_price,'co2TonPrice':co2TonPrice,'co2factor':co2factor,'fuelUnit':'eur_kWh','co2factor':co2factor,'businessModel':businessModel,
            'location':location,'location_aux':'na','surface':surface,'terrain':terrain,
            'distance':distance,'orientation':orientation,'inclination':inclination,'shadows':shadows,
            'fluid':fluid,'pressure':pressure,'pressureUnit':pressureUnit,'tempIN':tempIN,
            'tempOUT':tempOUT,'connection':connection,'process':process,'demand':demand,
            'demandUnit':demandUnit,'hourINI':hourINI,'hourEND':hourEND,'Mond':Mond_value,'Tues':Tues_value,
            'Wend':Wend_value,'Thur':Thur_value,'Fri':Fri_value,'Sat':Sat_value,'Sun':Sun_value,'Jan':Jan_value,'Feb':Feb_value,'Mar':Mar_value,
            'Apr':Apr_value,'May':May_value,'Jun':Jun_value,'Jul':Jul_value,'Aug':Aug_value,'Sep':Sep_value,'Oct':Oct_value,'Nov':Nov_value,
            'Dec':Dec_value,'last_reg':'666'}


            confReport={'lang':lang,'sender':'frontEndExample','cabecera':'na','mapama':0}
            modificators={'mofINV':1,'mofDNI':1,'mofProd':1}
            desginDict={'num_loops':num_loops,'n_coll_loop':n_coll_loop,'type_integration':type_integration,'almVolumen':almVolumen}
            simControl={'finance_study':1,'mes_ini_sim':1,'dia_ini_sim':1,'hora_ini_sim':1,'mes_fin_sim':12,'dia_fin_sim':31,'hora_fin_sim':24}    
               

            [template_vars,plotVars,reportsVar,version]=ressspiSIM(1,inputsDjango,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],200,confReport,modificators,desginDict,simControl,'666')

            Q_prod=plotVars['Q_prod']
            Q_prod_lim=plotVars['Q_prod_lim']
            DNI=plotVars['DNI']
            Demand=plotVars['Demand']

            n_years_sim=plotVars['n_years_sim']
            Acum_FCF=plotVars['Acum_FCF']
            FCF=plotVars['FCF']
            m_dot_min_kgs=plotVars['m_dot_min_kgs']
            steps_sim=plotVars['steps_sim']
            AmortYear=plotVars['AmortYear']
            Selling_price=plotVars['Selling_price']

            Q_charg=plotVars['Q_charg']
            Q_useful=plotVars['Q_useful']
            Q_defocus=plotVars['Q_defocus']
            Q_discharg=plotVars['Q_discharg']
            T_alm_K=plotVars['T_alm_K']
            SOC=plotVars['SOC']

            type_integration=plotVars['type_integration']
            in_s=plotVars['in_s']
            out_s=plotVars['out_s']
            T_in_flag=plotVars['T_in_flag']
            T_in_C=plotVars['T_in_C']
            T_in_C_AR=plotVars['T_in_C_AR']
            T_out_C=plotVars['T_out_C']
            outProcess_s=plotVars['outProcess_s']
            T_out_process_C=plotVars['T_out_process_C']
            P_op_bar=plotVars['P_op_bar']
            x_design=plotVars['x_design']
            T_out_C=plotVars['T_out_C']
            h_in=plotVars['h_in']
            h_out=plotVars['h_out']
            hProcess_out=plotVars['hProcess_out']
            outProcess_h=plotVars['outProcess_h']

            Production_max=plotVars['Production_max']
            Production_lim=plotVars['Production_lim']
            Perd_term_anual=plotVars['Perd_term_anual']
            DNI_anual_irradiation=plotVars['DNI_anual_irradiation']
            Area=plotVars['Area']
            num_loops=plotVars['num_loops']


            if fluid!="oil": #WATER OR STEAM
                #Mollier Plot for s-t for Water
                    image_prop1=mollierPlotST('django',-2,lang,type_integration,in_s,out_s,T_in_flag,T_in_C,T_in_C_AR,T_out_C,outProcess_s,T_out_process_C,P_op_bar,x_design,'na',200)              
                #Mollier Plot for s-h for Water 
                    image_prop2=mollierPlotSH('django',-2,lang,type_integration,h_in,h_out,hProcess_out,outProcess_h,in_s,out_s,T_in_flag,T_in_C,T_in_C_AR,T_out_C,outProcess_s,T_out_process_C,P_op_bar,x_design,'na',200)  
            if fluid=="oil": 
                    image_prop1=rhoTempPlotOil('django',-2,lang,T_out_C,'na',200) #(12) Plot thermal oil properties Rho & Cp vs Temp
                    image_prop2=viscTempPlotOil('django',-2,lang,T_out_C,'na',200) #(13) Plot thermal oil properties Viscosities vs Temp        

            image_prodMonths=prodMonths('django',-2,Q_prod,Q_prod_lim,DNI,Demand,lang,'na',200)
            image_finance=financePlot('django',-2,lang,n_years_sim,Acum_FCF,FCF,m_dot_min_kgs,steps_sim,AmortYear,Selling_price,'na',200)
            image_prodMonths=prodMonths('django',-2,Q_prod,Q_prod_lim,DNI,Demand,lang,'na',200)
            image_prodWinter=prodWinterPlot('django',-2,lang,Demand,Q_prod,Q_prod_lim,type_integration,Q_charg,Q_discharg,DNI,'na',200)   
            image_prodSummer=prodSummerPlot('django',-2,lang,Demand,Q_prod,Q_prod_lim,type_integration,Q_charg,Q_discharg,DNI,'na',200)  
            image_storageWinter=storageWinter('django',-2,lang,Q_prod,Q_charg,Q_prod_lim,Q_useful,Demand,Q_defocus,Q_discharg,type_integration,T_alm_K,SOC,'na',200)    
            image_storageSummer=storageSummer('django',-2,lang,Q_prod,Q_charg,Q_prod_lim,Q_useful,Demand,Q_defocus,Q_discharg,type_integration,T_alm_K,SOC,'na',200)    

            Boiler_eff=plotVars['Boiler_eff']
            Energy_before = [x / Boiler_eff for x in Demand]
            Energy_before_annual=sum(Energy_before)
            Energy_bill = Fuel_price*sum(Demand)/Boiler_eff

            results={'sav1':int(reportsVar['Energy_savingsList'][1]),
            'solarNetFraction':round(reportsVar['solar_fraction_lim'],2),
            'Energy_bill':int(Energy_bill),
            'Fuel_price':Fuel_price,
            'Investment':int(reportsVar['Selling_price']),
            'IRR':round(reportsVar['IRR'],2),
            'Amort':int(reportsVar['AmortYear']),
            'Area_total':int(reportsVar['Area_total']),
            'Production_lim':int(reportsVar['Production_lim']),
            'tonCo2Saved':int(reportsVar['tonCo2Saved'])}

            return  render(request, 'FE1/results.html',{'lang_text':lang_text,'image_prodMonths':image_prodMonths,'image_finance':image_finance,
            'image_prodWinter':image_prodWinter,'image_prodSummer':image_prodSummer,
            'image_storageWinter':image_storageWinter,'image_storageSummer':image_storageSummer,
            'image_prop1':image_prop1,'image_prop2':image_prop2,
            'version':version,'results':results})

          
        else:
            form=EntryForm(request.POST)
    else:
        form=EntryForm()
    
    return  render(request, 'FE1/simulator.html',{'lang_text':lang_text,'form':form})