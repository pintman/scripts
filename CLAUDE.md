# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Überblick

Dieses Repo ist eine private Sammlung eigenständiger Skripte (überwiegend
Python, teils Shell), die der Autor auf verschiedenen Rechnern einsetzt
(Bezug zu Schule/Unterricht, z.B. Klausuren, WebUntis, IHK). Es gibt keine
gemeinsame Anwendung, kein Package und keinen zentralen Entry Point — jede
Datei in `bin/` ist ein unabhängiges, direkt ausführbares Tool. Die Skripte
nicht zu einem gemeinsamen Package zusammenführen oder gemeinsame Module
einführen, außer es wird explizit verlangt.

## Struktur

- `bin/` — die eigentlichen Skripte, eine Datei = ein Tool. Mischung aus
  Python 3 (`.py`) und POSIX-/Bash-Shell (`.sh` oder ohne Endung). Keine
  Unterpakete; nichts importiert etwas anderes aus diesem Repo.
- `docker.exam/` — Docker-Setup, um isolierte Klausur-Container zu starten
  (SSH + Apache je Container), siehe `docker.exam/README.md`.
- `rpi_admin/` — Ansible-Playbooks (`setup.yml`, `abgaben_einsammeln.yml`) zur
  Administration einer Flotte von Raspberry Pis im Klassenraum, siehe
  `rpi_admin/README.md`.
- `etc/` — diverse Konfiguration (`pylintrc`, `vimrc`, `wtf/`).

## Befehle

Abhängigkeiten werden mit Poetry verwaltet (`pyproject.toml` /
`poetry.lock`, Python `^3.12`).

```bash
poetry install          # Abhängigkeiten installieren
poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
poetry run python -m doctest bin/*.py   # "Tests" sind Doctests in den Skripten
```

Das sind exakt die Schritte, die auch die CI ausführt
(`.github/workflows/python-app.yml`). Die meisten Skripte haben keine
Doctests; nur ergänzen, wenn die Logik eines Skripts das tatsächlich
rechtfertigt (siehe `bin/freies_magazin.py` als Beispiel).

Es gibt keinen separaten Build-Schritt und keine Testsuite über flake8 +
doctest hinaus — jedes Skript wird direkt ausgeführt, z.B. `./bin/stella.py`
oder `python3 bin/stella.py`.

`bin/klausur_check.sh` ist ein eigenständiges Qualitäts-Check-Tool für dieses
Repo: es baut ein Wegwerf-venv, führt `ruff check` und `findlike`
(Duplikat-/Ähnlichkeitserkennung) über alle `*.py`-Dateien aus und schreibt
`check.log` / `similarities.log`.

## Konventionen in den Skripten

- Python-Skripte beginnen mit `#!/usr/bin/env python3` und sind ausführbar
  (`chmod +x`), damit sie eigenständig aus `bin/` heraus gestartet werden
  können.
- Konfiguration erfolgt über Umgebungsvariablen, gelesen mit
  `os.environ.get('NAME', default)` als Modul-Konstanten nahe dem
  Dateianfang (z.B. `UNTIS_USER`, `MASTODON_API`, `ORT`) — nicht über
  Config-Dateien oder CLI-Flags. Einige Skripte nutzen `click` für echtes
  CLI-Argument-Parsing (z.B. `webuntis_absences.py`, `msteams.py`).
- Mehrere Skripte steuern einen echten Browser per Selenium
  (`selenium.webdriver.Firefox`) gegen Schul-/Behörden-Webportale (WebUntis,
  Stella, Bürgerbüro, IHK) — diese sind naturgemäß zustandsbehaftet/
  interaktiv und nicht unit-testbar; Änderungen daran müssen live gegen die
  jeweilige Seite geprüft werden.
- Secrets (Passwörter, Tokens) werden ausschließlich über Umgebungsvariablen
  gelesen, nie hartcodiert. Die CI setzt Dummy-Werte (`TIBROS_USER=0` etc.)
  nur, damit Imports/Doctests nicht an fehlenden Env-Variablen scheitern.
- Shell-Skripte nutzen meist `#!/bin/sh` oder `#!/bin/bash`; POSIX-nah
  bleiben, außer die jeweilige Datei nutzt bereits Bash-spezifische
  Features.

## Agent skills

### Issue tracker

Issues liegen in GitHub Issues (`pintman/scripts`, via `gh`). See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` im Repo-Root. See `docs/agents/domain.md`.
