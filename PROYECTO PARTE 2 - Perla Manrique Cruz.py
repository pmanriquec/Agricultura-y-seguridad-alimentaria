#!/usr/bin/env python
# coding: utf-8

# ### PROYECTO: AGRICULTURA Y SEGURIDAD ALIMENTARIA EN EL PERÚ

# * En esta segunda parte del Proyecto se obtuvieron los datos con el API del Banco Central de Reserva del Perú y se importaron datos del Sistema Integrado de Estadística Agraria (SIEA) del Ministerio de Desarrollo Agrario y Riego del Perú. La información que se extrajo está relacionada con la producción agrícola y pecuaria por cada despartamento del Perú y por año, a fin de conocer la evolución de los pincipales cultivos agropecuarios que caracterizan al Perú.

# In[1]:


# IMPORTANDO DATOS DEL 2019 DEL SISTEMA INTEGRADO DE ESTADÍSTICA AGRARIA (SIEA) - MINISTERIO DE DESARROLLO AGRARIO Y RIEGO 


# In[1]:


import pandas as pd
file = "PRODUCCION AGRICOLA POR DEPARTAMENTO 2019.csv"
produccion_agricola_dpto = pd.read_csv(file)
produccion_agricola_dpto.head()


# In[10]:


# Verificar si hay valores nulos
produccion_agricola_dpto1=produccion_agricola_dpto.isnull()
produccion_agricola_dpto1


# In[11]:


# Exportar los datos en formato csv 
produccion_agricola_dpto1.to_csv('Data_produccion_agricola_dpto.csv', index = True)


# In[ ]:


# EXTRACCIÓN DE DATOS USANDO API - BANCO CENTRAL DE RESERVA DEL PERÚ


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE PAPA


# In[12]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01777AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[13]:


import requests
response=requests.get(url)
print(response)


# In[14]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[15]:


for key in response_json.keys():
    print(key)


# In[16]:


print(response_json["config"])


# In[17]:


print(response_json["periods"])


# In[18]:


periodos=response_json.get("periods")
prod_papa=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_papa.append(w)
        
print(prod_papa)


# In[19]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[21]:


diccionario1= {"Fechas":fechas, "Valores":prod_papa}
print(diccionario1)


# In[22]:


df1=pd.DataFrame(diccionario1)
df1


# In[23]:


df1.rename(columns={'Valores':'Papa'}, inplace=True)
df1.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE ARROZ CÁSCARA


# In[24]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01778AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[25]:


import requests
response=requests.get(url)
print(response)


# In[26]:


# extraer en formato json
response_json=response.json()


# In[27]:


for key in response_json.keys():
    print(key)


# In[28]:


print(response_json["config"])


# In[29]:


# llamar a los valores
print(response_json["periods"])


# In[30]:


periodos=response_json.get("periods")
prod_arroz=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_arroz.append(w)
print(prod_arroz)


# In[31]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[32]:


diccionario2= {"Fechas":fechas, "Valores":prod_arroz}
print(diccionario2)


# In[33]:


df2=pd.DataFrame(diccionario2)
df2


# In[34]:


df2.rename(columns={'Valores':'Arroz'}, inplace=True)
df2.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE CEBOLLA


# In[35]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01779AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[36]:


import requests
response=requests.get(url)
print(response)


# In[37]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[38]:


for key in response_json.keys():
    print(key)


# In[39]:


print(response_json["config"])


# In[40]:


# llamar a los valores
print(response_json["periods"])


# In[41]:


periodos=response_json.get("periods")
prod_cebolla=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_cebolla.append(w)
print(prod_cebolla)


# In[42]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[43]:


diccionario3= {"Fechas":fechas, "Valores":prod_cebolla}
print(diccionario3)


# In[44]:


df3=pd.DataFrame(diccionario3)
df3


# In[45]:


df3.rename(columns={'Valores':'Cebolla'}, inplace=True)
df3.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE MANDARINA


# In[46]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01780AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[47]:


