# Definir eventos
eventos = ["el clima es agradable", "el cielo está nublado", "la temperatura es alta"]

# Definir objetos mentales
creencias = [{"el clima es agradable": 0.8}]

# Función para actualizar creencias
def actualizar_creencias(evento, creencias):
    # Buscar la creencia correspondiente al evento y actualizar su probabilidad
    for creencia in creencias:
        if evento in creencia:
            creencia[evento] = 0.5
            return
    # Si no se encontró una creencia correspondiente, agregar una nueva
    creencias.append({evento: 0.6})

# Simular eventos
actualizar_creencias("el cielo está nublado", creencias)
actualizar_creencias("la temperatura es alta", creencias)

# Imprimir creencias actualizadas
print(creencias)
