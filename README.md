# snmp ricoh


#### simple snmp requests for ricoh printers for MacOs system



> [!IMPORTANT]
>
> 
>- modified this lines in app.py with your path
```
# Write the rendered HTML to the output file
output_file_path = "/enteryourpath/" + output_file

# Route to serve the generated HTML file
@app.route('/snmp_walk_result.html')
def serve_snmp_html():
return send_from_directory("/enteryourpath/", "snmp_walk_result.html")


```
> [!IMPORTANT]
> - change in file index.html inside templates with the ip address of printers
```

<li><a href="#" onclick="generateHTML('x.x.0.10')">printer1</a></li>
<li><a href="#" onclick="generateHTML('x.x.0.181')">printer2</a></li>
<li><a href="#" onclick="generateHTML('x.x.0.183')">printer3</a></li>
```

> [!TIP]
> Run in vscode or other editor and thats'it!



![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://github.com/pepo087/test/blob/main/snmp_screen.png)
