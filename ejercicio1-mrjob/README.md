# Laboratorio MapReduce
##  Punto desarrollado:

## 1. Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.

* Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

1. El salario promedio por Sector Económico (SE)
2. El salario promedio por Empleado
3. Número de SE por Empleado que ha tenido a lo largo de la estadística

##  Comando para correr los programas:
*python NOMBREARCHIVO.py datosEmpleados.csv* 

##  Con hadoop:
*python mr-job.py datosEmpleados.csv -r hadoop  --hadoop-streaming-jar $HADOOP_STREAMING_HOME/hadoop-streaming.jar
