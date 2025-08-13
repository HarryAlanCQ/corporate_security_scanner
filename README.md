# Corporate Security Scanner 🛡️

Herramienta en **Python** para el escaneo de puertos TCP en entornos corporativos, con generación de **logs**, exportación a **CSV** y sistema de **alertas**.

---

## 📌 Características
- Escaneo de puertos TCP con `socket`
- Registro de actividad en archivo `log.txt`
- Exportación de resultados a formato **CSV** compatible con Excel
- Sistema de alertas (simulado)
- Código modular con **herencia múltiple** y **Mixins**
- Rutas organizadas en carpetas `logs/` y `reports/`

---

## 📂 Estructura del proyecto

corporate-security-scanner/
│── scanner.py # Código principal
│── README.md # Documentación
│── logs/ # Carpeta para logs
│ └── log.txt
│── reports/ # Carpeta para reportes CSV
│ └── reporte.csv

---

## ⚙️ Requisitos
- Python 3.8 o superior
- No requiere librerías externas

---

## 🚀 Uso
1. **Clonar el repositorio**

   git clone https://github.com/HarryAlanCQ/corporate-security-scanner.git
   cd corporate-security-scanner

2. **Ejecutar el script**

    python scanner.py

3. **Archivos generados**

    logs/log.txt -> Registro de escaneo
    reports/reporte.csv -> Resultado del escaneo en formato CSV

EJEMPLO DE SALIDA DE CÓDIGO:

[ALERTA] Escaneo finalizado para scanme.nmap.org
Escaneo finalizado.

EJEMPLO DE REPORTE CSV

Puerto,Estado,Fecha y hora
21,cerrado,13-08-2025 12:30:45
22,abierto,13-08-2025 12:30:45
80,abierto,13-08-2025 12:30:45
443,abierto,13-08-2025 12:30:45

🛠️ Personalización

Añadir Mixins: Puedes crear nuevas clases para enviar correos, guardar en base de datos o generar reportes en otros formatos sin modificar el núcleo del escáner.

Modificar puertos: Cambia la lista puertos en el script para adaptarlo a tus necesidades.

📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

