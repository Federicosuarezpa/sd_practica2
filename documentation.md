# Documentación de la práctica 2 de Sistemas distribuidos


## Arquitectura del proyecto 🚀

Para la práctica en un principio se pensó en realizar todas las fases,
pero por falta de tiempo se ha optado por realizar tan solo las dos últimas fases
las cuales constan de la fase 2 en la cual se realiza un merge de dos documentos csv que hemos 
cogido de la página [enlace](https://analisi.transparenciacatalunya.cat/browse?&page=2) y por otro lado
las consultas sobre el csv resultante de fusionar estos dos.

Se planteó la idea de en vez de coger los nombres de los ficheros, trabajar con la libreria OS que se puede 
utilizar en la nube, que posibilita ver todos los archivos e ir cogiendo los que hay. Pero para simplificar el programa
ponemos el nombre de los ficheros en un .env que nadie podrá ver y los tratamos directamente.

Por otro lado tenemos las librerías y funciones que nos otorga IBM para trabajar:

* IBM Cloud Functions: Es la nube de IBM donde podemos ejecutar el código de manera remota y con mayor potencia que en local.
* main.py: Por otro lado tenemos el fichero principal del proyecto, el cual contiene el código para fusionar nuestros dos datasets
escogidos para esta práctica.
* .env y los yml: nos permiten definir las variables de entorno y la configuración con la nube de IBM
* IBM Cloud Storage: Es la nube de almacenamiento que nos ha proporcionado IBM para poder realizar la práctica y guardar la información


### Decisiones de diseño 📋

Como se ha comentado con anterioridad, en un primer momento se planteó la idea de la realización de las 3 fases
pero por falta de tiempo se optó por realizar únicamente las dos últimas. Para estas dos fases hacemos uso de datasets externos
proporcionados por la página que se puso en el punto anterior.

Para trabajar con ellos hacemos uso de las funciones de la nube de IBM y trabajamos sobre ella, cogiendo los dos documentos,
pasandole el bucket donde tenemos los csv y los nombres de estos y los procesamos para fusionarlos. Una vez fusionados los guardamos nuevamente
con un nombre nuevo (database) en el bucket para posteriormente poder analizarlo.

Finalmente pasamos a la fase de las consultas, para estas hacemos uso de la libreria pandas, que nos permite utilizar los CSV como BD's
De pandas usamos diversas funciones como por ejemplo getData, graph_plot para gráficos, formatar para las fechas, formato utf-8.

## Tamaño de los datos 🛠️

La idea original era realizar scrapping de montones de tweets, pero al ver el escaso tiempo del que disponíamos y que twitter limita
el volumen de datos que se pueden obtener se descartó la idea, con lo cual cogimos dos datasets de 

* [Casos por municipio y sexo](https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-a-Catalunya-per-muni/jj6z-iyrp/data) 218.836 elementos
* [Incidencia COVID-19 Cataluña](https://analisi.transparenciacatalunya.cat/Salut/Incid-ncia-de-la-COVID-19-a-Catalunya/623z-r97q/data) 212 elementos
Los datos han sido extraídos de: [Info](https://analisi.transparenciacatalunya.cat/browse?&page=2)
 
Con lo cual nos queda una base de datos con un total de 219.048 elementos, no está mal, pero no és tanto como esperábamos.

## Computación 🛠️
La etapa dos al ser simplemente un merge de dos datasets, relativamente pequeños, no supone un gran esfuerzo para la nube,
en unas primeras etapas del desarrollo donde probamos con tweepy el scrapping de tweets, vimos que suponía algo mas de esfuerzo,
pero finalmente vimos que la larga espera que teníamos era debido a la limitación de tweets diarios y que se quedaba en waits muy largos.

Para la fase tres por otro lado, tenemos las consultas sobre la base de datos (el csv database), las cuales son relativamente ligeras
ya que no estamos tratando grandes volúmenes de datos, algo menos de 50Mb entre ambos ficheros 


