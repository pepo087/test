import subprocess
from flask import Flask, request, jsonify, render_template, send_from_directory
from jinja2 import Template

app = Flask(__name__)

def run_snmpwalk_to_html(ip_address, output_file):
    # Run snmpwalk command
    command = ['snmpwalk', '-v', '2c', '-c', 'public', '-OXsq', ip_address]
    
    try:
        # Run the snmpwalk command
        result = subprocess.run(command, capture_output=True, check=True)
        
        # Decode the output using latin-1 encoding
        output = result.stdout.decode('latin-1')
        # Print the SNMP walk result in the terminal
        print("Original SNMP Walk Result:")
        print(output)
        # Filter lines with specific OIDs
        lines = [line.strip() for line in output.split('\n') if line.startswith(('mib-2.43.5.1.1.16.1', 'mib-2.43.5.1.1.17.1','mib-2.43.18.1.1.8.1.1'))]
        
        # Initialize variables to store the values
        model_value = 'N/A'
        matricola_value = 'N/A'
        toner_value='N/A'

        for line in lines:
            if 'mib-2.43.5.1.1.16.1' in line:
                model_value = line.split('"')[1]
            elif 'mib-2.43.5.1.1.17.1' in line:
                matricola_value = line.split('"')[1]
            elif 'mib-2.43.18.1.1.8.1.1' in line:
                toner_value = line.split('"')[1]
                

        # Jinja2 template for HTML table
        template_str = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>SNMP Walk Result for {{ ip_address }}</title>
        </head>
        <body>
            <h2>SNMP Walk Result for {{ ip_address }}</h2>
            <table border="1">
                <tr><th>Field</th><th>OID</th><th>Value</th></tr>
                <tr><td>Model</td><td>mib-2.43.5.1.1.16.1</td><td>{{ model_value }}</td></tr>
                <tr><td>Matricola</td><td>mib-2.43.5.1.1.17.1</td><td>{{ matricola_value }}</td></tr>
                <tr><td>Toner</td><td>mib-2.43.18.1.1.8.1.1</td><td>{{ toner_value }}</td></tr>
            </table>
        </body>
        </html>
        '''
        template = Template(template_str)
        
        # Render the template with the IP address and values
        rendered_html = template.render(ip_address=ip_address, model_value=model_value, matricola_value=matricola_value,toner_value=toner_value)
        
        # Write the rendered HTML to the output file
        output_file_path = "/Users/administrator/Library/CloudStorage/Dropbox/Zsysadmin/romana maceri/test/" + output_file
        with open(output_file_path, 'w') as f:
            f.write(rendered_html)
        
        return True, f"SNMP walk result has been saved to {output_file_path}"
    except subprocess.CalledProcessError as e:
        return False, f"Error executing snmpwalk: {e}"

# Route to generate SNMP HTML
@app.route('/generate_snmp_html', methods=['POST'])
def generate_snmp_html():
    ip_address = request.json.get('ip_address')
    output_file = 'snmp_walk_result.html'
    success, message = run_snmpwalk_to_html(ip_address, output_file)
    if success:
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'message': message}), 500

# Route to serve the generated HTML file
@app.route('/snmp_walk_result.html')
def serve_snmp_html():
    return send_from_directory("/Users/administrator/Library/CloudStorage/Dropbox/Zsysadmin/romana maceri/test/", "snmp_walk_result.html")

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)