import requests
response=requests.get(url)
print(response)


# In[48]:


# extraer en formato json
response_json=response.json()


# In[49]:


for key in response_json.keys():
    print(key)


# In[50]:


print(response_json["config"])


# In[51]:


# llamar a los valores
print(response_json["periods"])


# In[52]:


periodos=response_json.get("periods")
prod_mandarina=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_mandarina.append(w)
        
print(prod_mandarina)


# In[53]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[54]:


diccionario4= {"Fechas":fechas, "Valores":prod_mandarina}
print(diccionario4)


# In[55]:


df4=pd.DataFrame(diccionario4)
df4


# In[56]:


df4.rename(columns={'Valores':'Mandarina'}, inplace=True)
df4.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE NARANJA


# In[57]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01781AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[58]:


import requests
response=requests.get(url)
print(response)


# In[59]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[60]:


for key in response_json.keys():
    print(key)


# In[61]:


print(response_json["config"])


# In[62]:


# llamar a los valores
print(response_json["periods"])


# In[63]:


periodos=response_json.get("periods")
prod_naranja=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_naranja.append(w)
        
print(prod_naranja)


# In[64]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[65]:


diccionario5= {"Fechas":fechas, "Valores":prod_naranja}
print(diccionario5)


# In[66]:


import pandas as pd
df5=pd.DataFrame(diccionario5)
df5.head()


# In[67]:


df5.rename(columns={'Valores':'Naranja'}, inplace=True)
df5.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE ALFALFA


# In[68]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01782AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[69]:


import requests
response=requests.get(url)
print(response)


# In[70]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[71]:


for key in response_json.keys():
    print(key)


# In[72]:


print(response_json["config"])


# In[73]:


# llamar a los valores
print(response_json["periods"])


# In[74]:


periodos=response_json.get("periods")
prod_alfalfa=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_alfalfa.append(w)
        
print(prod_alfalfa)


# In[75]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[77]:


diccionario6= {"Fechas":fechas, "Valores":prod_alfalfa}
print(diccionario6)


# In[78]:


df6=pd.DataFrame(diccionario6)
df6


# In[79]:


df6.rename(columns={'Valores':'Alfalfa'}, inplace=True)
df6.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE TOMATE


# In[80]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01783AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[81]:


import requests
response=requests.get(url)
print(response)


# In[82]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[83]:


for key in response_json.keys():
    print(key)


# In[84]:


print(response_json["config"])


# In[85]:


# llamar a los valores
print(response_json["periods"])


# In[86]:


periodos=response_json.get("periods")
prod_tomate=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_tomate.append(w)
        
print(prod_tomate)


# In[87]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[88]:


diccionario7= {"Fechas":fechas, "Valores":prod_tomate}
print(diccionario7)


# In[89]:


df7=pd.DataFrame(diccionario7)
df7


# In[90]:


df7.rename(columns={'Valores':'Tomate'}, inplace=True)
df7.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE PLÁTANO


# In[91]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01784AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[92]:


import requests
response=requests.get(url)
print(response)


# In[93]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[94]:


for key in response_json.keys():
    print(key)


# In[95]:


print(response_json["config"])


# In[96]:


# llamar a los valores
print(response_json["periods"])


# In[97]:


print(response_json["periods"])


# In[98]:


periodos=response_json.get("periods")
prod_plátano=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_plátano.append(w)
        
print(prod_plátano)


# In[99]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[100]:


diccionario8= {"Fechas":fechas, "Valores":prod_plátano}
print(diccionario8)


# In[101]:


df8=pd.DataFrame(diccionario8)
df8


# In[102]:


df8.rename(columns={'Valores':'Plátano'}, inplace=True)
df8.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE YUCA


# In[103]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01785AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[104]:


import requests
response=requests.get(url)
print(response)


# In[105]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[106]:


for key in response_json.keys():
    print(key)


# In[107]:


print(response_json["config"])


# In[108]:


# llamar a los valores
print(response_json["periods"])


