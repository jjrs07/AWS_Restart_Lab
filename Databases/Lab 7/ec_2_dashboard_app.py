from flask import Flask, jsonify, render_template_string
import requests
import psutil

app = Flask(__name__)

# HTML Template (served from root)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EC2 Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f8f9fa; }
    header { background: #fff; padding: 10px 20px; border-bottom: 1px solid #ccc; display: flex; align-items: center; }
    header h1 { margin: 0; font-size: 20px; color: #333; }
    nav a { margin-left: 20px; text-decoration: none; color: #333; font-weight: bold; }
    main { padding: 30px; }
    .card { background: white; padding: 20px; max-width: 600px; margin: auto; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    th, td { padding: 10px; border-bottom: 1px solid #ddd; text-align: left; }
    .cpu { font-size: 24px; font-weight: bold; color: #28a745; }
  </style>
</head>
<body>
  <header>
    <h1>AWS</h1>
    <nav>
      <a href="#">Load Test</a>
      <a href="#">RDS</a>
    </nav>
  </header>
  <main>
    <div class="card">
      <h2>Meta-Data</h2>
      <table>
        <tr><th>Meta-Data</th><th>Value</th></tr>
        <tr><td>InstanceId</td><td id="instance-id">Loading...</td></tr>
        <tr><td>Availability Zone</td><td id="availability-zone">Loading...</td></tr>
      </table>
      <p>Current CPU Load: <span class="cpu" id="cpu-load">0%</span></p>
    </div>
  </main>
  <script>
    function updateMetadata() {
      fetch('/metadata').then(res => res.json()).then(data => {
        document.getElementById('instance-id').textContent = data.instance_id;
        document.getElementById('availability-zone').textContent = data.availability_zone;
      });
    }
    function updateCPULoad() {
      fetch('/cpu').then(res => res.json()).then(data => {
        document.getElementById('cpu-load').textContent = data.cpu_load + "%";
      });
    }
    updateMetadata();
    updateCPULoad();
    setInterval(updateCPULoad, 3000);
  </script>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(HTML_PAGE)

@app.route("/metadata")
def metadata():
    try:
        instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id", timeout=1).text
        az = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone", timeout=1).text
    except Exception:
        instance_id = "Unavailable"
        az = "Unavailable"
    return jsonify({"instance_id": instance_id, "availability_zone": az})

@app.route("/cpu")
def cpu():
    return jsonify({"cpu_load": psutil.cpu_percent(interval=1)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
