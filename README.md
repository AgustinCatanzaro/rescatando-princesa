# rescatando-princesa

---

## DESCRIPCION DEL PROBLEMA

Hace mucho tiempo existía un bosque
con claros conectados por senderos. Un
príncipe está en uno de esos claros y tiene
que salvar a una princesa que está en otro
claro. En algunos claros hay dragones, que
intentarán interceptar al príncipe en su
camino a la princesa (los dragones atacan
al príncipe sólo en un claro).

---

SE PIDE

---

determinar un camino desde el príncipe
hasta la princesa que sea seguro para el
príncipe, es decir que asegure que el
príncipe no se cruzará con un dragón en
un claro. De todos los caminos seguros, es
mejor si determinas el camino mas corto
(o uno de los caminos mas cortos, si
hubiera varios).

---

DATOS DE ENTRADA

---

Primero una línea con:

la cantidad de claros c (2 ≤ c ≤ 100 000),

la cantidad s de senderos (0 ≤ s ≤ 600 000)

la cantidad d de dragones (0 ≤ d ≤ 100)

Luego una línea indicando los claros:

cf donde está la princesa y

cm donde está el príncipe. (1 ≤ cm, cf ≤ c)

Luego una línea con d números, correspondientes
a los claros donde están los dragones:

Luego s líneas con los senderos definidos con
3 números:

El claro inicial ci (1 ≤ ci ≤ c)

El claro final cf (1 ≤ cf ≤ c)

El largo l del sendero (0 < l ≤ 1000)

---

DATOS DE SALIDA

---

La hilera “NO HAY CAMINO” si no hay camino
que conecte el claro del príncipe con el claro de
la princesa

La hilera “INTERCEPTADO” si no existe camino
que evite que el príncipe sea interceptado por un
dragón

El camino que asegura que el príncipe llegue a
la princesa. El camino se debe describir
indicando la lista de claros desde el claro inicial
(donde esta el príncipe) hasta el claro final
(donde está la princesa)

---

EJEMPLO

---

Si la entrada fuera:

9 10 2<br />
9 1<br />
8 5<br />
1 2 3<br />
1 3 2<br />
2 3 4<br />
2 6 1<br />
3 8 1<br />
8 6 5<br />
4 5 2<br />
3 4 2<br />
3 6 2<br />
6 9 3<br />

La salida es:

1 2 6 9

u otra posibilidad es:

1 2 3 6 9
