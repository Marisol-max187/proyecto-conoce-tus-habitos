"""Conoce tus hábitos

Programa interactivo que registra datos sobre hábitos cotidianos
y realiza cálculos relacionados con el sueño, actividad física,
hidratación, tiempo libre y uso de pantallas.
"""

print("CONOCE TUS HÁBITOS")
print()

def calcular_sueno(horas_sueno):
    """Calcula la diferencia de horas de sueño respecto a 8 horas"""
    diferencia_sueno = 8 - horas_sueno
    return diferencia_sueno

def calcular_actividad(minutos_actividad):
    """Calcula diferencias y convierte la actividad a horas semanales."""
    diferencia_actividad = 60 - minutos_actividad
    horas_actividad = minutos_actividad / 60
    horas_actividad_semana = horas_actividad * 7
    return (
        diferencia_actividad,
            horas_actividad,
            horas_actividad_semana
        )

def calcular_agua(vasos_agua):
    """Calcula los vasos de agua registrados durante una semana."""
    vasos_semana = vasos_agua * 7
    return vasos_semana

def calcular_tiempo_libre(horas_libre):
    """Calcula las horas de tiempo libre registradas durante una semana."""
    horas_libre_semana = horas_libre * 7
    return horas_libre_semana

def calcular_pantalla(horas_pantalla):
    """calcula las horas de pantalla registradas durante una semana."""
    horas_pantalla_semana = horas_pantalla * 7
    return horas_pantalla_semana

# Entrada de datos

horas_sueno = float(input(
    "¿Cuántas horas duermes normalmente por noche? "))

minutos_actividad = float(input(
    "¿Cuántos minutos de actividad física realizas aproximadamente al día? "))

vasos_agua = float(input(
    "¿Cuántos vasos de agua tomas aproximadamente al día? "))

horas_libre = float(input(
    "¿Cuántas horas dedicas aproximadamente a tu tiempo libre al día? "))

horas_pantalla = float(input(
    "¿Cuántas horas pasas aproximadamente frente a una pantalla "
    "fuera de tus actividades escolares? "))

# Validación de datos con un ciclo
while (
    horas_sueno < 0
    or minutos_actividad < 0
    or vasos_agua < 0
    or horas_libre < 0
    or horas_pantalla < 0
):
    print("Los datos no pueden ser negativos.")
    
    if horas_sueno < 0:
        horas_sueno = float(input(
            "Ingresa nuevamente las horas de sueño: "))

    if minutos_actividad < 0:
        minutos_actividad = float(input(
            "Ingresa nuevamente los minutos de actividad física: "))

    if vasos_agua < 0:
        vasos_agua = float(input(
            "Ingresa nuevamente los vasos de agua: "))

    if horas_libre < 0:
        horas_libre = float(input(
            "Ingresa nuevamente las horas de tiempo libre: "))

    if horas_pantalla < 0:
        horas_pantalla = float(input(
            "Ingresa nuevamente las horas de pantalla: "))

# Calculos

diferencia_sueno = calcular_sueno(horas_sueno)
    

(   
diferencia_actividad,
horas_actividad,
horas_actividad_semana,
) = calcular_actividad(minutos_actividad)




vasos_semana = calcular_agua(vasos_agua)



horas_libre_semana = calcular_tiempo_libre(horas_libre)



horas_pantalla_semana = calcular_pantalla(horas_pantalla)


horas_actividad_y_libre = horas_actividad_semana + horas_libre_semana

# Decisión sobre el sueño
if horas_sueno < 8:
    print("Registraste menos de 8 horas de sueño.")
elif horas_sueno == 8:
    print("Registraste 8 horas de sueño.")
else:
    print("Registraste mas de 8 horas de sueño.")
    
# Decisión sobre la actividad física
if minutos_actividad >= 60:
    print("Registraste al menos 60 minutos de actividad física.")
else:
    print("Registraste menos de 60 minutos de actividad física.")
    
# Decisión sobre el registro de agua
if vasos_agua >= 6:
    print("Registraste 6 vasos de agua o más.")
else:
    print("Registraste menos de 6 vasos de agua.")
    
# Decisión sobre el tiempo libre
if horas_libre >= 2:
    print("Registraste 2 horas o más de tiempo libre al día.")
else:
    print("Registraste menos de 2 horas de tiempo libre al día.")

# Decisión sobre el tiempo de pantalla
if horas_pantalla > 4:
    print("Registraste más de 4 horas de pantalla al día.")
else:
    print("Registraste 4 horas o menos de pantalla al día.")
        
    
# Decisión combinada
if horas_sueno >= 8 and minutos_actividad >= 60:
    print("Tus registros cumplen las dos referencias.")
else:
    print("Uno o ambos registros están por debajo de la referencia.")
    

# Resultados

print()
print("RESULTADOS")
print("Diferencia de sueño:", diferencia_sueno, "horas")
print(
    "Diferencia de actividad física:",
    diferencia_actividad, "minutos"
    )
print("Horas de actividad física por día:", horas_actividad)
print("Horas de actividad física por semana:", horas_actividad_semana)
print("Vasos de agua registrados en una semana:", vasos_semana)
print("Horas de tiempo libre por semana:", horas_libre_semana)
print("Horas de pantalla por semana:", horas_pantalla_semana)
print(
    "Horas de actividad física y tiempo libre por semana:",
    horas_actividad_y_libre
    )

