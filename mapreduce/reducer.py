import os
from collections import Counter, defaultdict
from pathlib import Path


final_counts = Counter()

for file in os.listdir("splits"):
    if file.endswith(".out"):
        with open(f"splits/{file}", "r", encoding="utf-8") as f:
            for line in f:
                key, count = line.strip().split()
                final_counts[key] += int(count)


def extraer_por_prefijo(prefix):
    result = {}
    for key, count in final_counts.items():
        key_prefix, value = key.split("|", 1)
        if key_prefix == prefix:
            result[value] = count
    return result


def mayor(diccionario):
    return max(diccionario.items(), key=lambda item: item[1])


views = extraer_por_prefijo("video_views")
likes = extraer_por_prefijo("video_likes")
comments = extraer_por_prefijo("video_comments")
usuarios = extraer_por_prefijo("usuario")
horas = extraer_por_prefijo("hora")

ratio_data = defaultdict(lambda: {"like": 0, "comment": 0, "shared": 0, "view": 0})
for prefix, action in [
    ("ratio_like", "like"),
    ("ratio_comment", "comment"),
    ("ratio_shared", "shared"),
    ("ratio_view", "view"),
]:
    for video, count in extraer_por_prefijo(prefix).items():
        ratio_data[video][action] = count

ratios = {}
for video, data in ratio_data.items():
    if data["view"] == 0:
        ratios[video] = 0
    else:
        ratios[video] = (data["like"] + data["comment"] + data["shared"]) / data["view"]

resultados = [
    "RESULTADOS MAP REDUCE",
    f"Video mas visto: {mayor(views)[0]} ({mayor(views)[1]} views)",
    f"Video con mas likes: {mayor(likes)[0]} ({mayor(likes)[1]} likes)",
    f"Video mas comentado: {mayor(comments)[0]} ({mayor(comments)[1]} comentarios)",
    f"Usuario mas recurrente: {mayor(usuarios)[0]} ({mayor(usuarios)[1]} interacciones)",
    f"Hora con mas interaccion: {mayor(horas)[0]}:00 ({mayor(horas)[1]} interacciones)",
    f"Mayor ratio de interaccion: {max(ratios.items(), key=lambda item: item[1])[0]} ({max(ratios.items(), key=lambda item: item[1])[1]:.2f})",
]

salida = "\n".join(resultados)
Path("resultados.txt").write_text(salida + "\n", encoding="utf-8")
print(salida)
