# Experta

Utilizando la libreria de experta para crear un sistema experto

## Empezando

Un sistema de audio respuesta tiene un CSV que contiene cantidades de las siguientes variables: llam (frecuencia llamadas), vol (frecuencia de planta telefonica), tran (frecuencia de transacciones)

Se pretende contruir un experto que permita identificar cuando estas variables estan por encima del umbral basandose en el campo param para mapear el parametro, el tipo de alerta y el intervalo afectado.

### Prerrequisitos

Solo necesita:

```
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
```
## Autores
* **Leonardo Patiño rodriguez** - *Trabajo inicial*


