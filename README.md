# Renombrador Masivo de Archivos 🗂️🔄

(Arquitecto Técnico_JMC) Herramienta de escritorio ligera y rápida para renombrar múltiples archivos en lote. Desarrollada en Python con una interfaz gráfica intuitiva, está pensada para organizar entregas documentales, planos y modelos BIM asegurando una nomenclatura estandarizada sin riesgo de errores.

## 🚀 Características Principales

* **Patrones Personalizables:** Define rápidamente un texto base, un número de inicio secuencial y el separador (`_`, `-`, espacio o `.`).

* **Autocompletado Inteligente (Zero-padding):** Calcula automáticamente los ceros a la izquierda necesarios (ej. `01`, `02`... `10`) en base a la cantidad de archivos para mantener un orden alfanumérico perfecto en el explorador de Windows.

* **Previsualización en Tiempo Real:** Visualiza cómo quedarán exactamente los nombres en una tabla antes de aplicar cualquier cambio en tu disco duro.

* **Gestión de Errores Integrada:** Detecta conflictos de nombres (archivos ya existentes) o problemas de permisos sin detener el proceso abruptamente, mostrando un informe final.

* **Sin Dependencias Externas:** Construido 100% con las librerías estándar de Python. No requiere instalación de paquetes adicionales.

## ⚙️ Requisitos e Uso

Al no depender de librerías de terceros (como `pandas` o `matplotlib`), poner a funcionar esta herramienta es instantáneo. Solo necesitas tener Python instalado en tu equipo.

1. Clona este repositorio en tu equipo:

   ```bash
   git clone [https://github.com/TU_USUARIO/renombrador-masivo.git](https://github.com/TU_USUARIO/renombrador-masivo.git)
2. Navega al directorio del proyecto:
   
   ```bash
   cd renombrador-masivo
   
3. Ejecuta el script directamente (no necesitas pip install):
   
   ```bash
   python "Renombrador Archivos v01 by JMCG.py"
   
## 👨‍💻 Autor

Jose Manuel Caamaño González | Arquitecto Técnico & BIM Manager.
Digital Product Lead | ConTech & Digital Twin SaaS | BIM, Energy Modeling & Sustainability | Data Analytics (SQL, Power BI)

Hecho con código y café desde A Coruña. ☕

Jose Manuel Caamaño González | [LinkedIn](https://www.linkedin.com/in/jmcaamanog/)

Acuérdate de cambiar `TU_USUARIO` en el bloque de instalación por el tuyo de GitHub. Pégalo en tu VS Code, haz el "Commit" y "Sync Changes" que te comenté antes, y lo tendrás brillando en la web en cuestión de segundos. ¡Dale caña!
