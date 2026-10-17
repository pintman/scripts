#!/usr/bin/env python3
"""Prüft alle Feed-URLs einer OPML-Datei auf Erreichbarkeit und Feed-Inhalt.

Ausgabe maskiert Query-Strings und lange Pfadsegmente (Tokens).
Aufruf: check_feeds.py <datei.opml>
"""
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit

TIMEOUT = 20
UA = "Mozilla/5.0 (Macintosh) NetNewsWire-Feedcheck"


def mask(url):
    p = urlsplit(url)
    segs = [("…" if re.fullmatch(r"[A-Za-z0-9_\-]{20,}", s) else s)
            for s in p.path.split("/")]
    q = "?…" if p.query else ""
    return f"{p.scheme}://{p.netloc}{'/'.join(segs)}{q}"


def check(item):
    folder, title, url = item
    return (folder,) + _check(title, url)


def _check(title, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(4096).lstrip().lower()
            final = r.geturl()
            redirected = final.rstrip("/") != url.rstrip("/")
            looks_feed = (body.startswith(b"<?xml") or b"<rss" in body
                          or b"<feed" in body or b"<rdf" in body
                          or body.startswith(b"{"))
            if not looks_feed:
                return ("KEIN FEED", title, url, f"HTTP {r.status}, Inhalt kein RSS/Atom"
                        + (f", umgeleitet → {mask(final)}" if redirected else ""))
            if redirected:
                return ("UMLEITUNG", title, url, f"→ {mask(final)}")
            return ("OK", title, url, "")
    except urllib.error.HTTPError as e:
        return ("FEHLER", title, url, f"HTTP {e.code} {e.reason}")
    except Exception as e:  # Timeout, DNS, SSL, Verbindung
        return ("FEHLER", title, url, f"{type(e).__name__}: {e}"[:120])


def main(path):
    root = ET.parse(path).getroot()
    feeds = []
    for folder in root.find("body"):
        name = folder.get("title") or folder.get("text") or "?"
        for o in folder.iter("outline"):
            if o.get("xmlUrl"):
                feeds.append((name, o.get("title") or o.get("text") or "?", o.get("xmlUrl")))
    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(check, feeds))
    order = {"FEHLER": 0, "KEIN FEED": 1, "UMLEITUNG": 2, "OK": 3}
    results.sort(key=lambda r: (order[r[1]], r[0].lower(), r[2].lower()))
    for folder, status, title, url, info in results:
        if status not in ("OK", "UMLEITUNG"):
            print(f"{status}\t{folder}\t{title}\t{info}")
    counts = {k: sum(r[1] == k for r in results) for k in order}
    print(f"\n{len(results)} Feeds geprüft: " + ", ".join(f"{k} {v}" for k, v in counts.items()))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"Aufruf: {sys.argv[0]} <datei.opml>")
    main(sys.argv[1])
