# proyecto-conoce-tus-habitos
Programa interactivo para conocer y reflexionar sobre los hábitos cotidianos relacionados con el bienestar.

## Contexto

Los hábitos que una persona desarrolla en su vida cotidiana pueden influir en su bienestar. Entre ellos se encuentran aspectos como la alimentación, el descanso, la actividad física y las actividades que realiza durante su tiempo libre.

La Organización Mundial de la Salud señala que una alimentación saludable debe basarse en principios como la adecuación, el equilibrio, la moderación y la diversidad. También indica que la actividad física proporciona beneficios para la salud física y mental y que cualquier cantidad de actividad es mejor que ninguna.

A partir de esta idea, el proyecto propone desarrollar un programa interactivo en Python 3 que permita al usuario responder una serie de preguntas relacionadas con sus hábitos cotidianos. El programa analizará sus respuestas y generará un perfil general de sus hábitos, mostrando fortalezas y posibles áreas de mejora.

Importante: el programa no pretende realizar un diagnóstico médico, sino funcionar como una herramienta educativa de reflexión sobre los hábitos cotidianos.

## ¿Por qué es interesante?

Elegí este tema porque me interesa conocer mejor a las personas y la manera en que sus hábitos forman parte de su vida cotidiana. Me parece interesante que, aunque dos personas tengan rutinas completamente diferentes, ambas puedan tener hábitos que contribuyan a su bienestar.

Además, considero interesante convertir esta curiosidad en un programa interactivo, porque no solamente se trata de obtener un resultado, sino de permitir que cada usuario conozca un poco más sobre sus propias costumbres a partir de las respuestas que proporciona.

El proyecto también me parece interesante desde el punto de vista de la programación, porque las respuestas del usuario pueden producir diferentes resultados. Esto permite utilizar condiciones, variables, funciones y posteriormente organizar el programa en diferentes módulos.

## Objetivo

Desarrollar un programa interactivo en Python 3 que permita al usuario responder preguntas sobre sus hábitos cotidianos y obtener un perfil general basado en sus respuestas.

## Algoritmo

1. Iniciar el programa.

2. Mostrar al usuario una breve explicación del propósito del cuestionario.

3. Solicitar algunos datos generales del usuario.

4. Realizar preguntas relacionadas con sus hábitos de sueño.

5. Realizar preguntas relacionadas con su alimentación.

6. Realizar preguntas relacionadas con su actividad física.

7. Preguntar sobre las actividades que disfruta realizar durante su tiempo libre.

8. Registrar las respuestas proporcionadas por el usuario.

9. Analizar las respuestas utilizando diferentes condiciones.

10. Identificar los aspectos de los hábitos del usuario que presentan mayores fortalezas.

11. Identificar posibles áreas de mejora.

12. Generar un perfil general de hábitos a partir de las respuestas obtenidas.

13. Mostrar el resultado al usuario junto con recomendaciones generales relacionadas con hábitos saludables.

14. Preguntar si desea realizar nuevamente el cuestionario.

15. Si responde que sí, volver al cuestionario.

16. Si responde que no, finalizar el programa.

## Programa

Python 3.

## Fuentes

Organización Mundial de la Salud (OMS)
Alimentación saludable.
https://www.who.int/es/news-room/fact-sheets/detail/healthy-diet

Organización Mundial de la Salud (OMS)
Actividad física.
https://www.who.int/es/news-room/fact-sheets/detail/physical-activity

## Avance 2: Operaciones con operadores 

En este avance se incorporan operaciones con operadores al proyecto "Conoce tus hábitos". Las operaciones permiten trabajar con los datos proporcionados por el usuario y obtener resultados relacionados con sus hábitos cotidianos.

### Operaciones incorporadas 

Para analizar los datos de los hábitos se incorporan operaciones de suma, resta, multiplicación y división.

Sueño - resta
**Sueño:** se utiliza la resta para calcular la diferencia entre las horas registradas y una referencia de 8 horas.
`diferencia_sueno = 8 - horas_sueno`

