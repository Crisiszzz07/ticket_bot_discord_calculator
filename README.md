# 🧮 K-pop Card Pack Ticket Calculator 🎟️✨

Una herramienta en Python para calcular cuántos 🎟️ **tickets** necesitas para conseguir todas las cartas de tus grupos favoritos en un bot estilo gacha de K-pop (como los que usan packs "Ultimate" y "Legendary"). Enfocado en los números de Garam.

---

## 📌 ¿Qué hace este script?

Este script te ayuda a:

* Calcular cuántos tickets necesitas para conseguir **todas las cartas** de una nueva era (según miembros y rarezas).
* Combina de forma **estratégica** los packs `Ultimate` y `Legendary` para minimizar el gasto.
* Estimar **cuántos días/semanas** tardarías en conseguir esos tickets, dependiendo de si eres usuario **normal** o **Ko-fi**.

---

### ⚙️ Lógica de funcionamiento

Supongamos que una nueva era sale para un grupo de K-pop con varias rarezas de cartas. Este script:

1. **Cuenta cuántas cartas necesitas:**

   * Cada miembro tiene 3 cartas por era (1D, 2D, 3D).
   * Se calcula el total de cartas necesarias de la nueva era.

2. **Calcula los tickets necesarios:**

   * Usa **packs Ultimate** para conseguir las 1D (porque Legendary no las incluye).
   * Usa **packs Legendary** para las 2D y 3D, ya que permiten elegir el idol y el grupo.

3. **Simula probabilidades**: se calcula la esperanza matemática de obtener una carta específica con cada tipo de pack, basándose en el tamaño del pool.

4. **Calcula el total de tickets necesarios** multiplicando los packs necesarios por el precio de cada uno:

   * Ultimate: `205 🎟️`
   * Legendary: `299 🎟️`

5. **(Opcional)** Estima el tiempo que te tomaría conseguir los tickets haciendo `daily` una o dos veces al día, con bonificación si eres Ko-fi supporter.

---

### 💻 Cómo usarlo

#### ✅ Requisitos

* Python 3.7+
* (Opcional) Recomendado usarlo en consola o terminal

#### 🚀 Instrucciones

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/kpop-ticket-calculator.git
cd kpop-ticket-calculator
```

2. Ejecuta el script:

```bash
python3 ticket_calculator.py
```

3. Introduce los datos:

   * Nombre del grupo
   * Cuántos miembros tiene
   * Cuántas eras tiene (¡incluye la nueva!)
   * Puedes añadir varios grupos.
   * Cuando termines, escribe `fin`.

4. El script te mostrará:

   * Cuántos tickets necesitas por grupo y en total.
   * (Opcional) Cuánto tiempo te tomaría reunir los tickets haciendo `daily`.

---

### 📊 Ejemplo de uso

```plaintext
Nombre del grupo (o 'fin' para terminar): aespa
→ ¿Cuántos miembros tiene aespa? 4
→ ¿Cuántas eras tiene aespa (incluyendo la nueva)? 12
Nombre del grupo (o 'fin' para terminar): xg
→ ¿Cuántos miembros tiene xg? 7
→ ¿Cuántas eras tiene xg (incluyendo la nueva)? 8
Nombre del grupo (o 'fin' para terminar): fin

Resumen de Tickets Necesarios:
Grupo        Ultimate 🎟️      Legendary 🎟️        Total 🎟️
------------------------------------------------------------
aespa           1,025               4,596             5,621
xg              1,323               5,848             7,171
------------------------------------------------------------
TOTAL           2,348              10,444            12,792

¿Deseas calcular el tiempo estimado para juntar los tickets? (s/n): s
¿Eres usuario 'normal' o 'kofi'? kofi
¿Cuántas veces haces daily al día? (1 o 2): 2

🎯 Necesitas un promedio de 42.0 tickets por día.
📆 Te tomaría aproximadamente 305 días (43 semanas y 4 días) para alcanzar 12,792 tickets.
```

---

### 👥 Tipos de usuario

| Tipo   | Tickets por daily | Dailies por día | Tickets diarios aprox |
| ------ | ----------------- | --------------- | --------------------- |
| Normal | 10–16 (prom. 13)  | 1 o 2           | 13 o 26               |
| Ko-fi  | 13 + 8 = 21       | 1 o 2           | 21 o 42               |

---

### 🧠 ¿Por qué usar este script?

* Te ahorra tiempo haciendo cálculos a mano.
* Optimiza el uso de packs para gastar menos tickets.
* Te ayuda a **planificar** tus recursos y tus pulls para eventos importantes.

---

### 📄 Licencia

MIT License. Puedes modificar y compartir este script libremente.
¡Créditos si lo usas en proyectos públicos son siempre bienvenidos! 💖
