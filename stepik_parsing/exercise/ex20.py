header = """<html>
    <body>
        <table>
"""
footer = """\t\t</table>
    </body>
</html>
"""
table = ''
for i in range(1, 11):
    table += '\t\t\t<tr>\n'
    for j in range(1, 11):
        table += '\t\t\t\t<td>' + str(i * j) + '</td>\n'
    table += '\t\t\t</tr>\n'

with open("html/ex20.html", "w", encoding='utf-8') as f:
    f.write(header)
    f.write(table)
    f.write(footer)
