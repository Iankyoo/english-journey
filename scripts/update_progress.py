#!/usr/bin/env python3
"""Recalcula o bloco de progresso do README a partir dos checkboxes.

Uso:
    python scripts/update_progress.py          # reescreve o README
    python scripts/update_progress.py --check  # falha se estiver desatualizado
"""

import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

START = "<!-- progress:start -->"
END = "<!-- progress:end -->"

H2 = re.compile(r"^##\s+(.+?)\s*$")
MODULE_HEADING = re.compile(r"^.*?Módulo\s+(\S+)\s+—\s+(.+?)$")
CHECKBOX = re.compile(r"^\s*-\s+\[( |x|X)\]\s")

# Seções sem "Módulo" no título que ainda contam como etapa da jornada.
TRACKED_EXTRAS = ("Projeto Final", "Metas Alcançadas")

BAR_WIDTH = 24


def parse(text):
    """Retorna (secoes, feitos_total, total) a partir das linhas do README."""
    sections = []
    current = None

    for line in text.splitlines():
        heading = H2.match(line)
        if heading:
            # Qualquer H2 encerra a seção anterior — sem isso, os checkboxes
            # de "Projeto Final" e "Metas" vazam para o último módulo.
            current = None
            title = heading.group(1)

            module = MODULE_HEADING.match(title)
            if module:
                current = {"id": module.group(1), "name": module.group(2)}
            elif any(extra in title for extra in TRACKED_EXTRAS):
                # Tira emoji e espaços da frente para o rótulo da tabela.
                current = {"id": title.split(maxsplit=1)[-1].strip(), "name": ""}

            if current:
                current |= {"done": 0, "total": 0, "is_module": bool(module)}
                sections.append(current)
            continue

        box = CHECKBOX.match(line)
        if box and current is not None:
            current["total"] += 1
            if box.group(1).lower() == "x":
                current["done"] += 1

    done = sum(s["done"] for s in sections)
    total = sum(s["total"] for s in sections)
    return sections, done, total


def bar(done, total, width=BAR_WIDTH):
    if total == 0:
        return "░" * width
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)


def pct(done, total):
    return 0.0 if total == 0 else 100 * done / total


def render(sections, done, total):
    modules = [s for s in sections if s["is_module"]]
    complete = sum(1 for m in modules if m["total"] and m["done"] == m["total"])

    lines = [
        START,
        "",
        f"**`{bar(done, total)}`  {pct(done, total):.1f}%**",
        "",
        f"`Módulos concluídos: {complete} / {len(modules)}` "
        f"`Tarefas: {done} / {total}` "
        f"`Duração estimada: ~38 semanas`",
        "",
        "<details>",
        "<summary>Progresso por seção</summary>",
        "",
        "| Seção | | Feito |",
        "|-------|---|-------|",
    ]

    for s in sections:
        mark = " ✅" if s["total"] and s["done"] == s["total"] else ""
        label = f"**{s['id']}** — {s['name']}" if s["name"] else f"**{s['id']}**"
        lines.append(
            f"| {label} "
            f"| `{bar(s['done'], s['total'], 12)}` "
            f"| {s['done']}/{s['total']}{mark} |"
        )

    lines += ["", "</details>", "", END]
    return "\n".join(lines)


def main():
    text = README.read_text(encoding="utf-8")

    if START not in text or END not in text:
        sys.exit(f"Marcadores {START} / {END} não encontrados no README.md")

    sections, done, total = parse(text)
    block = render(sections, done, total)

    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _: block,
        text,
        flags=re.DOTALL,
    )

    if "--check" in sys.argv:
        if updated != text:
            sys.exit("README.md desatualizado — rode: python scripts/update_progress.py")
        print("README.md está atualizado.")
        return

    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print(f"Atualizado: {done}/{total} tarefas ({pct(done, total):.1f}%)")
    else:
        print("Nada a mudar.")


if __name__ == "__main__":
    main()
