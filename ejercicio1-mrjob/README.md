#Comando para correr los archivos:
*python NOMBREARCHIVO.py datosEmpleados.csv* 

#con hadoop:
*python mr-job.py datosEmpleados.csv -r hadoop  --hadoop-streaming-jar $HADOOP_STREAMING_HOME/hadoop-streaming.jar
