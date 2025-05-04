def calcular_tickets(num_miembros, num_eras, nombre_grupo):
    cartas_1d = num_miembros
    cartas_2d3d = num_miembros * 2
    total_cartas_pool = num_eras * num_miembros * 3

    prob_1d_por_carta = cartas_1d / total_cartas_pool
    esperanza_1d_por_pack = 5 * prob_1d_por_carta
    num_packs_ultimate = cartas_1d / esperanza_1d_por_pack
    total_tickets_ultimate = round(num_packs_ultimate * 205)

    prob_2d3d_por_carta = 2 / (num_eras * 3)
    esperanza_2d3d_por_pack = 5 * prob_2d3d_por_carta
    num_packs_legendary = cartas_2d3d / esperanza_2d3d_por_pack
    total_tickets_legendary = round(num_packs_legendary * 299)

    return {
        "grupo": nombre_grupo,
        "ultimate": total_tickets_ultimate,
        "legendary": total_tickets_legendary,
        "total": total_tickets_ultimate + total_tickets_legendary
    }

def mostrar_tabla(resultados):
    print("\nResumen de Tickets Necesarios:\n")
    print(f"{'Grupo':<10}{'Ultimate 🎟️':>15}{'Legendary 🎟️':>18}{'Total 🎟️':>15}")
    print("-" * 60)
    total_global_ultimate = 0
    total_global_legendary = 0

    for r in resultados:
        print(f"{r['grupo']:<10}{r['ultimate']:>15,}{r['legendary']:>18,}{r['total']:>15,}")
        total_global_ultimate += r['ultimate']
        total_global_legendary += r['legendary']

    total = total_global_ultimate + total_global_legendary
    print("-" * 60)
    print(f"{'TOTAL':<10}{total_global_ultimate:>15,}{total_global_legendary:>18,}{total:>15,}")
    return total

def estimar_tiempo(tickets_necesarios):
    print("\n🕒 Estimador de Tiempo para Alcanzar los Tickets 🎟️")
    tipo = input("¿Eres usuario 'normal' o 'kofi'? ").strip().lower()
    while tipo not in ["normal", "kofi"]:
        tipo = input("❌ Por favor, escribe 'normal' o 'kofi': ").strip().lower()

    try:
        dailies_por_dia = int(input("¿Cuántas veces haces daily al día? (1 o 2): "))
        if dailies_por_dia not in [1, 2]:
            raise ValueError
    except ValueError:
        print("❌ Valor inválido. Usando 2 por defecto.")
        dailies_por_dia = 2

    # Promedio base por daily
    promedio_base = 13
    bonus_kofi = 8 if tipo == "kofi" else 0
    promedio_daily = promedio_base + bonus_kofi
    tickets_dia = promedio_daily * dailies_por_dia

    dias_necesarios = tickets_necesarios / tickets_dia
    semanas = dias_necesarios // 7
    dias = dias_necesarios % 7

    print(f"\n🎯 Necesitas un promedio de {tickets_dia:.1f} tickets por día.")
    print(f"📆 Te tomaría aproximadamente {int(dias_necesarios)} días ({int(semanas)} semanas y {int(dias)} días) para alcanzar {tickets_necesarios:,} tickets.\n")

def main():
    resultados = []
    print("🔮 Calculadora de Tickets para Packs (Ultimate + Legendary) 🔮\n")
    while True:
        nombre = input("Nombre del grupo (o 'fin' para terminar): ").strip()
        if nombre.lower() == "fin":
            break
        try:
            miembros = int(input(f"→ ¿Cuántos miembros tiene {nombre}? "))
            eras = int(input(f"→ ¿Cuántas eras tiene {nombre} (incluyendo la nueva)? "))
            resultados.append(calcular_tickets(miembros, eras, nombre))
        except ValueError:
            print("❌ Entrada no válida. Intenta de nuevo.\n")

    if resultados:
        total = mostrar_tabla(resultados)
        opcion = input("\n¿Deseas calcular el tiempo estimado para juntar los tickets? (s/n): ").strip().lower()
        if opcion == "s":
            estimar_tiempo(total)
    else:
        print("No se ingresaron grupos.")

if __name__ == "__main__":
    main()
