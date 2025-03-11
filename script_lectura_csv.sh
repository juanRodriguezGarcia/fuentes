#!/bin/bash

# Archivos
CSV_FILE="archivo.csv"
LOG_FILE="procesar.log"
TEMP_FILE="temp.csv"

# Verificar si el archivo existe
if [ ! -f "$CSV_FILE" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: Archivo CSV no encontrado" | tee -a "$LOG_FILE"
    exit 1
fi

# Leer el CSV línea por línea
while IFS= read -r linea || [ -n "$linea" ]; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Procesando: $linea" | tee -a "$LOG_FILE"

    # Simular procesamiento (reemplázalo con la lógica real)
    sleep 1

    # Remover la línea ya procesada del CSV original
    tail -n +2 "$CSV_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$CSV_FILE"

    echo "$(date '+%Y-%m-%d %H:%M:%S') - Línea procesada y eliminada" | tee -a "$LOG_FILE"
done < "$CSV_FILE"

echo "$(date '+%Y-%m-%d %H:%M:%S') - Proceso finalizado" | tee -a "$LOG_FILE"









#!/bin/bash

CSV_FILE="archivo.csv"
LOG_FILE="procesar.log"
TEMP_FILE="temp.csv"
LOCK_FILE="/tmp/csv.lock"

# Usar flock para evitar accesos simultáneos
exec 200>"$LOCK_FILE"
flock -n 200 || { echo "$(date '+%Y-%m-%d %H:%M:%S') - Otro proceso está usando el CSV" | tee -a "$LOG_FILE"; exit 1; }

# Verificar si el archivo CSV existe y tiene datos
if [ ! -s "$CSV_FILE" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: Archivo CSV vacío o no encontrado" | tee -a "$LOG_FILE"
    exit 1
fi

# Leer y procesar línea a línea
while IFS= read -r linea || [ -n "$linea" ]; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Procesando: $linea" | tee -a "$LOG_FILE"

    # Simular procesamiento (reemplázalo con la lógica real)
    sleep 1

    # Remover la línea ya procesada del CSV original
    tail -n +2 "$CSV_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$CSV_FILE"

    echo "$(date '+%Y-%m-%d %H:%M:%S') - Línea procesada y eliminada" | tee -a "$LOG_FILE"
done < "$CSV_FILE"

echo "$(date '+%Y-%m-%d %H:%M:%S') - Proceso finalizado" | tee -a "$LOG_FILE"

