# Documentaci贸n de la pr谩ctica 2 de Sistemas distribuidos


## Arquitectura del proyecto 馃殌

Para la pr谩ctica en un principio se pens贸 en realizar todas las fases,
pero por falta de tiempo se ha optado por realizar tan solo las dos 煤ltimas fases
las cuales constan de la fase 2 en la cual se realiza un merge de dos documentos csv que hemos 
cogido de la p谩gina [enlace](https://analisi.transparenciacatalunya.cat/browse?&page=2) y por otro lado
las consultas sobre el csv resultante de fusionar estos dos.

Se plante贸 la idea de en vez de coger los nombres de los ficheros, trabajar con la libreria OS que se puede 
utilizar en la nube, que posibilita ver todos los archivos e ir cogiendo los que hay. Pero para simplificar el programa
ponemos el nombre de los ficheros en un .env que nadie podr谩 ver y los tratamos directamente.

Por otro lado tenemos las librer铆as y funciones que nos otorga IBM para trabajar:

* IBM Cloud Functions: Es la nube de IBM donde podemos ejecutar el c贸digo de manera remota y con mayor potencia que en local.
* main.py: Por otro lado tenemos el fichero principal del proyecto, el cual contiene el c贸digo para fusionar nuestros dos datasets
escogidos para esta pr谩ctica.
* .env y los yml: nos permiten definir las variables de entorno y la configuraci贸n con la nube de IBM
* IBM Cloud Storage: Es la nube de almacenamiento que nos ha proporcionado IBM para poder realizar la pr谩ctica y guardar la informaci贸n


### Decisiones de dise帽o 馃搵

Como se ha comentado con anterioridad, en un primer momento se plante贸 la idea de la realizaci贸n de las 3 fases
pero por falta de tiempo se opt贸 por realizar 煤nicamente las dos 煤ltimas. Para estas dos fases hacemos uso de datasets externos
proporcionados por la p谩gina que se puso en el punto anterior.

Para trabajar con ellos hacemos uso de las funciones de la nube de IBM y trabajamos sobre ella, cogiendo los dos documentos,
pasandole el bucket donde tenemos los csv y los nombres de estos y los procesamos para fusionarlos. Una vez fusionados los guardamos nuevamente
con un nombre nuevo (database) en el bucket para posteriormente poder analizarlo.

Finalmente pasamos a la fase de las consultas, para estas hacemos uso de la libreria pandas, que nos permite utilizar los CSV como BD's
De pandas usamos diversas funciones como por ejemplo getData, graph_plot para gr谩ficos, formatar para las fechas, formato utf-8.

## Tama帽o de los datos 馃洜锔?

La idea original era realizar scrapping de montones de tweets, pero al ver el escaso tiempo del que dispon铆amos y que twitter limita
el volumen de datos que se pueden obtener se descart贸 la idea, con lo cual cogimos dos datasets de 

* [Casos por municipio y sexo](https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-a-Catalunya-per-muni/jj6z-iyrp/data) 218.836 elementos
* [Incidencia COVID-19 Catalu帽a](https://analisi.transparenciacatalunya.cat/Salut/Incid-ncia-de-la-COVID-19-a-Catalunya/623z-r97q/data) 212 elementos
Los datos han sido extra铆dos de: [Info](https://analisi.transparenciacatalunya.cat/browse?&page=2)
 
Con lo cual nos queda una base de datos con un total de 219.048 elementos, no est谩 mal, pero no 茅s tanto como esper谩bamos.

## Computaci贸n 馃洜锔?
La etapa dos al ser simplemente un merge de dos datasets, relativamente peque帽os, no supone un gran esfuerzo para la nube,
en unas primeras etapas del desarrollo donde probamos con tweepy el scrapping de tweets, vimos que supon铆a algo mas de esfuerzo,
pero finalmente vimos que la larga espera que ten铆amos era debido a la limitaci贸n de tweets diarios y que se quedaba en waits muy largos.

Para la fase tres por otro lado, tenemos las consultas sobre la base de datos (el csv database), las cuales son relativamente ligeras
ya que no estamos tratando grandes vol煤menes de datos, algo menos de 50Mb entre ambos ficheros 


