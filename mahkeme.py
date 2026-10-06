#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işığı Yüksek Mahkemesi.

Kapak açıkken ışık vardır. Kapak kapalıyken yargı vardır.
Çalıştırmak: python3 mahkeme.py [dilekçe]
"""

from __future__ import annotations

import hashlib
import random
import sys
import textwrap

UYELER = (
    "Ampul Üyesi (sürekli konuşur, az aydınlatır)",
    "Kapı Contası Üyesi (muhalefet şerhi sızdırır)",
    "Raftaki Hardal Üyesi (usulden reddeder, esastan yer)",
)

KARARLAR = (
    "IŞIK YANAR, ama sadece kimse bakmıyorken. Bu bir hak değil, alışkanlıktır.",
    "IŞIK YANMAZ. Yanıyormuş gibi yapmak, enerji tasarrufunun tiyatro hâlidir.",
    "IŞIK KARARSIZDIR. Ara karar: lamba mütalaa için keşfe gönderilsin.",
    "DAVA DÜŞER. Başvurucu kapağı açık unutmuş, süt tanıklıktan çekilmiştir.",
    "IŞIK YANAR VE ÖZÜR DİLER. Gerekçe: gece 03:14'te sucuk yalnız bırakılamaz.",
)


def _tohum(metin: str) -> int:
    ozet = hashlib.sha256(metin.encode("utf-8")).hexdigest()
    return int(ozet[:8], 16)


def durusma(dilekce: str) -> str:
    rng = random.Random(_tohum(dilekce))
    heyet = list(UYELER)
    rng.shuffle(heyet)
    karar = rng.choice(KARARLAR)
    muhalefet = rng.choice(heyet)
    sure = rng.randint(4, 47)
    satirlar = [
        "BUZDOLABI IŞIĞI YÜKSEK MAHKEMESİ",
        "Esas no: " + str(rng.randint(2026, 2099)) + "/" + str(rng.randint(1, 999)),
        "Dilekçe: " + dilekce.strip(),
        "Heyet (rastgele oturma düzeni):",
    ]
    for i, uye in enumerate(heyet, 1):
        satirlar.append(f"  {i}. {uye}")
    satirlar.append(f"Müzakere süresi: {sure} saliselik ciddiyet")
    satirlar.append("KARAR: " + karar)
    satirlar.append("Muhalefet şerhi: " + muhalefet + " bu işe contanın karışmasını usulsüz bulmuştur.")
    satirlar.append("Temyiz: kapağı kapatın. Dosya kendiliğinden soğur.")
    return "\n".join(satirlar)


def main() -> int:
    dilekce = " ".join(sys.argv[1:]).strip() or "Kapak kapandı, ışık hâlâ orada mı, mahkeme söylesin."
    print(durusma(dilekce))
    print()
    print(textwrap.fill(
        "İşbu karar, buzdolabının içinde okunursa geçerlidir. Dışarıda okunursa dedikodudur.",
        width=72,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
