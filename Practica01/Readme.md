Alumna: Ana Valeria Deloya Andrade

Para ejecutar el programa, poner en terminal: python3 Practica1.py


*** Sobre la forma en que funcionan las ventas: 

La idea es que el usuario registre las compras con la opción "6 Para registrar una compra" en el menú de inicio.
Por cada compra que quiera hacer durante el día debe de seleccionar esa  opción en el menú. 

La compras durante el dia se van registrando en "ventas.csv", que es un archivo auxiliar para registrarlas.

Al final de día que el usuario quiera consultar el monto total de todas las ventas del dia, debe seleccionar en el menú de inicio la opcion "7 Para ver las ventas totales del dia". 
Con esa opción sale la suma ventas registradas en el archivo auxiliar y el monto total junto con la fecha del día son registrados en "ventas_totales.csv". 
Cuando esto pase, todas las ventas del día serán eliminadas de "ventas.csv"; esto con la idea de que se puedan registrar y sumar nuevas compras, del día siguiente.