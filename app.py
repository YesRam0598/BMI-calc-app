from flask import Flask, request

app = Flask(__name__)

def getCatRisk(bmi):

    if bmi < 18.5:
        cat = "Underweight"
        risk = "Malnutrition risk"
    elif bmi < 25:
        cat = "Normal weight"
        risk = "Low risk"
    elif bmi < 30:
        cat = "Overweight "
        risk = "Enhanced risk"
    elif bmi < 35:
        cat = "Moderately "
        risk = "Medium risk"
    elif bmi < 40:
        cat = "Severely obese"
        risk = "High risk"
    else:
        cat = "Very severely obese"
        risk = "Very high risk"

    return {"cat" : cat, "risk" : risk}

@app.route("/", methods=['GET'])
def getBMIData():
    req = request.json
    data = req["data"]
    for i in range(len(data)):
        d = data[i]
        bmi = d["WeightKg"]/((d["HeightCm"]/100)**2)
        bmiData = getCatRisk(bmi)
        cat = bmiData["cat"]
        risk = bmiData["risk"]
        data[i]["BMI"] = bmi
        data[i]["Category"] = cat
        data[i]["Risk"] = risk
    return {"data":  data}



if __name__ == '__main__':
    app.run()