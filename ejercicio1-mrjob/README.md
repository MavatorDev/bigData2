Laboratorio MapReduce
1. Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.
datasets de ejemplo

La estructura del archivo es: (sececon: sector económico) (archivo: dataempleados.csv)

idemp,sececon,salary,year

3233,1234,35000,1960
3233,5434,36000,1961
1115,3432,34000,1980
3233,1234,40000,1965
1115,1212,77000,1980
1115,1412,76000,1981
1116,1412,76000,1982
Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

El salario promedio por Sector Económico (SE)
El salario promedio por Empleado
Número de SE por Empleado que ha tenido a lo largo de la estadística

#Comando para correr los archivos:
*python NOMBREARCHIVO.py datosEmpleados.csv* 

#con hadoop:
*python mr-job.py datosEmpleados.csv -r hadoop  --hadoop-streaming-jar $HADOOP_STREAMING_HOME/hadoop-streaming.jar
