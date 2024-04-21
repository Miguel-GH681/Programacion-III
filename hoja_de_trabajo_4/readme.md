
# Hoja de trabajo #4 - API con Arbol AVL
Se construyo una API utilizando la libreria de Flask de Python con  la finalidad de poner en practica nuestros conocimientos a cerca de la estructura de datos del Arbol AVL y las API's.

Los arboles AVL son estructuras de datos que se caracterizan por mantenerse balanceados teniendo un factor de equilibrio -1 <= FE <=1. Por otro lado tambien se implementaron los conocimientos sobre API's que no son mas que una arquitectura que permite la comunicacion entre dos o mas aplicaciones.
## Ejecucion

Cuando se haya clonado el repositorio por favor colocar los siguientes comandos en una terminal

```bash
  cd Programacion-III
  cd hoja_de_trabajo_4
```

Cuando se encuentre dentro de la carpeta adecuada ejecute el siguiente comando en una terminal

```bash
  python3 api.py
```

## Endpoints

- https://bodies-api.onrender.com/cargar - GET: Este endpoint se encarga de llenar el arbol AVL con datos que se obtienen de un archivo CSV

- https://bodies-api.onrender.com/clear_db - GET:
Este endpoint se encarga de vaciar la estructura de datos

- https://bodies-api.onrender.com/get_body?id=225 - GET:
Recibe un parametro llamado 'id' el cual se utiliza para buscar este elemento dentro del arbol AVL

- https://bodies-api.onrender.com/get_info_grupo - GET:
Obtiene la informacion de cada uno de los integrantes del grupo

- http://localhost:3000/add_body - POST:
Ingresa un nuevo elemento a la estrutura de datos

```
{
    "bodyId":950,
    "englishName":"The Earth",
    "isPlanet":true,
    "gravity":"9.8",
    "discoveredBy":"",
    "discoveryDate":"",
    "density":"1.32620",
    "bodyType":"planet"
}
```
## Autores

- Alvaro Miguel Gonzalez Hic - 9490224805 - 100%
- Walter Daniel Palacios De León - 9490212140 - 100%

