import os
import jinja2
SAMPLE_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>

<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>Helen Bennett</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Yoshi Tannamuri</td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
  </tr>
</table>

</body>
</html>
"""

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
    white-space: nowrap;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>

<table>
  <tr>
    <th>Item Name</th>
    <th>Source</th>
    <th>Price</th>
    <th>Picture</th>
  </tr>
  {{rows}}
</table>

</body>
</html>
"""

#<td> <img src=\"{3}\" alt="PIC TITLE GOES HERE style="width:128px;height:128px;"> </td>
ROW_TEMPLATE = """
<tr>
  <td> <a href=\"{4}\"> {0} </a> </td>
  <td>{1}</td><td>{2}</td>
  <td> <img src=\"{3}\" alt="PIC TITLE GOES HERE style="width:100px;height:100px;"> </td>
</tr>"""

def row_formatter(table_rows):
    """
    Description:
        Formats a string of table rows into an HTML Table Template
    Arguments:
        table_rows (str) - HTML markup for rows to be inserted into the table 
    """
    return jinja2.Template(TEMPLATE).render(rows=table_rows)

def write_ebay_page(formatted_html, output_path):
    """
    Description:
        Writes an html
    Arguments:
        table_rows (str) - HTML markup for rows to be inserted into the table 
    """
    if os.path.exists(output_path):
        raise IOError("{} already exists! Cannot write here..".format(output_path))

    with open(output_path, "w") as html_writer:
        html_writer.write(formatted_html)
