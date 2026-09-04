print("CONOCE TUS HÁBITOS")
print()

horas_sueno = float(input("¿Cuántas horas duermes normalmente por noche? "))

minutos_actividad = float(input(
    "¿Cuántos minutos de actividad física realizas aproximadamente al día? "))

vasos_agua = float(input(
    "¿Cuántos vasos de agua tomas aproximadamente al día? "))

horas_libre = float(input(
    "¿Cuántas horas dedicas aproximadamente a tu tiempo libre al día? "))

horas_pantalla = float(input(
    "¿Cuántas horas pasas aproximadamente frente a una pantalla "
    "fuera de tus actividades escolares? "))

diferencia_sueno = 8 - horas_sueno
diferencia_actividad = 60 - minutos_actividad

horas_actividad = minutos_actividad / 60
horas_actividad_semana = horas_actividad * 7

vasos_semana = vasos_agua * 7
horas_libre_semana = horas_libre * 7
horas_pantalla_semana = horas_pantalla * 7

horas_actividad_y_libre = horas_actividad_semana + horas_libre_semana

print()
print("RESULTADOS")
print("Diferencia de sueño:", diferencia_sueno, "horas")
print("Diferencia de actividad física:", diferencia_actividad, "minutos")
print("Horas de actividad física por día:", horas_actividad)
print("Horas de actividad física por semana:", horas_actividad_semana)
print("Vasos de agua registrados en una semana:", vasos_semana)
print("Horas de tiempo libre por semana:", horas_libre_semana)
print("Horas de pantalla por semana:", horas_pantalla_semana)
print(
    "Horas de actividad física y tiempo libre por semana:",
    horas_actividad_y_libre)
