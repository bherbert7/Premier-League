from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_league_table():
    url = "https://www.premierleague.com/tables"  # Example URL (may change)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table and extract data (inspect the website to find the correct elements)
    table = soup.find("table", class_="standing-table__table")  # Example class name
    # ... (Code to extract team names, positions, points, etc. from the table) ...

    # Format the data into a list of dictionaries (or another suitable structure)
    league_table = [
        {"position": 1, "team": "Team A", "played": 10, "won": 8, "drawn": 2, "lost": 0, "points": 26},
        # ... more teams ...
    ]
    return league_table

@app.route("/api/table")
def table_api():
    table_data = get_league_table()
    return jsonify(table_data)

if __name__ == "__main__":
    app.run(debug=True)