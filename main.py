from flask import Flask, request, jsonify
import os
import fitz  # PyMuPDF

app = Flask(__name__)

# Load all PDF manuals into memory
manual_texts = {}

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {str(e)}"

manual_folder = "manuals"
for filename in os.listdir(manual_folder):
    if filename.endswith(".pdf"):
        filepath = os.path.join(manual_folder, filename)
        manual_texts[filename] = extract_text_from_pdf(filepath)

@app.route("/")
def home():
    return "PsyPractice Manual Search API is running!"

@app.route("/search", methods=["POST"])
def search_manuals():
    data = request.get_json()
    query = data.get("query", "").lower()

    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = []

    for manual_name, content in manual_texts.items():
        matches = [line.strip() for line in content.split("\n") if query in line.lower()]
        if matches:
            results.append({
                "manual": manual_name,
                "matches": matches[:3]
            })

    if not results:
        return jsonify({"result": "No relevant content found."})

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
