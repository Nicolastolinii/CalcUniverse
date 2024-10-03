from caida import caida
from calcular_fuerzas import calcular_fuerzas

def main():
    while True:
        print("\nSeleccione la opción que desea realizar:")
        print("1. Calcular la caída libre de un objeto")
        print("2. Calcular fuerzas concurrentes")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            # Obtener parámetros para la caída
            
            v0 = float(input("\nIngrese la velocidad inicial (m/s): "))
            g = float(input("Ingrese la aceleración debida a la gravedad (m/s^2): "))
            t = float(input("Ingrese el tiempo de caída (s): "))

            # Calcular resultado de la caída
            resultado = caida(v0, g, t)
            print(f"Velocidad final después de {t} segundos: {resultado['velocidad_final']:.2f} m/s")
            print(f"Desplazamiento después de {t} segundos: {resultado['desplazamiento']:.2f} m")

        elif opcion == '2':
            # Obtener parámetros para calcular fuerzas
            num_fuerzas = int(input("\nIngrese el número de fuerzas: "))
            fuerzas = []

            for i in range(num_fuerzas):
                F = float(input(f"Ingrese el módulo de la fuerza {i + 1} (N): "))
                angulo = float(input(f"Ingrese el ángulo de la fuerza {i + 1} (grados): "))
                fuerzas.append((F, angulo))

            # Calcular resultados de fuerzas
            resultados_fuerzas = calcular_fuerzas(fuerzas)
            print(f"Fuerza resultante: Magnitud = {resultados_fuerzas['resultante']['magnitud']:.2f} N, Dirección = {resultados_fuerzas['resultante']['direccion']:.2f} grados")
            print(f"Fuerza equilibrante: Magnitud = {resultados_fuerzas['equilibrante']['magnitud']:.2f} N, Dirección = {resultados_fuerzas['equilibrante']['direccion']:.2f} grados")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()