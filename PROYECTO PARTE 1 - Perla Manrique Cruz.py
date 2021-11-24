#!/usr/bin/env python
# coding: utf-8

# ### PROYECTO: AGRICULTURA Y SEGURIDAD ALIMENTARIA EN EL PERÚ

# * Este proyecto tiene como objetivo analizar los principales indicadores de la agricultura y la seguridad alimentaria en el Perú; así como la relación y el impacto de la agricultura en la seguridad alimentaria.Todo ello a fin de generar evidencia que apoye al Ministerio de Desarrollo Agrario y Riego, a tomar mejores decisiones en la formulación de Políticas públicas orientadas al desarrollo sostenible del sector agrícola y a garantizar la seguridad alimentaria en el Perú.

# * Preguntas de investigación:
#      - ¿Qué reflejan las estadísticas descriptivas de los datos sobre la agricultura en el Perú?
#      - ¿Qué reflejan las estadísticas descriptivas de los datos sobre la seguridad alimentaria en el Perú?
#      - ¿De qué manera se relaciona la agricultura con la seguridad alimentaria en el Perú?
#      - ¿Cuál es el impacto de la agricultura en la seguridad alimentaria del Perú durante los años 2001-2019?

# In[ ]:


# EXTRACCIÓN DE DATOS USANDO API - BANCO MUNDIAL


# In[1]:


pip install wbgapi


# In[2]:


import wbgapi as wb


# In[3]:


wb.source.info()


# ### BASE DE DATOS DE LA AGRICULTURA

# * Según la Organización de las Naciones Unidas para la Alimentación y la Agricultura - FAO(2011), la agricultura es una actividad que se ocupa de la producción del cultivo del suelo, el desarrollo y recogida de las cosechas, así como también de la explotación de bosques y selvas (silvicultura), la cría y desarrollo de ganado. Es por ello que para este proyecto se ha considerado los principales indicadores de la agricultura extraídos a través del API del Banco Mundial, tales como: Tierras agrícolas (% del área de tierra), Tierras cultivables(% del área de tierra), Agricultura, valor agregado (% del PIB), Empleos en agricultura (% del total de empleos), Índice de producción de alimentos (2004-2006 = 100), Índice de producción animal (2004-2006 = 100), Importaciones de alimentos (% de importaciones de mercaderías), Exportaciones de alimentos (% de exportaciones de mercaderías).

# In[4]:


# PIB per cápita (US$ a precios actuales)
PBI=wb.data.DataFrame('NY.GDP.PCAP.CD', ['PER'], time = range(1990,2020), labels = True)
PBI


# In[5]:


PBI.drop(['Country'], axis=1, inplace=True)
PBI


# In[6]:


PBI.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
PBI


# In[7]:


data0=PBI.transpose()
data0.head()


# In[8]:


data0.rename(columns={'PER':'PBI'}, inplace=True)
data0.head()


# In[9]:


data0['index'] = data0.index
data0.head()


# In[10]:


data0.rename(columns={'index':'Año'}, inplace=True)
data0.head()


# In[11]:


# Tierras agrícolas (% del área de tierra)
tierrasagricolas=wb.data.DataFrame('AG.LND.AGRI.ZS', ['PER'], time = range(1990,2020), labels = True)
tierrasagricolas


# In[12]:


tierrasagricolas.drop(['Country'], axis=1, inplace=True)
tierrasagricolas


# In[13]:


tierrasagricolas.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
tierrasagricolas


# In[14]:


data1=tierrasagricolas.transpose()
data1.head()


# In[15]:


data1.rename(columns={'PER':'Tierras_agrícolas'}, inplace=True)
data1.head()


# In[16]:


data1['index'] = data1.index
data1.head()


# In[17]:


data1.rename(columns={'index':'Año'}, inplace=True)
data1.head()


# In[18]:


# Tierras cultivables(% del área de tierra)
tierrascultivables=wb.data.DataFrame('AG.LND.ARBL.ZS', ['PER'], time = range(1990,2020), labels = True)
tierrascultivables


# In[19]:


tierrascultivables.drop(['Country'], axis=1, inplace=True)
tierrascultivables


# In[20]:


tierrascultivables.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
tierrascultivables


# In[21]:


data2=tierrascultivables.transpose()
data2.head()


# In[22]:


data2.rename(columns={'PER':'Tierras_cultivables'}, inplace=True)
data2.head()


