html = """<html>
    <body>
        <table>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>4</td>
            </tr>
        </table>
    </body>
</html>
"""

with open("html/ex19.html", "w", encoding='utf-8') as f:
    f.write(html)