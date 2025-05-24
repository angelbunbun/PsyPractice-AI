
from flask import Flask, request, jsonify
import os
import fitz
import requests

app = Flask(__name__)
manual_texts = {}


manual_scopes = {
    "microskills": [
        "Clinical Interviewing  Sommers-Flanagan",
        "Therapy Theories  Sommers-Flanagan",
        "Interpersonal Process  Teyber",
        "Counselling & Psychotherapy  Carl Rogers",
        "The Gift of Therapy  Yalom",
        "Therapist Dialogue  McHenry"
    ],
    "intervention": [
        "DBT  Linehan Manual",
        "DBT  Made Simple",
        "CBT  Beck",
        "CBT  Practical Guide",
        "CBT  Brief Guide",
        "ACT  100 Key Points",
        "ACT  Oxford Handbook",
        "CFT  Made Simple",
        "CFT  Gilbert & Simos",
        "EMDR  Shapiro"
    ],
    "formulation": [
        "DSM-5-TR",
        "CBT  Beck",
        "CBT  Practical Guide",
        "ACT  Oxford Handbook",
        "CFT  Gilbert & Simos",
        "DBT  Linehan Manual"
    ],
    "evaluation": [
        "Clinical Interviewing  Sommers-Flanagan",
        "Therapy Theories  Sommers-Flanagan",
        "Interpersonal Process  Teyber",
        "Counselling & Psychotherapy  Carl Rogers",
        "The Gift of Therapy  Yalom",
        "Therapist Dialogue  McHenry"
    ],
    "study": [
        "DBT  Linehan Manual",
        "DBT  Made Simple",
        "CBT  Beck",
        "CBT  Practical Guide",
        "CBT  Brief Guide",
        "ACT  100 Key Points",
        "ACT  Oxford Handbook",
        "CFT  Made Simple",
        "CFT  Gilbert & Simos",
        "EMDR  Shapiro"
    ]
}


def download_and_extract_text(label, url):
    try:
        local_path = f"manuals/{label}.pdf"
        if not os.path.exists("manuals"):
            os.makedirs("manuals")
        if not os.path.exists(local_path):
            print(f"Downloading: {label}")
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        print(f"Extracting: {label}")
        doc = fitz.open(local_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error processing {label}: {str(e)}"

# Placeholder Google Drive links (to be replaced with actual mapping in production)
manual_links = {
    manual: "https://drive.google.com/uc?id=dummy_id" for scope in manual_scopes.values() for manual in scope
}

for label, url in manual_links.items():
    if label not in manual_texts:
        manual_texts[label] = download_and_extract_text(label, url)

@app.route("/")
def home():
    return "PsyPractice Manual Search API is live!"

@app.route("/search", methods=["POST"])
def search_manuals():
    data = request.get_json()
    query = data.get("query", "").lower()
    scope = data.get("scope")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    manuals_to_search = manual_texts.keys()
    if scope and scope in manual_scopes:
        manuals_to_search = manual_scopes[scope]

    results = []
    for label in manuals_to_search:
        content = manual_texts.get(label, "")
        matches = [line.strip() for line in content.split("\n") if query in line.lower()]
        if matches:
            results.append({
                "manual": label,
                "matches": matches[:3]
            })

    if not results:
        return jsonify({"result": "No relevant content found."})

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