# In[23]:


data2['index'] = data2.index
data2.head()


# In[24]:


data2.rename(columns={'index':'Año'}, inplace=True)
data2.head()


# In[25]:


# Agricultura, valor agregado (% del PIB)
pbiagricultura=wb.data.DataFrame('NV.AGR.TOTL.ZS', ['PER'], time = range(1990,2020), labels = True)
pbiagricultura


# In[26]:


pbiagricultura.drop(['Country'], axis=1, inplace=True)
pbiagricultura


# In[27]:


pbiagricultura.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
pbiagricultura


# In[28]:


data3=pbiagricultura.transpose()
data3.head()


# In[29]:


data3.rename(columns={'PER':'PBI_agricultura'}, inplace=True)
data3.head()


# In[30]:


data3['index'] = data3.index
data3.head()


# In[31]:


data3.rename(columns={'index':'Año'}, inplace=True)
data3.head()


# In[32]:


# Empleos en agricultura (% del total de empleos)
empleototal=wb.data.DataFrame('SL.AGR.EMPL.ZS', ['PER'], time = range(1990,2020), labels = True)
empleototal


# In[33]:


empleototal.drop(['Country'], axis=1, inplace=True)
empleototal


# In[34]:


empleototal.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
empleototal


# In[35]:


data4=empleototal.transpose()
data4.head()


# In[36]:


data4.rename(columns={'PER':'Empleo_total'}, inplace=True)
data4.head()


# In[37]:


data4['index'] = data4.index
data4.head()


# In[38]:


data4.rename(columns={'index':'Año'}, inplace=True)
data4.head()


# In[39]:


# Empleados en agricultura, mujeres (% del empleo femenino)
empleomujeres=wb.data.DataFrame('SL.AGR.EMPL.FE.ZS', ['PER'], time = range(1990,2020), labels = True)
empleomujeres


# In[40]:


empleomujeres.drop(['Country'], axis=1, inplace=True)
empleomujeres


# In[41]:


empleomujeres.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
empleomujeres


# In[42]:


data5=empleomujeres.transpose()
data5.head()


# In[43]:


data5.rename(columns={'PER':'Empleo_mujeres'}, inplace=True)
data5.head()


# In[44]:


data5['index'] = data5.index
data5.head()


# In[45]:


data5.rename(columns={'index':'Año'}, inplace=True)
data5.head()


# In[46]:


# Empleados en agricultura, hombres (% del empleo masculino)
empleohombres=wb.data.DataFrame('SL.AGR.EMPL.MA.ZS', ['PER'], time = range(1990,2020), labels = True)
empleohombres


# In[47]:


empleohombres.drop(['Country'], axis=1, inplace=True)
empleohombres


# In[48]:


empleohombres.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
empleohombres


# In[49]:


data6=empleohombres.transpose()
data6.head()


# In[50]:


data6.rename(columns={'PER':'Empleo_hombres'}, inplace=True)
data6.head()


# In[51]:


data6['index'] = data6.index
data6.head()


# In[52]:


data6.rename(columns={'index':'Año'}, inplace=True)
data6.head()


# In[53]:


# Índice de producción de alimentos (2004-2006 = 100)
indicealimentos=wb.data.DataFrame('AG.PRD.FOOD.XD', ['PER'], time = range(1990,2020), labels = True)
indicealimentos


# In[54]:


indicealimentos.drop(['Country'], axis=1, inplace=True)
indicealimentos


# In[55]:


indicealimentos.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
indicealimentos


# In[56]:


data7=indicealimentos.transpose()
data7.head()


# In[57]:


data7.rename(columns={'PER':'Indice_alimentos'}, inplace=True)
data7.head()


# In[58]:


data7['index'] = data7.index
data7.head()


# In[59]:


data7.rename(columns={'index':'Año'}, inplace=True)
data7.head()


# In[61]:


indiceanimal.drop(['Country'], axis=1, inplace=True)
indiceanimal


# In[62]:


# Índice de producción animal (2004-2006 = 100)
indiceanimal=wb.data.DataFrame('AG.PRD.LVSK.XD', ['PER'], time = range(1990,2020), labels = True)
indiceanimal


# In[63]:


indiceanimal.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
indiceanimal


# In[64]:


data8=indiceanimal.transpose()
data8.head()


# In[65]:


