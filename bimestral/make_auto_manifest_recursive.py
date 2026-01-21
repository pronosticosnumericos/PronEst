#!/usr/bin/env python3
"""Genera auto_manifest.json listando TODOS los *.json (incluye subcarpetas).

Útil si tus JSON no están en el mismo nivel que el HTML.

Uso:
  cd /media/climdes1/DATA/ClimaProAgro/01-NMME/Nacional/29-EF-MA-MJ-2026/auto
  python3 make_auto_manifest_recursive.py

Salida:
  auto_manifest.json  (con rutas relativas, p. ej. "json/NMME_prate_prom_202601.json")
"""

from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import json

def main() -> None:
    root = Path(".").resolve()

    files = []
    for p in root.rglob("*.json"):
        if not p.is_file():
            continue
        if p.name.lower() == "auto_manifest.json":
            continue
        files.append(str(p.relative_to(root)))

    files = sorted(files, key=lambda s: s.lower())

    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": len(files),
        "files": files
    }

    out = root / "auto_manifest.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {out} ({len(files)} archivos)")

if __name__ == "__main__":
    main()
