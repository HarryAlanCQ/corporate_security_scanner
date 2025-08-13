import socket
from datetime import datetime
import os

# ==============================
#   Clases base y mixins
# ==============================

class EscanerBase:
    """Clase base para escaneo de puertos TCP."""
    def escanear(self, objetivo, puertos):
        resultados = []
        for puerto in puertos:
            conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexion.settimeout(0.5)
            try:
                conexion.connect((objetivo, puerto))
                resultados.append((puerto, "abierto"))
            except socket.error:
                resultados.append((puerto, 'cerrado'))
            conexion.close()
        return resultados


class LogMixin:
    """Mixin para guardar registros de actividad."""
    def guardar_log(self, archivo_log, mensaje):
        with open(archivo_log, 'a') as f:
            f.write(mensaje + '\n')


class ExportacionCSVMixin:
    """Mixin para exportar resultados a CSV."""
    def exportar_csv(self, archivo_csv, datos, fechayhora):
        with open(archivo_csv, 'w') as f:
            f.write('Puerto,Estado,Fecha y hora\n')
            for dato in datos:
                f.write(','.join(map(str, dato)) + f',{fechayhora}\n')


class AlertasEmailMixin:
    """Mixin para enviar alertas (simulación)."""
    def alerta(self, objetivo):
        print(f"[ALERTA] Escaneo finalizado para {objetivo}")


class EscanerCorporativo(EscanerBase, LogMixin, ExportacionCSVMixin, AlertasEmailMixin):
    """Escáner corporativo que combina escaneo, log, exportación y alertas."""
    pass


# ==============================
#   Ejecución del script
# ==============================

if __name__ == "__main__":
    # Configuración de rutas
    os.makedirs("logs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    log_path = os.path.join("logs", "log.txt")
    csv_path = os.path.join("reports", "reporte.csv")

    # Parámetros de escaneo
    objetivo = "scanme.nmap.org"
    fecha_actual = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    puertos = [21, 22, 80, 443]

    # Crear instancia
    escaner_corporativo = EscanerCorporativo()

    # Escaneo
    resultado = escaner_corporativo.escanear(objetivo, puertos)

    # Contar puertos abiertos
    puertos_abiertos = sum(1 for _, estado in resultado if estado == "abierto")
    mensaje_log = f"{objetivo} - {puertos_abiertos} puertos abiertos - {fecha_actual}"

    # Guardar log
    escaner_corporativo.guardar_log(log_path, mensaje_log)

    # Exportar CSV
    escaner_corporativo.exportar_csv(csv_path, resultado, fecha_actual)

    # Enviar alerta
    escaner_corporativo.alerta(objetivo)

    print("Escaneo finalizado.")
