from pathlib import Path
contador = 0
while contador < 100:
    contador = contador + 1
    path = Path(f"Day {contador} /")
    path.mkdir()
