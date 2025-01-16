
# 5h0d4n5p1d3r

**5h0d4n5p1d3r** es una herramienta diseñada para buscar información en Shodan de manera eficiente. Este script facilita consultas específicas y puede guardar los resultados en un archivo.

---

## Instalación

1. Clona el repositorio o descarga el script:
   ```bash
   git clone https://github.com/c1ph3rbyt3/ShodanSpider.git
   cd ShodanSpider
   ```

2. Asegúrate de tener Python instalado (versión 3.7 o superior).

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

### Opciones

Ejecuta el script con las siguientes opciones disponibles:

- `-q [consulta]`:
  Realiza una búsqueda en Shodan basada en una consulta específica.

- `-cve [id-cve]`:
  Busca vulnerabilidades asociadas a un CVE específico.

- `-o [archivo]`:
  Guarda los resultados en un archivo de texto.

- `-h`:
  Muestra el mensaje de ayuda detallando todas las opciones.

---

### Ejemplos de uso

1. **Búsqueda general en Shodan:**
   ```bash
   python ShodanSpider.py -q "apache"
   ```

2. **Búsqueda de un CVE específico:**
   ```bash
   python ShodanSpider.py -cve "cve-2024-39943"
   ```

3. **Guardar resultados en un archivo:**
   ```bash
   python ShodanSpider.py -q "nginx" -o resultados.txt
   ```

---

## Notas adicionales

- Este script es una mejora del trabajo original realizado por [Shubham Rooter](https://github.com/shubhamrooter).
- Para ejecutar el script, asegúrate de tener conexión a Internet.
- Si necesitas más ayuda, utiliza la opción `-h` para obtener una descripción completa.

---

## Contacto

Creado por: **C1ph3rByt3**
