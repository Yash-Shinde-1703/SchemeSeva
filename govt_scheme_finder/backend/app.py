from flask import Flask, render_template, request
import json
import os

app = Flask(__name__, instance_path='/tmp/instance')

# Create the instance path directory if it doesn't exist
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Load the data from the JSON files
def load_data():
    schemes_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schemes.json')
    categories_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'categories.json')
    with open(schemes_path) as f:
        schemes = json.load(f)
    with open(categories_path) as f:
        categories = json.load(f)
    return schemes, categories

schemes, categories = load_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_schemes = schemes
    selected_category = "All"
    selected_state = "All"

    if request.method == 'POST':
        selected_category = request.form.get('category')
        selected_state = request.form.get('state')

        if selected_category and selected_category != 'All':
            filtered_schemes = [s for s in filtered_schemes if s.get('category') == selected_category]

        if selected_state and selected_state != 'All':
            filtered_schemes = [s for s in filtered_schemes if s.get('state') == selected_state]

    states = sorted(list(set(s['state'] for s in schemes if 'state' in s)))

    return render_template('index.html',
                           schemes=filtered_schemes,
                           categories=categories,
                           states=states,
                           selected_category=selected_category,
                           selected_state=selected_state)

if __name__ == '__main__':
    app.run(debug=True)
