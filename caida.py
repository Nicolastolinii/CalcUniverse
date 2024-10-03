def caida(v0, g, t):
    def calcular_velocidad(v0, g, t):
        """
        Calcula la velocidad final de un objeto en caída libre.

        Parámetros:
        v0 (float): Velocidad inicial en m/s.
        g (float): Aceleración debido a la gravedad en m/s^2.
        t (float): Tiempo en segundos.

        Retorna:
        float: Velocidad final en m/s.
        """
        return v0 + g * t

    def calcular_desplazamiento(v0, g, t):
        """
        Calcula el desplazamiento de un objeto en caída libre.

        Parámetros:
        v0 (float): Velocidad inicial en m/s.
        g (float): Aceleración debido a la gravedad en m/s^2.
        t (float): Tiempo en segundos.

        Retorna:
        float: Desplazamiento en metros.
        """
        return v0 * t + 0.5 * g * t**2

    # Cálculos
    velocidad_final = calcular_velocidad(v0, g, t)
    desplazamiento = calcular_desplazamiento(v0, g, t)
    result = {
        'velocidad_final': velocidad_final,
        'desplazamiento': desplazamiento
    }
    return result
    
# Ejemplo:

# v0 = 12  # Velocidad inicial en m/s
# g = 10   # Aceleración debido a la gravedad en m/s^2
# t = 7 # Tiempo en segundos
# resultado = caida(v0,g,t)
# print(f"Velocidad final después de {t} segundos: {resultado['velocidad_final']:.2f} m/s")
# print(f"Desplazamiento después de {t} segundos: {resultado['desplazamiento']:.2f} m")

