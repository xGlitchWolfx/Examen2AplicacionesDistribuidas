import sys
from collections import Counter


filename = sys.argv[1]
counts = Counter()

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        parts = [part.strip() for part in line.strip().split(",")]
        if len(parts) != 5:
            continue

        usuario, accion, fecha, hora, video = parts
        hora_bloque = hora[:2]

        counts[f"usuario|{usuario}"] += 1
        counts[f"hora|{hora_bloque}"] += 1

        if accion == "view":
            counts[f"video_views|{video}"] += 1
            counts[f"ratio_view|{video}"] += 1
        elif accion == "like":
            counts[f"video_likes|{video}"] += 1
            counts[f"ratio_like|{video}"] += 1
        elif accion == "comment":
            counts[f"video_comments|{video}"] += 1
            counts[f"ratio_comment|{video}"] += 1
        elif accion == "shared":
            counts[f"ratio_shared|{video}"] += 1

with open(f"{filename}.out", "w", encoding="utf-8") as out:
    for key, count in counts.items():
        out.write(f"{key} {count}\n")

print(f"Mapper procesado: {filename}")
