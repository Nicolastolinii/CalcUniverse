import math

def calcular_fuerzas(fuerzas):
    """
    Calcula la fuerza resultante y la fuerza equilibrante de un sistema de fuerzas concurrentes.

    Parámetros:
    fuerzas (list): Lista de tuplas donde cada tupla contiene:
        - float: módulo de la fuerza (en unidades de fuerza, por ejemplo, Newtons).
        - float: ángulo en grados (medido en sentido antihorario desde el eje positivo x).
        
    Ejemplo:
    >>> fuerzas = [
    ...     (25, 41),   # Fuerza 1: 25 Newtons, 41 grados
    ...     (35, 130),  # Fuerza 2: 35 Newtons, 130 grados
    ...     (45, 335)   # Fuerza 3: 45 Newtons, 335 grados
    ... ]
    Retorna:
    dict: Diccionario con la magnitud y dirección de la fuerza resultante y equilibrante, en el siguiente formato:
        {
            'resultante': {
                'magnitud': float,  # Magnitud de la fuerza resultante.
                'direccion': float  # Dirección de la fuerza resultante (en grados).
            },
            'equilibrante': {
                'magnitud': float,  # Magnitud de la fuerza equilibrante.
                'direccion': float  # Dirección de la fuerza equilibrante (en grados).
            }
        }
    """
    def calcular_resultante(fuerzas):
        """
        Calcula la fuerza resultante de un sistema de fuerzas concurrentes.

        Parámetros:
        fuerzas (list): Lista de tuplas donde cada tupla contiene el módulo de la fuerza y el ángulo en grados.

        Retorna:
        tuple: Componente x y componente y de la fuerza resultante.
        """
        Rx = 0  # Componente x de la resultante
        Ry = 0  # Componente y de la resultante
        
        for F, angulo in fuerzas:
            # Convertir ángulo de grados a radianes
            radianes = math.radians(angulo)
            # Calcular componentes
            Rx += F * math.cos(radianes)
            Ry += F * math.sin(radianes)
        
        return Rx, Ry

    def calcular_magnitud_y_direccion(Rx, Ry):
        """
        Calcula la magnitud y la dirección de la fuerza resultante.

        Parámetros:
        Rx (float): Componente x de la fuerza resultante.
        Ry (float): Componente y de la fuerza resultante.

        Retorna:
        tuple: Magnitud y dirección (ángulo en grados) de la fuerza resultante.
        """
        magnitud = math.sqrt(Rx**2 + Ry**2)  # Magnitud de la fuerza resultante
        direccion = math.degrees(math.atan2(Ry, Rx))  # Dirección en grados
        return magnitud, direccion

    def calcular_equilibrante(R):
        """
        Calcula la fuerza equilibrante.

        Parámetros:
        R (tuple): Componente x y componente y de la fuerza resultante.

        Retorna:
        tuple: Magnitud y dirección de la fuerza equilibrante.
        """
        Rx, Ry = R
        # La equilibrante es igual en magnitud pero opuesta en dirección
        magnitud = math.sqrt(Rx**2 + Ry**2)
        direccion = (math.degrees(math.atan2(Ry, Rx)) + 180) % 360  # Ángulo opuesto
        return magnitud, direccion

    # Cálculo de la resultante
    Rx, Ry = calcular_resultante(fuerzas)
    R = (Rx, Ry)

    # Cálculo de la magnitud y dirección de la resultante
    magnitud_R, direccion_R = calcular_magnitud_y_direccion(Rx, Ry)

    # Cálculo de la equilibrante
    magnitud_E, direccion_E = calcular_equilibrante(R)
    result = {
        'resultante': {
            'magnitud': magnitud_R,
            'direccion': direccion_R
        },
        'equilibrante': {
            'magnitud': magnitud_E,
            'direccion': direccion_E
        }
    }
    return result