# In[109]:


periodos=response_json.get("periods")
prod_yuca=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_yuca.append(w)
        
print(prod_yuca)


# In[110]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[111]:


diccionario9= {"Fechas":fechas, "Valores":prod_yuca}
print(diccionario9)


# In[112]:


df9=pd.DataFrame(diccionario9)
df9


# In[113]:


df9.rename(columns={'Valores':'Yuca'}, inplace=True)
df9.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE LIMÓN


# In[114]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01788AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[115]:


import requests
response=requests.get(url)
print(response)


# In[116]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[117]:


for key in response_json.keys():
    print(key)


# In[118]:


print(response_json["config"])


# In[119]:


# llamar a los valores
print(response_json["periods"])


# In[120]:


periodos=response_json.get("periods")
prod_limón=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_limón.append(w)
        
print(prod_limón)


# In[121]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[122]:


diccionario10= {"Fechas":fechas, "Valores":prod_limón}
print(diccionario10)


# In[123]:


df10=pd.DataFrame(diccionario10)
df10


# In[124]:


df10.rename(columns={'Valores':'Limón'}, inplace=True)
df10.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE CAFÉ


# In[125]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01789AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[126]:


import requests
response=requests.get(url)
print(response)


# In[127]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[128]:


for key in response_json.keys():
    print(key)


# In[129]:


print(response_json["config"])


# In[130]:


# llamar a los valores
print(response_json["periods"])


# In[131]:


periodos=response_json.get("periods")
prod_café=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_café.append(w)
        
print(prod_café)


# In[132]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[133]:


diccionario11= {"Fechas":fechas, "Valores":prod_café}
print(diccionario11)


# In[134]:


df11=pd.DataFrame(diccionario11)
df11


# In[135]:


df11.rename(columns={'Valores':'Café'}, inplace=True)
df11.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE CAÑA DE AZÚCAR


# In[136]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01790AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[137]:


import requests
response=requests.get(url)
print(response)


# In[138]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[139]:


for key in response_json.keys():
    print(key)


# In[140]:


print(response_json["config"])


# In[141]:


# llamar a los valores
print(response_json["periods"])


# In[142]:


periodos=response_json.get("periods")
prod_caña_azúcar=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_caña_azúcar.append(w)
        
print(prod_caña_azúcar)


# In[143]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[144]:


diccionario12= {"Fechas":fechas, "Valores":prod_caña_azúcar}
print(diccionario12)


# In[145]:


df12=pd.DataFrame(diccionario12)
df12


# In[146]:


df12.rename(columns={'Valores':'Caña_azúcar'}, inplace=True)
df12.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE ESPÁRRAGO


# In[147]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01792AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[148]:


import requests
response=requests.get(url)
print(response)


# In[149]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[150]:


for key in response_json.keys():
    print(key)


# In[151]:


print(response_json["config"])


# In[152]:


# llamar a los valores
print(response_json["periods"])


# In[153]:


periodos=response_json.get("periods")
prod_espárrago=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_espárrago.append(w)
        
print(prod_espárrago)


# In[154]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[155]:


diccionario13= {"Fechas":fechas, "Valores":prod_espárrago}
print(diccionario13)


# In[156]:


df13=pd.DataFrame(diccionario13)
df13


# In[157]:


df13.rename(columns={'Valores':'Espárrago'}, inplace=True)
df13.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE MANGO


# In[158]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01795AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[159]:


import requests
response=requests.get(url)
print(response)


# In[160]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[161]:


for key in response_json.keys():
    print(key)


# In[162]:


print(response_json["config"])


# In[163]:


# llamar a los valores
print(response_json["periods"])


# In[164]:


periodos=response_json.get("periods")
prod_mango=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_mango.append(w)
        
print(prod_mango)


# In[165]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[167]:


diccionario14= {"Fechas":fechas, "Valores":prod_mango}
print(diccionario14)


# In[168]:


df14=pd.DataFrame(diccionario14)
df14


