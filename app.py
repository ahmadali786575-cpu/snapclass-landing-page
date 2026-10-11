
from flask import Flask, render_template, send_from_directory, Response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/robots.txt")
def robots():
    content = """User-agent: *
Allow: /

Sitemap: https://snapclass-landing-page-eta.vercel.app/sitemap.xml
"""
    return Response(content, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(
        "static",
        "sitemap.xml",
        mimetype="application/xml"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5002)
