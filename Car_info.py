from dataclasses import dataclass, field, asdict
from typing import List, Dict, Union
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@dataclass
class Car:
    brand: str
    model: str
    year: int
    engine: float
    transmission: str
    accessories: List[str] = field(default_factory=list)

    def update(self, data: Dict[str, Union[str, int, float, List[str]]]):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def serialize(self):
        return asdict(self)


# Initialize a default car object
car = Car(
    brand="Hyundai",
    model="hb20",
    year=2015,
    engine=1.6,
    transmission="automatic",
    accessories=[]
)


# API Endpoints
@app.route("/car", methods=["GET"])
def get_car():
    return jsonify(car.serialize()), 200


@app.route("/car", methods=["POST"])
def update_car():
    data = request.get_json(force=True)
    car.update(data)
    return jsonify({"message": "Car updated successfully", "car": car.serialize()}), 200


@app.route("/car/accessories", methods=["POST"])
def add_accessory():
    data = request.get_json(force=True)
    accessory = data.get("accessory")
    if accessory and accessory not in car.accessories:
        car.accessories.append(accessory)
        return jsonify({"message": f"Accessory '{accessory}' added.", "accessories": car.accessories}), 200
    return jsonify({"error": "Invalid or duplicate accessory"}), 400


@app.route("/car/accessories", methods=["DELETE"])
def clear_accessories():
    car.accessories.clear()
    return jsonify({"message": "All accessories removed", "accessories": car.accessories}), 200


# Simple HTML frontend with a form to view/update the car
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Car Info</title>
</head>
<body>
    <h1>Car Information</h1>
    <form id="carForm">
        Brand: <input type="text" name="brand" value="{{ car.brand }}" /><br/>
        Model: <input type="text" name="model" value="{{ car.model }}" /><br/>
        Year: <input type="number" name="year" value="{{ car.year }}" /><br/>
        Engine (L): <input type="number" step="0.1" name="engine" value="{{ car.engine }}" /><br/>
        Transmission: <input type="text" name="transmission" value="{{ car.transmission }}" /><br/>
        Accessories: <ul>
            {% for a in car.accessories %}
                <li>{{ a }}</li>
            {% else %}
                <li>No accessories added.</li>
            {% endfor %}
        </ul>
        <button type="submit">Update Car</button>
    </form>

    <h2>Add Accessory</h2>
    <form id="accessoryForm">
        <input type="text" name="accessory" placeholder="Accessory name" />
        <button type="submit">Add Accessory</button>
    </form>

    <button id="clearAccessoriesBtn">Remove All Accessories</button>

    <div id="response"></div>

<script>
const carForm = document.getElementById('carForm');
const accessoryForm = document.getElementById('accessoryForm');
const clearBtn = document.getElementById('clearAccessoriesBtn');
const responseDiv = document.getElementById('response');
const accessoriesList = document.querySelector('form#carForm ul');

async function refreshAccessories() {
    const res = await fetch('/car');
    const data = await res.json();
    accessoriesList.innerHTML = '';
    if (data.accessories.length > 0) {
        data.accessories.forEach(acc => {
            const li = document.createElement('li');
            li.textContent = acc;
            accessoriesList.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'No accessories added.';
        accessoriesList.appendChild(li);
    }
}

carForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(carForm);
    const data = Object.fromEntries(formData.entries());
    data.year = parseInt(data.year);
    data.engine = parseFloat(data.engine);

    const res = await fetch('/car', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    const json = await res.json();
    responseDiv.textContent = json.message;
    refreshAccessories();
});

accessoryForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(accessoryForm);
    const accessory = formData.get('accessory');

    const res = await fetch('/car/accessories', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ accessory })
    });
    const json = await res.json();
    responseDiv.textContent = json.message;
    if (res.ok) {
        accessoryForm.reset();
        await refreshAccessories();
    }
});

clearBtn.addEventListener('click', async () => {
    const res = await fetch('/car/accessories', { method: 'DELETE' });
    const json = await res.json();
    responseDiv.textContent = json.message;
    await refreshAccessories();
});
refreshAccessories();
</script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, car=car)


if __name__ == "__main__":
    app.run(debug=True)
