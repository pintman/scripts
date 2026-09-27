## Überblick

Dieses Repo ist eine private Sammlung eigenständiger Skripte.

## Struktur

- `bin/` — die eigentlichen Skripte, eine Datei = ein Tool. Mischung aus
  Python 3 (`.py`) und POSIX-/Bash-Shell (`.sh` oder ohne Endung).
- `docker.exam/` — Docker-Setup, um isolierte Klausur-Container zu starten
  Details in `docker.exam/README.md`.
- `rpi_admin/` — Ansible-Playbooks (`setup.yml`, `abgaben_einsammeln.yml`) zur
  Administration einer Flotte von Raspberry Pis im Klassenraum, Details in
  `rpi_admin/README.md`.
- `etc/` — diverse Konfiguration (`pylintrc`, `vimrc`, `wtf/`).

## Konventionen in den Skripten

- Python-Skripte beginnen mit `#!/usr/bin/env python3` und sind ausführbar
  (`chmod +x`), damit sie eigenständig aus `bin/` heraus gestartet werden
  können. Skripte mit Drittbibliotheken nutzen stattdessen
  `#!/usr/bin/env -S pipx run` plus PEP-723-Header (siehe `README.md`);
  kein uv.
- Konfiguration erfolgt über Umgebungsvariablen, gelesen mit
  `os.environ.get('NAME', default)` als Modul-Konstanten nahe dem
  Dateianfang (z.B. `UNTIS_USER`, `MASTODON_API`, `ORT`) — nicht über
  Config-Dateien oder CLI-Flags. Einige Skripte nutzen `click` für echtes
  CLI-Argument-Parsing (z.B. `webuntis_absences.py`, `msteams.py`).
- Secrets (Passwörter, Tokens) werden ausschließlich über Umgebungsvariablen
  gelesen, nie hartcodiert. Die CI setzt Dummy-Werte (`TIBROS_USER=0` etc.)
  nur, damit Imports/Doctests nicht an fehlenden Env-Variablen scheitern.

## Agent skills

### Issue tracker

Issues liegen in GitHub Issues (`pintman/scripts`, via `gh`). See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` im Repo-Root. See `docs/agents/domain.md`.
