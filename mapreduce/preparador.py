from pathlib import Path
from urllib.request import urlopen
import os


DATOS_URL = os.environ.get("DATOS_URL", "http://host.docker.internal:8080/datos")


def main():
    with urlopen(DATOS_URL) as response:
        contenido = response.read().decode("utf-8")

    Path("entrada.txt").write_text(contenido, encoding="utf-8")
    lineas = [linea for linea in contenido.splitlines() if linea.strip()]
    print(f"Entrada generada desde {DATOS_URL}")
    print(f"Registros descargados: {len(lineas)}")


if __name__ == "__main__":
    main()