data8.rename(columns={'PER':'Indice_produccion_animal'}, inplace=True)
data8.head()


# In[66]:


data8['index'] = data8.index
data8.head()


# In[67]:


data8.rename(columns={'index':'Año'}, inplace=True)
data8.head()


# In[ ]:





# In[68]:


# Índice de cosecha (2004-2006 = 100)
indicecosecha=wb.data.DataFrame('AG.PRD.CROP.XD', ['PER'], time = range(1990,2020), labels = True)
indicecosecha


# In[69]:


indicecosecha.drop(['Country'], axis=1, inplace=True)
indicecosecha


# In[70]:


indicecosecha.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
indicecosecha


# In[71]:


data9=indicecosecha.transpose()
data9.head()


# In[72]:


data9.rename(columns={'PER':'Indice_cosecha'}, inplace=True)
data9.head()


# In[73]:


data9['index'] = data9.index
data9.head()


# In[74]:


data9.rename(columns={'index':'Año'}, inplace=True)
data9.head()


# In[75]:


# Producción de cereales (toneladas métricas)
produccioncereales=wb.data.DataFrame('AG.PRD.CREL.MT', ['PER'], time = range(1990,2020), labels = True)
produccioncereales


# In[76]:


produccioncereales.drop(['Country'], axis=1, inplace=True)
produccioncereales


# In[77]:


produccioncereales.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
produccioncereales


# In[78]:


data10=produccioncereales.transpose()
data10.head()


# In[79]:


data10.rename(columns={'PER':'Produccion_cereales'}, inplace=True)
data10.head()


# In[80]:


data10['index'] = data10.index
data10.head()


# In[81]:


data10.rename(columns={'index':'Año'}, inplace=True)
data10.head()


# In[82]:


# Exportaciones de alimentos (% de exportaciones de mercaderías)
exportaciones=wb.data.DataFrame('TX.VAL.FOOD.ZS.UN', ['PER'], time = range(1990,2020), labels = True)
exportaciones


# In[83]:


exportaciones.drop(['Country'], axis=1, inplace=True)
exportaciones


# In[84]:


exportaciones.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
exportaciones


# In[85]:


data11=exportaciones.transpose()
data11.head()


# In[86]:


data11.rename(columns={'PER':'Exportaciones'}, inplace=True)
data11.head()


# In[87]:


data11['index'] = data11.index
data11.head()


# In[88]:


data11.rename(columns={'index':'Año'}, inplace=True)
data11.head()


# In[89]:


# Importaciones de alimentos (% de importaciones de mercaderías)
importaciones=wb.data.DataFrame('TM.VAL.FOOD.ZS.UN', ['PER'], time = range(1990,2020), labels = True)
importaciones


# In[90]:


importaciones.drop(['Country'], axis=1, inplace=True)
importaciones


# In[91]:


importaciones.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
importaciones


# In[92]:


data12=importaciones.transpose()
data12.head()


# In[93]:


data12.rename(columns={'PER':'Importaciones'}, inplace=True)
data12.head()


# In[94]:


data12['index'] = data12.index
data12.head()


# In[95]:


data12.rename(columns={'index':'Año'}, inplace=True)
data12.head()


# In[ ]:


# UNIÓN DE LOS INDICADORES DE AGRICULTURA


# In[97]:


import pandas as pd
datafinal1=pd.merge(data0,data1, how='inner', on=["Año"])
datafinal1.head()


# In[98]:


datafinal2=pd.merge(datafinal1,data2, how='inner', on=["Año"])
datafinal2.head()


# In[99]:


datafinal3=pd.merge(datafinal2,data3, how='inner', on=["Año"])
datafinal3.head()


# In[100]:


datafinal4=pd.merge(datafinal3,data4, how='inner', on=["Año"])
datafinal4.head()


# In[101]:


datafinal5=pd.merge(datafinal4,data5, how='inner', on=["Año"])
datafinal5.head()


# In[102]:


datafinal6=pd.merge(datafinal5,data6, how='inner', on=["Año"])
datafinal6.head()


# In[103]:


datafinal7=pd.merge(datafinal6,data7, how='inner', on=["Año"])
datafinal7.head()


# In[104]:


datafinal8=pd.merge(datafinal7,data8, how='inner', on=["Año"])
datafinal8.head()


# In[105]:


datafinal9=pd.merge(datafinal8,data9, how='inner', on=["Año"])
datafinal9.head()


