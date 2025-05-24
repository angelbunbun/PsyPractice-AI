
from flask import Flask, request, jsonify
import os
import fitz
import requests

app = Flask(__name__)
manual_texts = {}

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

manual_links = {'CFT – Gilbert & Simos': 'https://drive.google.com/uc?id=1Jv0ucXU6Pta2mtAKqmo5YSGQ8m1aVeHL', 'ACT – Oxford Handbook': 'https://drive.google.com/uc?id=1pIoU6ZYa_mgnbtZLezB1Df7akTehE7A7', 'DBT – Linehan Manual': 'https://drive.google.com/uc?id=11vUuxUp03eRreshEUzsgUBzlvhS8a22K', 'ACT – 100 Key Points': 'https://drive.google.com/uc?id=1Q1_jHtx2QYCAI9lLflJRRNCDhhzm2r_I', 'CFT – Made Simple': 'https://drive.google.com/uc?id=1fK17sp4S74F4DXyT4S4MGtxgaiCEHsnd', 'CBT – Brief Guide': 'https://drive.google.com/uc?id=1ov-UpxqkulA3l7KW5bwTPruVVRtR5ltI', 'CBT – Beck': 'https://drive.google.com/uc?id=1G0CTMdzQylzPQYj1BOCPPdES1erS8ewc', 'CBT – Practical Guide': 'https://drive.google.com/uc?id=1ZF7ayvCLBFZ5ZMoeesuC6DhEhb6K4tRJ', 'EMDR – Shapiro': 'https://drive.google.com/uc?id=1yFxGJ1fOwck7kHYphcWIQfavVcISZYxV', 'DBT – Made Simple': 'https://drive.google.com/uc?id=1YM57GL1INv-eYotsBUcY_-XxUtX7ptqg', 'DSM-5-TR': 'https://drive.google.com/uc?id=1bXzuquafCOjAvs4T28ATO3Km-Bm0zl43', 'Interpersonal Process – Teyber': 'https://drive.google.com/uc?id=1fYycTwydvnIx_Jd2SrXAGEFKudjYhKKN', 'Therapy Theories – Sommers-Flanagan': 'https://drive.google.com/uc?id=1IzvRP85edgI4J--hvajnCTYQlp13Cpt7', 'Clinical Interviewing – Sommers-Flanagan': 'https://drive.google.com/uc?id=1pe5JN5mxG-DNMVm-sOs2JSpH3vwXCc7d', 'Therapist Dialogue – McHenry': 'https://drive.google.com/uc?id=12phEA2-lstYoXcF-sCfW3qLmwDf3T_hg', 'Counselling & Psychotherapy – Carl Rogers': 'https://drive.google.com/uc?id=1-t-5k9JrZGIqvdNHc5JNV5aijsLQ5YLF', 'The Gift of Therapy – Yalom': 'https://drive.google.com/uc?id=1G5VxS6df3FYPOANnMVNws_mLYUpBoqVF'}

for label, url in manual_links.items():
    manual_texts[label] = download_and_extract_text(label, url)

@app.route("/")
def home():
    return "PsyPractice Manual Search API is live!"

@app.route("/search", methods=["POST"])
def search_manuals():
    data = request.get_json()
    query = data.get("query", "").lower()

    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = []
    for label, content in manual_texts.items():
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