# In[169]:


df14.rename(columns={'Valores':'Mango'}, inplace=True)
df14.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE CACAO


# In[170]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01796AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[171]:


import requests
response=requests.get(url)
print(response)


# In[172]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[173]:


for key in response_json.keys():
    print(key)


# In[174]:


print(response_json["config"])


# In[175]:


# llamar a los valores
print(response_json["periods"])


# In[176]:


periodos=response_json.get("periods")
prod_cacao=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_cacao.append(w)
        
print(prod_cacao)


# In[177]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[178]:


diccionario15= {"Fechas":fechas, "Valores":prod_cacao}
print(diccionario15)


# In[179]:


df15=pd.DataFrame(diccionario15)
df15


# In[180]:


df15.rename(columns={'Valores':'Cacao'}, inplace=True)
df15.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE PALMA ACEITERA


# In[181]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01797AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[182]:


import requests
response=requests.get(url)
print(response)


# In[183]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[184]:


for key in response_json.keys():
    print(key)


# In[185]:


print(response_json["config"])


# In[186]:


# llamar a los valores
print(response_json["periods"])


# In[187]:


periodos=response_json.get("periods")
prod_palma_aceitera=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_palma_aceitera.append(w)
        
print(prod_palma_aceitera)


# In[188]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[190]:


diccionario16= {"Fechas":fechas, "Valores":prod_palma_aceitera}
print(diccionario16)


# In[191]:


df16=pd.DataFrame(diccionario16)
df16


# In[192]:


df16.rename(columns={'Valores':'Palma_aceitera'}, inplace=True)
df16.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE QUINUA


# In[193]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01798AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[194]:


import requests
response=requests.get(url)
print(response)


# In[195]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[196]:


for key in response_json.keys():
    print(key)


# In[197]:


print(response_json["config"])


# In[198]:


# llamar a los valores
print(response_json["periods"])


# In[199]:


periodos=response_json.get("periods")
prod_quinua=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_quinua.append(w)
        
print(prod_quinua)


# In[200]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[201]:


diccionario17= {"Fechas":fechas, "Valores":prod_quinua}
print(diccionario17)


# In[202]:


df17=pd.DataFrame(diccionario17)
df17


# In[203]:


df17.rename(columns={'Valores':'Quinua'}, inplace=True)
df17.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE UVA


# In[204]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01793AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[207]:


import requests
response=requests.get(url)
print(response)


# In[208]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[209]:


for key in response_json.keys():
    print(key)


# In[210]:


print(response_json["config"])


# In[211]:


# llamar a los valores
print(response_json["periods"])


# In[212]:


periodos=response_json.get("periods")
prod_uva=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_uva.append(w)
        
print(prod_uva)


# In[213]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[214]:


diccionario18= {"Fechas":fechas, "Valores":prod_uva}
print(diccionario18)


# In[215]:


df18=pd.DataFrame(diccionario18)
df18


# In[216]:


df18.rename(columns={'Valores':'Uva'}, inplace=True)
df18.head()


# In[ ]:


# DATOS DE PRODUCCIÓN AGRÍCOLA DE MAÍZ AMARILLO DURO


# In[217]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01791AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[218]:


import requests
response=requests.get(url)
print(response)


# In[219]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[220]:


for key in response_json.keys():
    print(key)


# In[221]:


print(response_json["config"])


# In[222]:


# llamar a los valores
print(response_json["periods"])


# In[223]:


periodos=response_json.get("periods")
prod_maíz=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_maíz.append(w)
        
print(prod_maíz)


# In[224]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[225]:


diccionario19= {"Fechas":fechas, "Valores":prod_maíz}
print(diccionario19)


# In[226]:


df19=pd.DataFrame(diccionario19)
df19


# In[227]:


df19.rename(columns={'Valores':'Maíz'}, inplace=True)
df19.head()


# In[ ]:


# DATOS DE PRODUCCIÓN PECUARIA DE AVE


