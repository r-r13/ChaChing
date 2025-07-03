from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    habit = request.form['habit']
    cost = float(request.form['cost'])
    frequency = int(request.form['frequency'])
    duration = int(request.form['duration'])
    unit = request.form['unit']

    # Number of days per unit for calculation
    unit_days = {"days": 1, "weeks": 7, "months": 30, "years": 365}
    days_in_unit = unit_days.get(unit, 30)

    # Calculate total instances
    total_instances = duration * frequency * days_in_unit

    total_cost = round(cost * total_instances, 2)

    # Build cumulative cost data for chart
    cumulative_costs = []
    for i in range(1, duration + 1):
        instances = frequency * i * days_in_unit
        cost_at_i = round(cost * instances, 2)
        cumulative_costs.append(cost_at_i)

    # Fun comparisons as before
    comparisons = []
    if total_cost >= 1300:
        comparisons.append(f"That's a MacBook Air (~$1300)")
    if total_cost >= 800:
        comparisons.append(f"Or a flight to Hawaii and back (~$800)")
    if total_cost >= 500:
        comparisons.append(f"Or a new iPhone SE (~$500)")
    if total_cost >= 200:
        comparisons.append(f"Or 25 Chipotle burritos 🌯")
    if total_cost >= 100:
        comparisons.append(f"Or 12 months of Netflix Premium")
    
    fun_units = int(total_cost // 5)
    if fun_units > 0:
        comparisons.append(f"Or {fun_units} iced coffees ☕")

    return render_template(
        'result.html',
        habit=habit,
        total=total_cost,
        comparisons=comparisons,
        cumulative_costs=cumulative_costs,
        duration=duration,
        unit=unit
    )


if __name__ == '__main__':
    app.run(debug=True)
