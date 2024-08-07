# snmp ricoh


#### simple snmp requests for ricoh printers

- modified this lines in app.py with your path
```
# Write the rendered HTML to the output file
output_file_path = "/enteryourpath/" + output_file

# Route to serve the generated HTML file
@app.route('/snmp_walk_result.html')
def serve_snmp_html():
return send_from_directory("/enteryourpath/", "snmp_walk_result.html")


```
- change in file index.html the ip address of printers