2. Actividad Física -resta 
**Actividad física:** se utiliza la resta para calcular la diferencia entre los minutos registrados y una referencia de 60 minutos.

`diferencia_actividad = 60 minutos_actividad`


3. Hidratación - multiplicación
**Hidratación:** se utiliza la multiplicación para calcular la cantidad aproximada de vasos de agua registrados durante una semana.

`vasos_semana = vasos_agua * 7`

4. Tiempo libre - multiplicación
**Tiempo libre:** se utiliza la multiplicación para calcular las horas aproximadas de tiempo libre durante una semana.

`horas_libre_semana = horas_libre * 7'

5. Pantallas - multiplicación
**Tiempo frente a pantallas:** se utiliza la multiplicación para calcular la cantidad aproximada de horas registradas frente a pantallas durante una semana.
`horas_pantallas_semana = horas_pantalla * 7`

## Avance 3: Uso de Funciones
En este avance se incorporan funciones al proyecto "Conoce tus hábitos". Las funciones permiten organizar las operaciones del programa en bloques de código reutilizables, haciendo que el programa sea más ordenado y fácil de comprender.

### Funciones incorporadas

Las funciones se utilizan para realizar los cálculos relacionados con los hábitos registrados por el usuario.

Cada función recibe los datos necesarios, realiza una operación y devuelve un resultado.

1. **Sueño:** calcula la diferencia entre las horas de sueño registradas y una referencia de 8 horas.

2. **Actividad física:** calcula la diferencia respecto a una referencia de 60 minutos y convierte los minutos de actividad física a horas. También calcula las horas de actividad física registradas durante una semana.

3. **Hidratación/Agua:** calcula la cantidad aproximada de vasos de agua registrados durante una semana.

4. **Tiempo libre:** calcula las horas aproximadas de tiempo libre registradas durante una semana.

5. **Pantallas:** calcula las horas aproximadas frente a pantallas registradas durante una semana.

Las funciones permiten separar los cálculos del resto del programa y reutilizar los resultados obtenidos a partir de los datos ingresados por el usuario.

## Avance 4: Estructuras de decisión

En este avance se incorporan estructuras de decisión al proyecto
"Conoce tus hábitos". Estas estructuras permiten que el programa
tome diferentes caminos dependiendo de los datos ingresados por
el usuario.

### Decisiones incorporadas

- **Sueño:** utiliza `if`, `elif` y `else` para comparar las horas
  registradas con una referencia de 8 horas.

- **Actividad física:** utiliza `if` y `else` para comparar los
  minutos registrados con una referencia de 60 minutos.

- **Agua:** utiliza `if` y `else` para comparar el registro con una
  referencia de 6 vasos.

- **Tiempo libre:** utiliza `if` y `else` para comparar el registro
  con una referencia de 2 horas.

- **Tiempo de pantalla:** utiliza `if` y `else` para identificar si
  el registro supera una referencia de 4 horas.

- **Decisión combinada:** utiliza el operador lógico `and` para
  comprobar dos condiciones al mismo tiempo.

Estas decisiones permiten que el programa muestre diferentes
mensajes dependiendo de las respuestas del usuario. Las cantidades
utilizadas como referencias forman parte de la lógica del programa
y no representan un diagnóstico médico.

## Avance 5: Estructuras de repetición

En este avance se incorpora una estructura de repetición al proyecto
"Conoce tus hábitos". Se utiliza el ciclo `while` para validar los
datos ingresados por el usuario.

El ciclo verifica si alguno de los datos registrados tiene un valor
negativo. Si encuentra un dato no válido, muestra un mensaje y vuelve
a solicitar el dato correspondiente. El ciclo continúa hasta que los
datos cumplen con la condición establecida.

De esta manera, el ciclo `while` permite que el programa repita una
acción mientras exista un dato que deba corregirse.


