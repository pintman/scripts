#!/usr/bin/env python3
#
# A helper script for creating an array of images in an HTML file from a list
# of images inside a folder. Call the script with the image folder as the
# only argument. The folder name will be used as title.

import sys
import os

OUTFILE = "fotoliste.html"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Fotoliste {title}</title>
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

        name = image.replace(".jpg", "").replace(" ", ", ", 1)
        html += ROW_TEMPLATE.format(src=image, name=name)
        entries += 1

        if entries % entries_per_row == 0:
            html += "</tr>\n<tr>"

    html += "</tr>"
    return html


def main():
    if len(sys.argv) != 2:
        print("Need one argument: folder with images")
        return

    folder = os.path.normpath(sys.argv[1])
    print("using pictures from", folder)
    title = os.path.basename(folder)
    tab_rows = create_table_rows(os.listdir(folder))
    html = HTML_TEMPLATE.format(title=title, table_rows=tab_rows)
    print("Creating", OUTFILE, "in", folder, "with title", title)
    with open(os.path.join(folder, OUTFILE), "wt") as outfile:
        outfile.write(html)


if __name__ == "__main__":
    main()
