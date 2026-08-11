#!/usr/bin/env python3
"""Gera arquivos .tsv importáveis no Anki a partir das aulas.

Lê a seção "Cards pro Anki" de cada aula em modules/ e monta um arquivo por
módulo, com tag hierárquica por aula. Rodar sempre que uma aula mudar:

    python scripts/build_anki_deck.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "modules"
OUT_DIR = ROOT / "anki"

# Pega o bloco de código que vem logo depois do título "Cards pro Anki".
CARD_BLOCK = re.compile(r"Cards pro Anki\s*\n+```\n(.*?)```", re.DOTALL)

# Em qual dos dois decks do Módulo 0 cada módulo cai.
DECKS = {
    "1A-fundacao-gramatical": "English::Grammar Patterns",
    "1B-vocabulario-base": "English::Vocabulary",
}


def extract(lesson_file):
    """Retorna [(front, back)] de uma aula."""
    block = CARD_BLOCK.search(lesson_file.read_text(encoding="utf-8"))
    if not block:
        return []

    cards = []
    for line in block.group(1).splitlines():
        if "|" not in line:
            continue
        front, back = line.rsplit("|", 1)
        front, back = " ".join(front.split()), " ".join(back.split())
        if front and back:
            cards.append((front, back))
    return cards


def build(module_dir):
    lessons = sorted(p for p in module_dir.iterdir() if p.is_dir())
    module_tag = module_dir.name.split("-")[0]

    rows = []
    per_lesson = []

    for lesson in lessons:
        readme = lesson / "README.md"
        if not readme.exists():
            continue
        cards = extract(readme)
        per_lesson.append((lesson.name, len(cards)))
        tag = f"{module_tag}::{lesson.name}"
        rows += [(f, b, tag) for f, b in cards]

    if not rows:
        return None

    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"{module_dir.name}.tsv"

    # Cabeçalho de diretivas: o Anki lê isso e configura a importação sozinho.
    header = [
        "#separator:tab",
        "#html:false",
        "#notetype:Basic",
        f"#deck:{DECKS.get(module_dir.name, 'English::' + module_dir.name)}",
        "#tags column:3",
    ]
    body = ["\t".join(r) for r in rows]
    # newline="" impede o Windows de virar \r\n — o \r sujaria as diretivas.
    with out.open("w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(header + body) + "\n")

    return out, len(rows), per_lesson


def main():
    if not MODULES.exists():
        sys.exit("Pasta modules/ não encontrada.")

    total = 0
    for module_dir in sorted(p for p in MODULES.iterdir() if p.is_dir()):
        result = build(module_dir)
        if not result:
            print(f"{module_dir.name}: nenhum card encontrado.")
            continue

        out, count, per_lesson = result
        total += count
        print(f"\n{out.relative_to(ROOT)} — {count} cards")
        for name, n in per_lesson:
            print(f"    {n:>3}  {name}")

    print(f"\nTotal: {total} cards")


if __name__ == "__main__":
    main()
