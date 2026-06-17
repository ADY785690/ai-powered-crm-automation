def classify_lead(score):
    if score >= 80:
        return "Hot"
    elif score >= 50:
        return "Warm"
    else:
        return "Cold"
