# Análisis de la Agricultura y Seguridad Alimentaria en el Perú 
Noviembre-2021
![](https://portal.andina.pe/EDPfotografia3/Thumbnail/2021/03/05/000754579W.jpg)
### Descripción y motivación
------------
Este proyecto tiene como objetivo analizar los principales indicadores de la agricultura y la seguridad alimentaria en el Perú; así como la relación y el impacto de la agricultura en la seguridad alimentaria durante los años 2001-2019. Todo ello a fin de generar evidencia que apoye al Ministerio de Desarrollo Agrario y Riego, a tomar mejores decisiones en la formulación de Políticas públicas orientadas al desarrollo sostenible del sector agrícola y a garantizar la seguridad alimentaria en el Perú.

Las preguntas que motivaron el proyecto son las siguientes
- ¿Qué reflejan las estadísticas descriptivas de los datos sobre la agricultura en el Perú?
- ¿Qué reflejan las estadísticas descriptivas de los datos sobre la seguridad alimentaria en el Perú?
- ¿De qué manera se relaciona la agricultura con la seguridad alimentaria en el Perú?
- ¿Cuál es el impacto de la agricultura en la seguridad alimentaria del Perú durante los años 2001-2019?

### Métodos utilizados
------------
1. Extracción de datos usando API:
Para ello se utilizaron las siguientes fuentes de datos:
- Parte 1 - Banco Mundial (2001-2019): https://datos.bancomundial.org/indicator
- Parte 2 - Banco Central de Reserva del Perú (2007-2020) : https://estadisticas.bcrp.gob.pe/estadisticas/series/
- Parte 2 - Sistema Integrado de Estadísticas Agrarias - SIEA (2019): https://siea.midagri.gob.pe/portal/siea_bi/index.html
 
2. Procesamiento y limpieza de datos:
Para ello utilicé Python con la librería Pandas y Requests.

3. Análisis y visualización de datos:
- Python: con las librerías NumPy, Matplotlib, Seaborn, Pylab. Así mismo para estimar el modelo de regresión lineal, usé Statsmodels y Pandas.
- Tableau
- Power Bi

El código para la Parte 1 está disponible aquí: https://github.com/pmanriquec/Agricultura-y-seguridad-alimentaria/blob/9e2063a2bf45888c2b341aa5ceb9ecd7784947d1/PROYECTO%20PARTE%201%20-%20Perla%20Manrique%20Cruz.ipynb

El código para la Parte 2 está disponible aquí: https://github.com/pmanriquec/Agricultura-y-seguridad-alimentaria/blob/main/PROYECTO%20PARTE%202%20-%20Perla%20Manrique%20Cruz.ipynb

### Resultados
A continuación se muestra los resultados más relevantes:
- Agricultura en el Perú

El PBI peruano ha experimentado un notable crecimiento en los años 2001-2019; sin embargo, el porcentaje del PIB que ha representado el sector agrícola ha decrecido alrededor de 1%.
<img src=https://github.com/pmanriquec/Agricultura-y-seguridad-alimentaria/blob/3c71b4e3218f384580109c44667fe69425768450/PBI%20Agricultura.png />

La evolución anual del índice de producción de alimentos y animal en el Perú, representa un crecimiento constante desde el 2001 hasta el 2018, teniendo en el 2019 una drástica caída, y siendo la producción de alimentos mayor que la producción animal.
<img src=https://github.com/pmanriquec/Agricultura-y-seguridad-alimentaria/blob/main/Produccion.png />


