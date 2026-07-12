def predict_flood_risk(rainfall, discharge, soil):
    score = (rainfall * 0.4 + discharge * 0.4 + soil * 100 * 0.2) / 200

    if score < 0.4:
        level = "Low"
    elif score < 0.7:
        level = "Medium"
    else:
        level = "High"

    return round(score, 3), level
