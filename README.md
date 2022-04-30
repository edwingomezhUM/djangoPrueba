# prueba

Para ejecutar el código se debe ejecutar python manage.py runserver para que quede local

# 1. Un punto final para proporcionar una búsqueda dentro de las pistas (al menos por nombre, pero es abierto a cualquier sugerencia)

Se crea un punto final para búsqueda por nombre mediante método GET, llamado getTracksName

Debe ser invocado de la siguiente manera, (al final agregar el nombre del artista a búscar
'''
http://localhost:8000/api/getTracksName/?name=NAMESEARCH
'''

- Y le resultado es en formato json.
---

---


# 2. Un punto final que permitiría obtener las 50 mejores pistas de popularidad.

Como no existe un variable para saber el ranking  de popularidad de las pistas, se desarrollo un endpoint que ordenara en orden ascendente lo artistas por su identificado y el resultado fuera el identificador y el nombre del artista. Se desarrollo el servicio getTopTracks

Debe ser invocado de la siguiente manera, 
'''
http://localhost:8000/api/getTopTracks/
'''

- Y le resultado es en formato json.
---

---


# 3. Un punto final para eliminar una pista, usando un identificador dado (definido por usted)

Se desarrollo punto final para eliminar un track a partir de un identificador, y este es enviados mediante método GET

Se crea el endpoint delTracks

Debe ser invocado de la siguiente manera, 
'''
http://localhost:8000/api/delTracks/?id=1611056166
'''

- Y le resultado es en formato json.
---

---

# 4. Un punto final para agregar nuevas pistas usando ORM.

Se desarrollo un endpoint para agregar nuevas pistas mediante ORM django, los parametros se envian mediante método GET.

Se crea el endpoint insertTracks

Debe ser invocado de la siguiente manera, 

NOTA: se pueden enviar todo los parámetros, o solo se pueden enviar algunos
'''
http://localhost:8000/api/insertTracks/?id=1&artistName=edu&name=edwin&artistId=1
'''

- Y le resultado es en formato json.
---

---


