# Configure the Google Cloud provider
provider "google" {
  project = "mlops-lab-477022"
  region  = "us-central1"
  zone    = "us-central1-a"
}

# 1. Compute Engine VM
resource "google_compute_instance" "vm_instance" {
  name         = "terraform-markdown-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  labels = {
    purpose = "markdown-lab"
  }

  # Network tag used by the firewall rule
  tags = ["markdown-app"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {} # Grants an external IP
  }

  # Startup script: Installs dependencies and runs the app
  metadata_startup_script = <<-EOT
    #!/bin/bash
    exec > /var/log/startup-script.log 2>&1
    set -eux

    # Install Python and pip
    apt-get update -y
    apt-get install -y python3 python3-pip

    # Create app directory
    mkdir -p /opt/markdown_app

    # Write the Flask app code to the VM
    cat << 'PYEOF' >/opt/markdown_app/markdown_web.py
from flask import Flask, request, render_template_string
import markdown

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Markdown Previewer</title>
  <style>
    body { font-family: sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
    h1 { text-align: center; }
    .container { display: flex; gap: 20px; height: 60vh; }
    .box { flex: 1; display: flex; flex-direction: column; }
    textarea { flex: 1; padding: 10px; font-family: monospace; font-size: 14px; }
    .preview { flex: 1; padding: 10px; border: 1px solid #ccc; background: #f9f9f9; overflow-y: auto; }
    button { margin-top: 10px; padding: 10px 20px; font-size: 16px; cursor: pointer; background: #007bff; color: white; border: none; }
  </style>
</head>
<body>
  <h1>Markdown to HTML Previewer</h1> 
  <form method="post">
    <div class="container">
      <div class="box">
        <h3>Markdown Input</h3>
        <textarea name="md_text" placeholder="# Type Markdown here...">{{ md_text }}</textarea>
      </div>
      <div class="box">
        <h3>HTML Preview</h3>
        <div class="preview">
          {{ html_result|safe }}
        </div>
      </div>
    </div>
    <div style="text-align: center;">
      <button type="submit">Convert / Preview</button>
    </div>
  </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    md_text = ""
    html_result = ""
    if request.method == "POST":
        md_text = request.form.get("md_text", "")
        try:
            html_result = markdown.markdown(md_text, extensions=['extra'])
        except Exception as e:
            html_result = f"<p style='color:red'>Error: {e}</p>"

    return render_template_string(PAGE, md_text=md_text, html_result=html_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
PYEOF

    # Install Python dependencies
    pip3 install flask markdown

    # Run the app in the background
    nohup python3 /opt/markdown_app/markdown_web.py > /var/log/markdown_web.log 2>&1 &
  EOT
}

# 2. Firewall Rule
resource "google_compute_firewall" "allow-markdown-8080" {
  name    = "allow-markdown-8080"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["8080"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["markdown-app"]
}

# 3. Storage Bucket (Optional, for practice)
resource "google_storage_bucket" "markdown_bucket" {
  name          = "markdown-lab-bucket-${random_id.bucket_suffix.hex}"
  location      = "us-central1"
  force_destroy = true
}

# Generate a random suffix for the bucket name to ensure uniqueness
resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# 4. Outputs
output "app_url" {
  value = "http://${google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip}:8080"
}