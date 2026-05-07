from pathlib import Path
import shutil
import sys

pasta = Path(sys.argv[1])  

for arquivo in pasta.iterdir():

    if arquivo.is_dir():
        continue

    extensao = arquivo.suffix

    nome_pasta = extensao.lstrip(".").lower() if extensao else "no_extension"

    destino = pasta / nome_pasta

    destino.mkdir(exist_ok=True)

    shutil.move(str(arquivo), str(destino / arquivo.name))

    print(f"Movido: {arquivo.name}")

