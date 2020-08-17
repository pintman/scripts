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
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css">
</head>
<body>
  <h1>{title}</h1>
  <table>
  <tbody>
  {table_rows}
  <tbody>
  </table>
</body>
</html>
"""

ROW_TEMPLATE = """
    <td valign="bottom"> <img width="100%" src="{src}"><br>
    {name} </td>"""


def create_table_rows(images_files, entries_per_row=5):
    entries = 0
    html = "<tr>"

    for image in images_files:
        if not (image.endswith(".jpg") or image.endswith('.png')):
            print("ignoring", image)
            continue

        name, _suffix = os.path.splitext(image)
        html += ROW_TEMPLATE.format(src=image, name=name)
        entries += 1

        if entries % entries_per_row == 0:
            html += "</tr>\n<tr>"

    html += "</tr>"
    return html


def main():
    if len(sys.argv) != 3:
        print("Need two arguments: name of class and folder with images")
        return

    folder = os.path.normpath(sys.argv[2])
    print("using pictures from", folder)
    title = sys.argv[1]
    tab_rows = create_table_rows(sorted(os.listdir(folder)))
    html = HTML_TEMPLATE.format(title=title, table_rows=tab_rows)
    print("Creating", OUTFILE, "in", folder, "with title", title)
    with open(os.path.join(folder, OUTFILE), "wt") as outfile:
        outfile.write(html)


if __name__ == "__main__":
    main()
