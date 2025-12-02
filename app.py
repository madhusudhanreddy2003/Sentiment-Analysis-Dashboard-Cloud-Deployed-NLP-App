import os
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# --------------------------
#  Load local HF model once
# --------------------------
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# CPU-only pipeline (device = -1)
sentiment_model = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME,
    device=-1
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "").strip()

    if not text:
        # Empty input -> treat as neutral
        return render_template(
            "results.html",
            text=text,
            label="NEUTRAL",
            score=0.0
        )

    try:
        result = sentiment_model(text)[0]
        label = result["label"]
        score = float(result["score"])
        score = round(score, 2)
    except Exception as e:
        # If anything goes wrong, log and show graceful error
        print("Error during sentiment analysis:", e, flush=True)
        label = "ERROR"
        score = 0.0

    return render_template(
        "results.html",
        text=text,
        label=label,
        score=score
    )

if __name__ == "__main__":
    # local debug only
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
