def generate_explanation(data):
    return (
        f"Flood risk is {data['risk_level']} due to rainfall "
        f"{data['rainfall']} mm, discharge {data['discharge']} m3/s, "
        f"and soil moisture {data['soil_moisture']}. "
        f"Take precautions and monitor conditions."
    )
