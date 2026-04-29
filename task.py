import requests
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser

def scrape_website():
    url = input("Enter website URL (with https://): ").strip()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print("\n🔄 Fetching data...\n")

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract data
        title = soup.title.string.strip() if soup.title else "No Title Found"
        h1_tags = [h.get_text(strip=True) for h in soup.find_all("h1")]
        h2_tags = [h.get_text(strip=True) for h in soup.find_all("h2")]
        links = list(set([a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("http")]))

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create HTML content
        html_content = f"""
        <html>
        <head>
            <title>Web Scraper Report</title>
            <style>
                body {{
                    font-family: Arial;
                    background-color: #f4f4f4;
                    padding: 20px;
                }}
                h1 {{
                    color: #2c3e50;
                }}
                .box {{
                    background: white;
                    padding: 15px;
                    margin-bottom: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px gray;
                }}
                ul {{
                    max-height: 200px;
                    overflow-y: scroll;
                }}
                a {{
                    color: blue;
                }}
            </style>
        </head>
        <body>

        <h1>🌐 Web Scraper Report</h1>

        <div class="box">
            <p><b>URL:</b> {url}</p>
            <p><b>Title:</b> {title}</p>
            <p><b>Scraped on:</b> {time_now}</p>
        </div>

        <div class="box">
            <h2>H1 Headings ({len(h1_tags)})</h2>
            <ul>
                {''.join(f"<li>{h}</li>" for h in h1_tags)}
            </ul>
        </div>

        <div class="box">
            <h2>H2 Headings ({len(h2_tags)})</h2>
            <ul>
                {''.join(f"<li>{h}</li>" for h in h2_tags)}
            </ul>
        </div>

        <div class="box">
            <h2>Links ({len(links)})</h2>
            <ul>
                {''.join(f"<li><a href='{l}' target='_blank'>{l}</a></li>" for l in links[:30])}
            </ul>
        </div>

        </body>
        </html>
        """

        # Save HTML file
        file_name = "report.html"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_content)

        print("✅ Report generated successfully!")
        print("📂 Opening in browser...")

        # Open in browser
        webbrowser.open(file_name)

    except Exception as e:
        print("❌ Error:", e)


scrape_website()