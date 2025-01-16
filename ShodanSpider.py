import argparse
import random
import re
import requests
from urllib.parse import quote
from colorama import init, Fore, Style

# Inicializar colorama para compatibilidad en Windows
init(autoreset=True)

# Definir códigos de color
ROJO = Fore.RED
VERDE = Fore.GREEN
AMARILLO = Fore.YELLOW
AZUL = Fore.BLUE
CIAN = Fore.CYAN
BLANCO = Fore.WHITE
RESET = Style.RESET_ALL

# Mostrar el banner
def mostrar_banner():
    print(f"{VERDE}#########################################################{RESET}")
    print(f"{CIAN}#                                                       #{RESET}")
    print(f"{VERDE}#            ████▓▒░  5h0d4n 5p1d3r  ░▒▓████            #{RESET}")
    print(f"{CIAN}#                                                       #{RESET}")
    print(f"{VERDE}#########################################################{RESET}")
    print(f"{AZUL}#              ▓▒░ Creado por: C1ph3rByt3               #{RESET}")
    print(f"{VERDE}#########################################################{RESET}")
    print()

# Validar que las IPs estén dentro del rango permitido
def ip_valida(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    return all(0 <= int(parte) <= 255 for parte in partes if parte.isdigit())

# Procesar argumentos
def procesar_argumentos():
    parser = argparse.ArgumentParser(description="5h0d4n5p1d3r")
    parser.add_argument("-q", type=str, help="Buscar en Shodan con una consulta específica")
    parser.add_argument("-cve", type=str, help="Buscar en Shodan para un CVE específico")
    parser.add_argument("-o", type=str, help="Guardar la salida en un archivo especificado")
    args = parser.parse_args()

    if not (args.q or args.cve):
        print(f"{ROJO}Error: Debes proporcionar una consulta (-q) o un CVE (-cve). Usa -h para ayuda.{RESET}")
        exit(1)

    consulta = args.q if args.q else f"vuln:{args.cve}"
    return consulta, args.o

# Ejecutar la solicitud a Shodan
def ejecutar_consulta(consulta, agente_usuario):
    consulta_codificada = quote(consulta)
    url = f"https://www.shodan.io/search/facet?query={consulta_codificada}&facet=ip"
    headers = {
        "User-Agent": agente_usuario,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"{ROJO}Error en la solicitud: {e}{RESET}")
        exit(1)

# Filtrar direcciones IP válidas
def filtrar_ips(texto):
    ips = re.findall(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', texto)
    ips_filtradas = sorted(
        ip for ip in ips
        if ip_valida(ip) and not re.match(r'^(0|127|169\.254|172\.(1[6-9]|2[0-9]|3[0-1])|192\.168|10|224|240)\.', ip)
    )
    return ips_filtradas

# Guardar resultados en un archivo
def guardar_resultados(ips, archivo_salida):
    try:
        with open(archivo_salida, "w") as f:
            f.write("\n".join(ips))
        print(f"{VERDE}Resultados guardados en {archivo_salida}.{RESET}")
    except IOError as e:
        print(f"{ROJO}Error al guardar el archivo: {e}{RESET}")

# Función principal
def main():
    mostrar_banner()
    consulta, archivo_salida = procesar_argumentos()

    # Agentes de usuario aleatorios
    agentes_usuario = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.30.86 Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15",
        "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    ]

    agente_usuario = random.choice(agentes_usuario)
    texto_respuesta = ejecutar_consulta(consulta, agente_usuario)
    ips_filtradas = filtrar_ips(texto_respuesta)

    total_ips = len(ips_filtradas)
    if total_ips > 0:
        print("\n".join(ips_filtradas))
        print(f"{CIAN}Total de direcciones IP encontradas: {total_ips}{RESET}")
        if archivo_salida:
            guardar_resultados(ips_filtradas, archivo_salida)
    else:
        print(f"{AMARILLO}No se encontraron direcciones IP válidas.{RESET}")

if __name__ == "__main__":
    main()