# In[106]:


datafinal10=pd.merge(datafinal9,data10, how='inner', on=["Año"])
datafinal10.head()


# In[107]:


datafinal11=pd.merge(datafinal9,data11, how='inner', on=["Año"])
datafinal11.head()


# In[108]:


data_agricultura=pd.merge(datafinal11,data12, how='inner', on=["Año"])
data_agricultura.head()


# ### LIMPIEZA DE DATOS

# In[109]:


# Diagrama de caja y bigotes para ver si existen valores atípicos o outliers del dataset
import matplotlib.pyplot as plt
data_agricultura.boxplot(return_type="dict")
plt.show()


# In[110]:


# Para ver si hay valores atípicos o outliers en la tabla analizada se calcula los estadísticos para el boxplot de la data analizada
data_agricultura.describe()


# In[111]:


# Se reemplazan los valores nulos por la mediana
reemplazar_NA = data_agricultura.fillna(data_agricultura.median(), inplace=True)
data_agricultura.head()


# In[112]:


# Exportar los datos en formato csv 
data_agricultura.to_csv('Data_Agricultura.csv', index = True)


# ### BASE DE DATOS LA DE SEGURIDAD ALIMENTARIA

# * Según la Organización de las Naciones Unidas para la Alimentación y la Agricultura - FAO(2011), la seguridad alimentaria existe cuando todas las personas tienen, en todo momento, acceso físico, social y económico a alimentos suficientes, inocuos y nutritivos que satisfacen sus necesidades energéticas diarias y preferencias alimentarias para llevar una vida activa y sana.
# 
# * En base a ello, la definición plantea cuatro dimensiones primordiales de la seguridad alimentaria: la uitlización biológica de los alimentos, la disponibilidad física de los alimentos, el acceso económico y físico a los alimentos, y la estabilidad en el tiempo de las tres dimensiones anteriores.
# 
# * Para esta variable dependiente se han extraído los datos a través del API del Banco Mundial, clasificándolos en las dimensiones mencionadas anteriormente.

# In[ ]:


# INSEGURIDAD ALIMENTARIA


# In[270]:


# Prevalencia de inseguridad alimentaria severa en la población (%)
inseguridad_alimentaria=wb.data.DataFrame('SN.ITK.SVFI.ZS', ['PER'], time = range(2015,2020), labels = True)
inseguridad_alimentaria


# In[271]:


inseguridad_alimentaria.drop(['Country'], axis=1, inplace=True)
inseguridad_alimentaria


# In[272]:


