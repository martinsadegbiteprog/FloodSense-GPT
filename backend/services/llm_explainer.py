from rag.query import retrieve
import os
from openai import OpenAI

USE_LLM = True
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_explanation(data):
    context = retrieve("flood risk and mitigation")

    prompt = f"""
    Context:
    {context}

    Rainfall: {data['rainfall']}
    Discharge: {data['discharge']}
    Soil: {data['soil_moisture']}
    Risk: {data['risk_level']}

    Explain clearly and give advice.
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
