#!/usr/bin/env python3
import sys
import os

OUTFILE = "fotoliste.html"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Fotoliste</title>
</head>
<body>
  <h1>{title}</h1>
  <table>
  {table_rows}
  </table>
</body>
</html>
"""

ROW_TEMPLATE = """
    <td align="center"> <img width="100%" src="{src}"><br> {name} </td>"""


def create_table_rows(images_files, entries_per_row=4):
    entries = 0
    html = "<tr>"

    for image in images_files:
        if not image.endswith(".jpg"):
            print("ignoring", image)
            continue

        if entries % entries_per_row == 0:
            html += "</tr>\n<tr>"

        name = image.replace(".jpg", "").replace(" ", ", ", 1)
        # print(image, "->", name)
        html += ROW_TEMPLATE.format(src=image, name=name)
        entries += 1

    html += "</tr>"

    return html


def main():
    if len(sys.argv) != 2:
        print("Need one argument: folder with images")
        return

    folder = sys.argv[1]
    print("using pictures from", folder)
    tab_rows = create_table_rows(os.listdir(folder))
    html = HTML_TEMPLATE.format(title=folder, table_rows=tab_rows)
    print("Creating", OUTFILE, "in", folder, "title is", folder)
    with open(folder + "/" + OUTFILE, "wt") as outfile:
        outfile.write(html)


if __name__ == "__main__":
    main()