inseguridad_alimentaria.rename(columns={'YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
inseguridad_alimentaria


# In[273]:


data1=inseguridad_alimentaria.transpose()
data1.head()


# In[274]:


data1.rename(columns={'PER':'Inseguridad_alimentaria'}, inplace=True)
data1.head()


# In[275]:


data1['index'] = data1.index
data1.head()


# In[276]:


data1.rename(columns={'index':'Año'}, inplace=True)
data1.head()


# In[ ]:


# DIMENSIÓN 1: CONDICIONES NUTRICIONALES


# In[120]:


# Prevalencia de desnutrición (% de la población)
desnutricion=wb.data.DataFrame('SN.ITK.DEFC.ZS', ['PER'], time = range(2001,2020), labels = True)
desnutricion


# In[121]:


desnutricion.drop(['Country'], axis=1, inplace=True)
desnutricion


# In[122]:


desnutricion.rename(columns={'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
desnutricion


# In[123]:


data2=desnutricion.transpose()
data2.head()


# In[124]:


data2.rename(columns={'PER':'Desnutricion'}, inplace=True)
data2.head()


# In[125]:


data2['index'] = data2.index
data2.head()


# In[126]:


data2.rename(columns={'index':'Año'}, inplace=True)
data2.head()


# In[127]:


# Prevalencia de anemia en la infancia (% de menores de 5 años)
anemia=wb.data.DataFrame('SH.ANM.CHLD.ZS', ['PER'], time = range(2000,2020), labels = True)
anemia


# In[128]:


anemia.drop(['Country'], axis=1, inplace=True)
anemia


# In[129]:


anemia.rename(columns={'YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
anemia


# In[130]:


data3=anemia.transpose()
data3.head()


# In[131]:


data3.rename(columns={'PER':'Anemia_infantil'}, inplace=True)
data3.head()


# In[132]:


data3['index'] = data3.index
data3.head()


# In[133]:


data3.rename(columns={'index':'Año'}, inplace=True)
data3.head()


# In[134]:


# Prevalencia de obesidad, varones (% de niños menores a 5)
obesidad_varones=wb.data.DataFrame('SH.STA.OWGH.MA.ZS', ['PER'], time = range(1990,2020), labels = True)
obesidad_varones


# In[135]:


obesidad_varones.drop(['Country'], axis=1, inplace=True)
obesidad_varones


# In[136]:


obesidad_varones.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
obesidad_varones


# In[137]:


data4=obesidad_varones.transpose()
data4.head()


# In[138]:


data4.rename(columns={'PER':'Obesidad_varones'}, inplace=True)
data4.head()


# In[139]:


data4['index'] = data4.index
data4.head()


# In[140]:


data4.rename(columns={'index':'Año'}, inplace=True)
data4.head()


# In[141]:


# Prevalencia de obesidad mujeres (% de niños menores a 5)
obesidad_mujeres=wb.data.DataFrame('SH.STA.OWGH.FE.ZS', ['PER'], time = range(1990,2020), labels = True)
obesidad_mujeres


# In[142]:


obesidad_mujeres.drop(['Country'], axis=1, inplace=True)
obesidad_mujeres


# In[143]:


obesidad_mujeres.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
obesidad_mujeres


# In[144]:


data5=obesidad_mujeres.transpose()
data5.head()


# In[145]:


data5.rename(columns={'PER':'Obesidad_mujeres'}, inplace=True)
data5.head()


# In[146]:


data5['index'] = data5.index
data5.head()


# In[147]:


data5.rename(columns={'index':'Año'}, inplace=True)
data5.head()


# In[ ]:


# DIMENSIÓN 2: DISPONIBILIDAD DE ALIMENTOS


# In[148]:


# Índice de cosecha (2004-2006 = 100)
cosecha=wb.data.DataFrame('AG.PRD.CROP.XD', ['PER'], time = range(1990,2020), labels = True)
cosecha


# In[149]:


cosecha.drop(['Country'], axis=1, inplace=True)
cosecha


# In[150]:


cosecha.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
cosecha


# In[151]:


data6=cosecha.transpose()
data6.head()


# In[152]:


data6.rename(columns={'PER':'Cosecha'}, inplace=True)
data6.head()


# In[153]:


data6['index'] = data6.index
data6.head()


# In[154]:


data6.rename(columns={'index':'Año'}, inplace=True)
data6.head()


# In[ ]:


# DIMENSIÓN 3: ACCESO A ALIMENTOS


# In[155]:


#  Índice de precios al consumidor (% anual)
IPC=wb.data.DataFrame('FP.CPI.TOTL.ZG', ['PER'], time = range(1990,2020), labels = True)
IPC


# In[156]:


IPC.drop(['Country'], axis=1, inplace=True)
IPC


# In[157]:


IPC.rename(columns={'YR1990':'1990', 'YR1991': '1991', 'YR1992': '1992', 'YR1993': '1993', 'YR1994': '1994', 'YR1995': '1995', 'YR1996': '1996', 'YR1997': '1997', 'YR1998': '1998', 'YR1999': '1999','YR2000':'2000', 'YR2001': '2001','YR2002': '2002','YR2003': '2003','YR2004': '2004','YR2005': '2005','YR2006': '2006','YR2007': '2007','YR2008': '2008','YR2009': '2009','YR2010': '2010','YR2011': '2011','YR2012': '2012','YR2013': '2013','YR2014': '2014','YR2015': '2015','YR2016': '2016','YR2017': '2017','YR2018': '2018','YR2019': '2019'}, inplace=True)
IPC


# In[158]:


data7=IPC.transpose()
data7.head()


# In[159]:


data7.rename(columns={'PER':'IPC'}, inplace=True)
data7.head()


# In[160]:


data7['index'] = data7.index
data7.head()


# In[161]:


data7.rename(columns={'index':'Año'}, inplace=True)
data7.head()


# ### Unión de datos

# In[162]:


import pandas as pd
datafinal1=pd.merge(data3,data2, how='inner', on=["Año"])
datafinal1.head()


# In[163]:


datafinal2=pd.merge(datafinal1,data5, how='inner', on=["Año"])
datafinal2.head()


# In[164]:


datafinal3=pd.merge(datafinal2,data6, how='inner', on=["Año"])
datafinal3.head()


# In[165]:


datafinal4=pd.merge(datafinal3,data7, how='inner', on=["Año"])
datafinal4.head()


# In[166]:


data_seguridad_alimentaria=pd.merge(datafinal4,data4, how='inner', on=["Año"])
data_seguridad_alimentaria.head()


# ### Limpieza de datos

# In[167]:


# Diagrama de caja y bigotes para ver si existen valores atípicos o outliers del dataset
import matplotlib.pyplot as plt
data_seguridad_alimentaria.boxplot(return_type="dict")
plt.show()


# In[168]:


# Para ver si hay valores atípicos o outliers en la tabla analizada se calcula los estadísticos para el boxplot de la data analizada
data_seguridad_alimentaria.describe()


# In[169]:


# Se reemplazan los valores nulos por la mediana
reemplazar_NA = data_seguridad_alimentaria.fillna(data_seguridad_alimentaria.median(), inplace=True)
data_seguridad_alimentaria.head()


# In[170]:


# Exportar los datos en formato csv 
data_seguridad_alimentaria.to_csv('Data_Seguridad_Alimentaria.csv', index = True)


# In[171]:


# Exportar los datos en formato csv 
data1.to_csv('Data_inseguridad.csv', index = True)


# In[ ]:


# Unión de la base de datos de agricultura con la variable dependiente Seguridad alimentaria


# In[172]:


data_agricultura_seguridad=pd.merge(data_agricultura,data2, how='inner', on=["Año"])
data_agricultura_seguridad.head()


# In[173]:


# Exportar los datos en formato csv 
data_agricultura_seguridad.to_csv('Data_Agricultura_seguridad.csv', index = True)


# ### RELACIÓN ENTRE LAS VARIABLES

# In[145]:


# Para visualizar la relación entre la agricultura y la seguridad alimentaria e se realiza el siguiente gráfico

import matplotlib.pyplot as plt
plt.style.use('ggplot')

data_agricultura_seguridad.plot(x="Indice_alimentos", y="Desnutricion", style='.',color='red', legend=False)
plt.title("Agricultura VS.Seguridad Alimentaria")
plt.xlabel("Agricultura")
plt.ylabel("Seguridad Alimentaria")
plt.show()


# In[146]:


# Se puede hacer una Matriz de correlación de Pearson para ver mejor las relaciones entre las variables, 

import numpy as np
import seaborn as sns

lista = ["Desnutricion","Indice_alimentos","Indice_produccion_animal","PBI_agricultura","Empleo_total","Importaciones","Exportaciones","Indice_cosecha","Empleo_hombres","Empleo_mujeres","Tierras_agrícolas","Tierras_cultivables","PBI"]

# Se genera una matriz de False del tamaño de la correlación
mask = np.zeros_like(data_agricultura_seguridad[lista].corr(), dtype=np.bool) 

# Se hace True la digonal superior
mask[np.triu_indices_from(mask)] = True 

f, ax = plt.subplots(figsize=(10, 10))
plt.title('Matriz de correlación de Pearson',fontsize=25)

# Se realiza la matriz de correlación
sns.heatmap(data_agricultura_seguridad[lista].corr(),linewidths=0.25,vmax=0.7,square=True,cmap="magma",
            linecolor='w',annot=True,annot_kws={"size":8},mask=mask, cbar_kws={"shrink": .9});


# ### MODELO DE REGRESIÓN LINEAL

# In[ ]:


# Para crear un modelo de Regresión Lineal que mejor explique la variable Seguridad Alimentaria, 
# se realizan los siguientes pasos:


# In[169]:


import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd


# In[ ]:


# MODELO DE REGRESIÓN LINEAL MÚLTIPLE


# In[179]:


# Se puede estimar de diferentes formas, en este caso se ha elegido el siguiente modelo:

# Establecer la regresión a estimar
modelo = smf.ols(formula = 'Desnutricion ~ PBI_agricultura + Empleo_total + Exportaciones + Importaciones', data= data_agricultura_seguridad)
# Resultados del ajuste 
resultados = modelo.fit()
# Imprimir el resultado
print(resultados.summary())


# In[180]:


from math import sqrt
from sklearn.metrics import mean_squared_error

observaciones= data_agricultura_seguridad[["Desnutricion"]]
predicciones= resultados.predict()

print(sqrt(mean_squared_error(observaciones,predicciones)))


# ### VISUALIZACIÓN DE DATOS

# In[313]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pylab as pl
import matplotlib.colors as mcolors
import plotly.graph_objects as go


# In[206]:


# Paleta de colores para matplotlib

def plot_colortable(colors, title, sort_colors=True, emptycols=0):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12
    topmargin = 40

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))),
                         name)
                        for name, color in colors.items())
        names = [name for hsv, name in by_hsv]
    else:
        names = list(colors)

    n = len(names)
    ncols = 4 - emptycols
    nrows = n // ncols + int(n % ncols > 0)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + margin + topmargin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-topmargin)/height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    ax.set_title(title, fontsize=24, loc="left", pad=10)

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig

plot_colortable(mcolors.BASE_COLORS, "Base Colors",
                sort_colors=False, emptycols=1)
plot_colortable(mcolors.TABLEAU_COLORS, "Tableau Palette",
                sort_colors=False, emptycols=2)

plot_colortable(mcolors.CSS4_COLORS, "CSS Colors")


# In[361]:


# Indicador: Tierras agrícolas y cultivables

plt.rcParams["figure.figsize"] = (11, 5)
fig, ax = plt.subplots()
Año = data_agricultura_seguridad['Año']
Tierras_agrícolas, =plt.plot(Año, data_agricultura_seguridad['Tierras_agrícolas'], marker = '^', color='darkviolet')
Tierras_cultivables, =plt.plot(Año, data_agricultura_seguridad['Tierras_cultivables'], marker = 'o', color='lawngreen')
plt.legend ([Tierras_agrícolas,Tierras_cultivables],  ['Tierras_agrícolas','Tierras_cultivables'])
plt.title("Tierras agrícolas y cultivables")
plt.xlabel("Año")
plt.ylabel("% Tierras agrícolas y cultivables")
plt.show()


# In[333]:


# Indicador: Empleos de hombres y mujeres en la agricultura
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data_agricultura_seguridad['Año'],
        y=data_agricultura_seguridad['Empleo_hombres'],
        name="% Empleo hombres",
        mode='lines+markers', 
        marker= dict(size=9,
                     symbol = 'diamond',
                     color ='RGB(251, 177, 36)',
                     line_width = 2
                   ),
        line = dict(color='firebrick', width=3)
    ))
