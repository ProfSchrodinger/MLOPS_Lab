# Terraform GCP Lab – Markdown Previewer

This project uses **Terraform** to deploy a Python Flask app on **Google Cloud**. The app converts Markdown text to HTML in real-time.

## Architecture
* **VM:** `e2-micro` (Debian 11) with a startup script to install Python/Flask.
* **Firewall:** Allows TCP traffic on port **8080**.
* **Storage:** A Cloud Storage bucket with a unique random ID.

## Quick Start

**1. Authenticate & Initialize**
```bash
gcloud auth application-default login
terraform init
```

**2. Deploy Infrastructure**
```bash
terraform apply
# Type 'yes' to confirm
```

**3. Access the App**
* Wait 2 minutes for the VM to configure itself.
* Open the app_url printed in the terminal (e.g., http://35.x.x.x:8080).

## Cleanup

To remove all resources and avoid costs:
```
terraform destroy
```