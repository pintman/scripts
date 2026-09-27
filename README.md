# Scripts

Das Projekt beinhaltet eine Sammlung von Skripten, die ich auf
unterschiedlichen Plattformen benötige.

## Skripte mit Abhängigkeiten

Skripte, die Bibliotheken außerhalb der Standardbibliothek brauchen, geben
diese als Inline Script Metadata ([PEP 723](https://peps.python.org/pep-0723/))
im Skript selbst an und werden über `pipx run` gestartet. Sie sind damit ohne
`poetry run` direkt aufrufbar:

```python
#!/usr/bin/env -S pipx run
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests"]
# ///
```

```bash
./bin/bo_buergerbuero_termine.py
```

Voraussetzung ist pipx >= 1.4 (`brew install pipx` bzw. `apt install pipx`).
Unter Windows gibt es keinen Shebang, dort `pipx run bin/<skript>.py`.

pipx legt je Skript eine gecachte Umgebung in `~/Library/Caches/pipx/<hash>/`
(macOS) an. Sie wird 14 Tage nach ihrer Erstellung beim nächsten `pipx run`
verworfen und neu gebaut; ändern sich die Abhängigkeiten im Header, entsteht
eine neue Umgebung.

uv wird bewusst nicht verwendet. Ab pipx 1.17 nutzt pipx uv jedoch
automatisch als Backend, sobald uv im `PATH` liegt. Um das zu verhindern:

```bash
export PIPX_DEFAULT_BACKEND=pip   # z.B. in ~/.zshrc
```

Poetry (`pyproject.toml`) bleibt für die Entwicklung und die CI (flake8,
doctest) bestehen.