# In[228]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01800AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[229]:


import requests
response=requests.get(url)
print(response)


# In[230]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[231]:


for key in response_json.keys():
    print(key)


# In[232]:


print(response_json["config"])


# In[233]:


# llamar a los valores
print(response_json["periods"])


# In[234]:


periodos=response_json.get("periods")
prod_ave=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_ave.append(w)
        
print(prod_ave)


# In[235]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[236]:


diccionario20= {"Fechas":fechas, "Valores":prod_ave}
print(diccionario20)


# In[237]:


df20=pd.DataFrame(diccionario20)
df20


# In[238]:


df20.rename(columns={'Valores':'Ave'}, inplace=True)
df20.head()


# In[ ]:


# DATOS DE PRODUCCIÓN PECUARIA DE VACUNO


# In[239]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01801AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[240]:


import requests
response=requests.get(url)
print(response)


# In[241]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[242]:


for key in response_json.keys():
    print(key)


# In[243]:


print(response_json["config"])


# In[244]:


# llamar a los valores
print(response_json["periods"])


# In[245]:


periodos=response_json.get("periods")
prod_vacuno=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_vacuno.append(w)
        
print(prod_vacuno)


# In[246]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[247]:


diccionario21= {"Fechas":fechas, "Valores":prod_vacuno}
print(diccionario21)


# In[248]:


df21=pd.DataFrame(diccionario21)
df21


# In[249]:


df21.rename(columns={'Valores':'Vacuno'}, inplace=True)
df21.head()


# In[ ]:


# DATOS DE PRODUCCIÓN PECUARIA DE HUEVOS


# In[250]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01802AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[251]:


import requests
response=requests.get(url)
print(response)


# In[252]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[253]:


for key in response_json.keys():
    print(key)


# In[254]:


print(response_json["config"])


# In[255]:


# llamar a los valores
print(response_json["periods"])


# In[256]:


periodos=response_json.get("periods")
prod_huevos=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_huevos.append(w)
        
print(prod_huevos)


# In[257]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[258]:


diccionario22= {"Fechas":fechas, "Valores":prod_huevos}
print(diccionario22)


# In[259]:


df22=pd.DataFrame(diccionario22)
df22


# In[260]:


df22.rename(columns={'Valores':'Huevos'}, inplace=True)
df22.head()


# In[ ]:


# DATOS DE PRODUCCIÓN PECUARIA DE PORCINO


# In[261]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01803AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[262]:


import requests
response=requests.get(url)
print(response)


# In[263]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[264]:


for key in response_json.keys():
    print(key)


# In[265]:


print(response_json["config"])


# In[266]:


# llamar a los valores
print(response_json["periods"])


# In[267]:


periodos=response_json.get("periods")
prod_porcino=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_porcino.append(w)
        
print(prod_porcino)


# In[268]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[269]:


diccionario23= {"Fechas":fechas, "Valores":prod_porcino}
print(diccionario23)


# In[270]:


df23=pd.DataFrame(diccionario23)
df23


# In[271]:


df23.rename(columns={'Valores':'Porcino'}, inplace=True)
df23.head()


# In[ ]:


# DATOS DE PRODUCCIÓN PECUARIA DE LECHE


# In[272]:


url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
cod_ser="PN01804AM"
formato="/json"
per="/2003-1/2020-12"
url=url_base+cod_ser+formato+per
print(url)


# In[273]:


import requests
response=requests.get(url)
print(response)


# In[274]:


# extraer en formato json
response_json=response.json()
print(response_json)


# In[275]:


for key in response_json.keys():
    print(key)


# In[276]:


print(response_json["config"])


# In[277]:


# llamar a los valores
print(response_json["periods"])


# In[278]:


periodos=response_json.get("periods")
prod_leche=[]
for i in periodos:
    valores_list=i["values"]
    for w in valores_list:
        w=str(w)
        prod_leche.append(w)
        
print(prod_leche)


# In[279]:


