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
    button:hover { background: #0056b3; }
  </style>
</head>
<body>
  <h1>Markdown to HTML Previewer</h1>
  
  <form method="post">
    <div class="container">
      <div class="box">
        <h3>Markdown Input</h3>
        <textarea name="md_text" placeholder="# Type Markdown here...&#10;- Item 1&#10;- Item 2">{{ md_text }}</textarea>
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
            html_result = f"<p style='color:red'>Error converting markdown: {e}</p>"

    return render_template_string(
        PAGE,
        md_text=md_text,
        html_result=html_result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)