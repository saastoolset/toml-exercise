from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

config = tomllib.loads(Path("tic_tac_toe.toml").read_text(encoding="utf-8"))
print(config)