fechas=[]
for i in periodos:
    nombres=i["name"]
    fechas.append(nombres)
print(fechas)


# In[280]:


diccionario24= {"Fechas":fechas, "Valores":prod_leche}
print(diccionario24)


# In[281]:


df24=pd.DataFrame(diccionario24)
df24


# In[282]:


df24.rename(columns={'Valores':'Leche'}, inplace=True)
df24.head()


# ### Unión de datas

# In[283]:


import pandas as pd
datafinal1=pd.merge(df1,df2, how='inner', on=["Fechas"])
datafinal1.head()


# In[284]:


datafinal2=pd.merge(datafinal1,df3, how='inner', on=["Fechas"])
datafinal2.head()


# In[285]:


datafinal3=pd.merge(datafinal2,df4, how='inner', on=["Fechas"])
datafinal3.head()


# In[286]:


datafinal4=pd.merge(datafinal3,df5, how='inner', on=["Fechas"])
datafinal4.head()


# In[287]:


datafinal5=pd.merge(datafinal4,df6, how='inner', on=["Fechas"])
datafinal5.head()


# In[288]:


datafinal6=pd.merge(datafinal5,df7, how='inner', on=["Fechas"])
datafinal6.head()


# In[289]:


datafinal7=pd.merge(datafinal6,df8, how='inner', on=["Fechas"])
datafinal7.head()


# In[290]:


datafinal8=pd.merge(datafinal7,df9, how='inner', on=["Fechas"])
datafinal8.head()


# In[291]:


datafinal9=pd.merge(datafinal8,df10, how='inner', on=["Fechas"])
datafinal9.head()


# In[292]:


datafinal10=pd.merge(datafinal9,df11, how='inner', on=["Fechas"])
datafinal10.head()


# In[293]:


datafinal11=pd.merge(datafinal10,df12, how='inner', on=["Fechas"])
datafinal11.head()


# In[294]:


datafinal12=pd.merge(datafinal11,df13, how='inner', on=["Fechas"])
datafinal12.head()


# In[295]:


datafinal13=pd.merge(datafinal12,df14, how='inner', on=["Fechas"])
datafinal13.head()


# In[296]:


datafinal14=pd.merge(datafinal13,df15, how='inner', on=["Fechas"])
datafinal14.head()


# In[297]:


datafinal15=pd.merge(datafinal14,df16, how='inner', on=["Fechas"])
datafinal15.head()


# In[298]:


datafinal16=pd.merge(datafinal15,df17, how='inner', on=["Fechas"])
datafinal16.head()


# In[299]:


datafinal17=pd.merge(datafinal16,df18, how='inner', on=["Fechas"])
datafinal17.head()


# In[300]:


datafinal18=pd.merge(datafinal17,df19, how='inner', on=["Fechas"])
datafinal18.head()


# In[301]:


datafinal19=pd.merge(datafinal18,df20, how='inner', on=["Fechas"])
datafinal19.head()


# In[302]:


datafinal20=pd.merge(datafinal19,df21, how='inner', on=["Fechas"])
datafinal20.head()


# In[303]:


datafinal21=pd.merge(datafinal20,df22, how='inner', on=["Fechas"])
datafinal21.head()


# In[304]:


datafinal22=pd.merge(datafinal21,df23, how='inner', on=["Fechas"])
datafinal22.head()


# In[305]:


data_produccion_agropecuaria=pd.merge(datafinal22,df24, how='inner', on=["Fechas"])
data_produccion_agropecuaria.head()


# In[306]:


# Verificar si hay valores nulos
data_produccion_agropecuaria1=data_produccion_agropecuaria.isnull()
data_produccion_agropecuaria1


# In[307]:


# Exportar los datos en formato csv 
data_produccion_agropecuaria.to_csv('Data_produccion_agropecuaria.csv', index = True)


# ### FUENTES:

# * https://estadisticas.bcrp.gob.pe/estadisticas/series/
# * https://siea.midagri.gob.pe/portal/siea_bi/index.html