fig.add_trace(
    go.Bar(
        x=data_agricultura_seguridad['Año'],
        y=data_agricultura_seguridad['Empleo_mujeres'],
        name="% Empleo mujeres",       
        text = data_agricultura_seguridad['Empleo_mujeres'],
        textposition='outside',
        textfont=dict(
        size=13,
        color='#1f77b4'),
        marker_color=data_agricultura_seguridad['PBI'],
        marker_line_color='rgb(17, 69, 126)',
        marker_line_width=2, 
        opacity=0.7
    ))


# In[297]:


# Indicador: Exportaciones de alimentos
plt.rcParams["figure.figsize"] = (11, 5)
fig, ax = plt.subplots()
ax.fill_between(data_agricultura_seguridad["Año"], data_agricultura_seguridad["Exportaciones"], color='sandybrown')
plt.title("Exportaciones de alimentos")
plt.xlabel("Año")
plt.ylabel("% Exportaciones")
plt.show()


# In[298]:


# Indicador: Importaciones de alimentos
plt.rcParams["figure.figsize"] = (11, 5)
fig, ax = plt.subplots()
ax.fill_between(data_agricultura_seguridad["Año"], data_agricultura_seguridad["Importaciones"], color="rosybrown")
plt.title("Importaciones de alimentos")
plt.xlabel("Año")
plt.ylabel("% Importaciones")
plt.show()


# In[295]:


# Indicador: Inseguridad alimentaria
fig, ax = plt.subplots()
ax.barh(data1["Año"], data1["Inseguridad_alimentaria"], color="mediumaquamarine")
plt.title("Inseguridad alimentaria severa")
plt.xlabel("Año")
plt.ylabel("% Inseguridad alimentaria severa")
plt.show()


# ### Referencias:

# * FAO. (2011). Una introducción a los conceptos básicos de la seguridad alimentaria. Obtenido de https://www.fao.org/3/al936s/al936s00.pdf

# ### Fuentes:

# * https://datos.bancomundial.org/indicator?tab=all
