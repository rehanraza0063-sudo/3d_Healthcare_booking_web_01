from flask import Flask, render_template_string, request, jsonify
import random
import time

app = Flask(__name__)

# ---------------------------------------------------------
# DEMO DATA
# ---------------------------------------------------------

doctors = [
    {
        "id": 1,
        "name": "Dr. Aisha Sharma",
        "speciality": "Cardiologist",
        "hospital": "CityCare Hospital",
        "experience": "12 Years",
        "rating": "4.9",
        "fee": 800
    },
    {
        "id": 2,
        "name": "Dr. Rahul Mehta",
        "speciality": "Neurologist",
        "hospital": "Apollo Medical Center",
        "experience": "10 Years",
        "rating": "4.8",
        "fee": 1000
    },
    {
        "id": 3,
        "name": "Dr. Priya Nair",
        "speciality": "Dermatologist",
        "hospital": "HealthPlus Hospital",
        "experience": "8 Years",
        "rating": "4.7",
        "fee": 600
    },
    {
        "id": 4,
        "name": "Dr. Arjun Patel",
        "speciality": "Orthopedic",
        "hospital": "MetroCare Hospital",
        "experience": "15 Years",
        "rating": "4.9",
        "fee": 900
    }
]

medicines = [
    {"id": 1, "name": "Paracetamol 500mg", "category": "Pain Relief", "price": 35},
    {"id": 2, "name": "Vitamin C Tablets", "category": "Supplement", "price": 120},
    {"id": 3, "name": "ORS Sachets", "category": "Hydration", "price": 40},
    {"id": 4, "name": "First Aid Kit", "category": "Emergency", "price": 299},
    {"id": 5, "name": "Digital Thermometer", "category": "Medical Device", "price": 199},
    {"id": 6, "name": "Antiseptic Solution", "category": "First Aid", "price": 95}
]

hospitals = [
    {
        "id": 1,
        "name": "CityCare Hospital",
        "location": "Mumbai Central",
        "beds": 24,
        "icu": 6,
        "emergency": True
    },
    {
        "id": 2,
        "name": "HealthPlus Hospital",
        "location": "Dadar",
        "beds": 17,
        "icu": 3,
        "emergency": True
    },
    {
        "id": 3,
        "name": "MetroCare Hospital",
        "location": "Andheri",
        "beds": 31,
        "icu": 8,
        "emergency": True
    },
    {
        "id": 4,
        "name": "Apollo Medical Center",
        "location": "Powai",
        "beds": 12,
        "icu": 2,
        "emergency": False
    }
]

bookings = []

# ---------------------------------------------------------
# HTML
# ---------------------------------------------------------

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>MediSphere 3D Healthcare</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

body {
    background:
        radial-gradient(circle at 20% 20%, #173d50 0%, transparent 30%),
        radial-gradient(circle at 80% 10%, #173456 0%, transparent 30%),
        linear-gradient(135deg, #06121d, #081c2c 50%, #05111c);

    color: white;
    min-height: 100vh;
}

/* NAVBAR */

nav {
    position: sticky;
    top: 0;
    z-index: 100;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px 6%;

    background: rgba(5, 18, 30, 0.82);
    backdrop-filter: blur(15px);

    border-bottom: 1px solid rgba(255,255,255,.08);
}

.logo {
    font-size: 25px;
    font-weight: bold;
}

.logo span {
    color: #28e0c2;
}

nav button {
    background: transparent;
    color: white;
    border: none;
    margin-left: 18px;
    cursor: pointer;
    font-size: 14px;
}

nav button:hover {
    color: #28e0c2;
}

/* HERO */

.hero {
    min-height: 500px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 60px 7%;
    gap: 40px;
}

.hero-text {
    max-width: 600px;
}

.hero h1 {
    font-size: clamp(42px, 6vw, 75px);
    line-height: 1.05;
    margin-bottom: 25px;
}

.hero h1 span {
    color: #28e0c2;
}

.hero p {
    color: #a8c1ce;
    font-size: 18px;
    line-height: 1.7;
}

.hero-buttons {
    margin-top: 30px;
}

.primary {
    padding: 15px 25px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg,#28e0c2,#17a9e0);
    color: #03131d;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 15px 35px rgba(40,224,194,.25);
}

.secondary {
    padding: 14px 24px;
    margin-left: 10px;
    border-radius: 14px;
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.12);
    color: white;
    cursor: pointer;
}

/* 3D MEDICAL OBJECT */

.medical-orb {
    width: 330px;
    height: 330px;

    border-radius: 50%;

    display: flex;
    justify-content: center;
    align-items: center;

    background:
        radial-gradient(circle at 35% 30%, #ffffff, #28e0c2 20%, #126d89 55%, #06121d 75%);

    box-shadow:
        0 0 50px rgba(40,224,194,.3),
        inset -30px -30px 50px rgba(0,0,0,.45);

    animation: float 5s ease-in-out infinite;

    position: relative;
}

.medical-orb::before {
    content: "✚";
    font-size: 130px;
    color: white;
    text-shadow: 0 0 30px #28e0c2;
}

.medical-orb::after {
    content: "";
    position: absolute;
    width: 380px;
    height: 380px;
    border: 1px solid rgba(40,224,194,.4);
    border-radius: 50%;
    animation: rotate 12s linear infinite;
}

@keyframes float {
    50% {
        transform: translateY(-20px) rotateY(15deg);
    }
}

@keyframes rotate {
    to {
        transform: rotate(360deg);
    }
}

/* DASHBOARD */

.dashboard {
    padding: 30px 7%;
}

.section-title {
    font-size: 32px;
    margin-bottom: 10px;
}

.section-subtitle {
    color: #8ea7b5;
    margin-bottom: 30px;
}

.stats {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 20px;
}

.stat {
    padding: 25px;

    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.1);

    border-radius: 22px;

    transform-style: preserve-3d;
    transition: .3s;

    box-shadow: 0 20px 40px rgba(0,0,0,.18);
}

.stat:hover {
    transform: translateY(-8px) rotateX(5deg) rotateY(-5deg);
}

.stat-icon {
    font-size: 35px;
}

.stat-number {
    font-size: 30px;
    font-weight: bold;
    margin-top: 15px;
}

.stat-label {
    color: #91aab8;
    margin-top: 5px;
}

/* SERVICES */

.services {
    padding: 70px 7%;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 25px;
}

.card {

    padding: 30px;

    min-height: 230px;

    border-radius: 25px;

    background:
        linear-gradient(145deg,
        rgba(255,255,255,.09),
        rgba(255,255,255,.025));

    border: 1px solid rgba(255,255,255,.1);

    box-shadow:
        0 20px 45px rgba(0,0,0,.25);

    transition: .35s;

    transform-style: preserve-3d;
}

.card:hover {
    transform:
        perspective(900px)
        rotateX(6deg)
        rotateY(-7deg)
        translateY(-10px);

    border-color: rgba(40,224,194,.6);
}

.card-icon {
    font-size: 50px;
    margin-bottom: 20px;
}

.card h3 {
    font-size: 23px;
    margin-bottom: 10px;
}

.card p {
    color: #91aab8;
    line-height: 1.5;
}

.card button {
    margin-top: 20px;
    padding: 11px 18px;
    border: none;
    border-radius: 10px;
    background: #28e0c2;
    cursor: pointer;
    font-weight: bold;
}

/* CONTENT */

.content {
    padding: 40px 7%;
}

.panel {

    display: none;

    background: rgba(255,255,255,.05);

    border: 1px solid rgba(255,255,255,.1);

    border-radius: 25px;

    padding: 30px;

    margin-bottom: 50px;

    animation: appear .4s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.panel.active {
    display: block;
}

.item-grid {
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 18px;
    margin-top: 25px;
}

.item {

    background: rgba(0,0,0,.18);

    border-radius: 18px;

    padding: 20px;

    border: 1px solid rgba(255,255,255,.08);
}

.item h3 {
    margin-bottom: 7px;
}

.item p {
    color: #91aab8;
    margin: 5px 0;
}

.price {
    color: #28e0c2;
    font-weight: bold;
    font-size: 20px;
}

.book-btn {
    margin-top: 15px;

    padding: 10px 18px;

    border-radius: 10px;

    border: none;

    background: #28e0c2;

    cursor: pointer;
}

/* EMERGENCY */

.emergency {

    margin: 30px 7% 80px;

    padding: 35px;

    border-radius: 25px;

    background:
        linear-gradient(
        135deg,
        rgba(255,70,70,.15),
        rgba(255,70,70,.03)
        );

    border: 1px solid rgba(255,70,70,.25);
}

.emergency h2 {
    color: #ff7070;
}

.emergency button {
    margin-top: 20px;
    padding: 13px 25px;
    border-radius: 12px;
    border: none;
    background: #ff5555;
    color: white;
    font-weight: bold;
    cursor: pointer;
}

/* MODAL */

.modal {

    display: none;

    position: fixed;

    inset: 0;

    z-index: 500;

    background: rgba(0,0,0,.75);

    justify-content: center;
    align-items: center;

    padding: 20px;
}

.modal-box {

    width: min(500px,100%);

    padding: 30px;

    border-radius: 25px;

    background: #0b2232;

    border: 1px solid rgba(40,224,194,.3);

    box-shadow: 0 30px 80px rgba(0,0,0,.5);
}

.modal input,
.modal select {

    width: 100%;

    padding: 13px;

    margin-top: 12px;

    border-radius: 10px;

    border: 1px solid #294354;

    background: #071824;

    color: white;
}

.modal-actions {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

.close {
    background: #334652 !important;
    color: white;
}

/* TOAST */

.toast {

    position: fixed;

    bottom: 25px;

    right: 25px;

    padding: 16px 22px;

    background: #102f3e;

    border: 1px solid #28e0c2;

    border-radius: 14px;

    display: none;

    z-index: 1000;

    box-shadow: 0 15px 40px rgba(0,0,0,.4);
}

/* RESPONSIVE */

@media(max-width:900px) {

    .hero {
        flex-direction: column;
        text-align: center;
    }

    .stats {
        grid-template-columns: repeat(2,1fr);
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .item-grid {
        grid-template-columns: 1fr;
    }
}

@media(max-width:500px) {

    .stats {
        grid-template-columns: 1fr;
    }

    .medical-orb {
        width: 250px;
        height: 250px;
    }

}

</style>

</head>

<body>

<!-- NAVBAR -->

<nav>

<div class="logo">
Medi<span>Sphere</span> 3D
</div>

<div>

<button onclick="showSection('doctors')">Doctors</button>
<button onclick="showSection('medicines')">Medicines</button>
<button onclick="showSection('beds')">Beds</button>
<button onclick="showSection('dashboard')">Dashboard</button>

</div>

</nav>


<!-- HERO -->

<section class="hero">

<div class="hero-text">

<h1>
Your Complete
<span>Healthcare</span>
Platform
</h1>

<p>
Book doctors, find medicines and reserve hospital beds
through one simple healthcare platform.
</p>

<div class="hero-buttons">

<button class="primary"
onclick="showSection('doctors')">
Book Doctor
</button>

<button class="secondary"
onclick="showSection('beds')">
Find Hospital Bed
</button>

</div>

</div>


<div class="medical-orb"></div>

</section>


<!-- DASHBOARD -->

<section class="dashboard" id="dashboard">

<h2 class="section-title">
Healthcare Dashboard
</h2>

<p class="section-subtitle">
Real-time demo availability
</p>

<div class="stats">

<div class="stat">
<div class="stat-icon">👨‍⚕️</div>
<div class="stat-number">128+</div>
<div class="stat-label">Doctors</div>
</div>

<div class="stat">
<div class="stat-icon">🏥</div>
<div class="stat-number">24</div>
<div class="stat-label">Hospitals</div>
</div>

<div class="stat">
<div class="stat-icon">🛏️</div>
<div class="stat-number">84</div>
<div class="stat-label">Available Beds</div>
</div>

<div class="stat">
<div class="stat-icon">💊</div>
<div class="stat-number">1,240+</div>
<div class="stat-label">Medicines</div>
</div>

</div>

</section>


<!-- SERVICES -->

<section class="services">

<h2 class="section-title">
Healthcare Services
</h2>

<p class="section-subtitle">
Everything you need in one place.
</p>

<div class="cards">

<div class="card">

<div class="card-icon">👨‍⚕️</div>

<h3>Doctor Appointment</h3>

<p>
Find doctors by speciality and book an appointment.
</p>

<button onclick="showSection('doctors')">
Find Doctor
</button>

</div>


<div class="card">

<div class="card-icon">💊</div>

<h3>Medicines</h3>

<p>
Browse medicines and create a demo medicine order.
</p>

<button onclick="showSection('medicines')">
Browse Medicines
</button>

</div>


<div class="card">

<div class="card-icon">🛏️</div>

<h3>Hospital Beds</h3>

<p>
Check hospital bed availability and reserve a bed.
</p>

<button onclick="showSection('beds')">
Find Bed
</button>

</div>

</div>

</section>


<!-- CONTENT -->

<section class="content">


<!-- DOCTORS -->

<div class="panel" id="doctors">

<h2>👨‍⚕️ Find a Doctor</h2>

<p class="section-subtitle">
Select a doctor to book an appointment.
</p>

<div class="item-grid">

{% for doctor in doctors %}

<div class="item">

<h3>{{ doctor.name }}</h3>

<p>🩺 {{ doctor.speciality }}</p>

<p>🏥 {{ doctor.hospital }}</p>

<p>⭐ {{ doctor.rating }} | {{ doctor.experience }}</p>

<p class="price">
₹{{ doctor.fee }}
</p>

<button class="book-btn"
onclick="openDoctor('{{ doctor.name }}')">
Book Appointment
</button>

</div>

{% endfor %}

</div>

</div>


<!-- MEDICINES -->

<div class="panel" id="medicines">

<h2>💊 Medicine Store</h2>

<p class="section-subtitle">
Select a medicine to add it to your demo order.
</p>

<div class="item-grid">

{% for medicine in medicines %}

<div class="item">

<h3>{{ medicine.name }}</h3>

<p>Category: {{ medicine.category }}</p>

<p class="price">
₹{{ medicine.price }}
</p>

<button class="book-btn"
onclick="orderMedicine('{{ medicine.name }}')">
Add to Order
</button>

</div>

{% endfor %}

</div>

</div>


<!-- BEDS -->

<div class="panel" id="beds">

<h2>🛏️ Hospital Bed Availability</h2>

<p class="section-subtitle">
Check available beds at nearby hospitals.
</p>

<div class="item-grid">

{% for hospital in hospitals %}

<div class="item">

<h3>{{ hospital.name }}</h3>

<p>📍 {{ hospital.location }}</p>

<p>
🛏️ Available Beds:
<strong>{{ hospital.beds }}</strong>
</p>

<p>
🚑 ICU Beds:
<strong>{{ hospital.icu }}</strong>
</p>

<p>
Emergency:
{% if hospital.emergency %}
<span style="color:#28e0c2">Available</span>
{% else %}
<span style="color:#ff7070">Limited</span>
{% endif %}
</p>

<button class="book-btn"
onclick="bookBed('{{ hospital.name }}')">
Reserve Bed
</button>

</div>

{% endfor %}

</div>

</div>


</section>


<!-- EMERGENCY -->

<section class="emergency">

<h2>🚨 Emergency Healthcare</h2>

<p style="margin-top:10px;color:#b8cbd5">
For a real emergency, contact your local emergency service
or visit the nearest emergency department.
</p>

<button onclick="emergencyAlert()">
Emergency Assistance
</button>

</section>


<!-- MODAL -->

<div class="modal" id="modal">

<div class="modal-box">

<h2 id="modalTitle">
Booking
</h2>

<div id="modalContent">

<input id="patientName"
placeholder="Patient Name">

<input id="phone"
placeholder="Phone Number">

<select id="time">

<option>10:00 AM</option>
<option>11:30 AM</option>
<option>1:00 PM</option>
<option>3:30 PM</option>
<option>5:00 PM</option>

</select>

</div>

<div class="modal-actions">

<button class="primary"
onclick="confirmBooking()">
Confirm
</button>

<button class="secondary close"
onclick="closeModal()">
Cancel
</button>

</div>

</div>

</div>


<div class="toast" id="toast"></div>


<script>

/* -------------------------------------------------
   SOUND ENGINE
   Creates simple sound effects without external files
-------------------------------------------------- */

let audioContext;

function sound(type="click") {

    if (!audioContext) {
        audioContext =
            new (window.AudioContext ||
            window.webkitAudioContext)();
    }

    const oscillator =
        audioContext.createOscillator();

    const gain =
        audioContext.createGain();

    oscillator.connect(gain);
    gain.connect(audioContext.destination);

    if(type === "success") {
        oscillator.frequency.value = 700;
    }
    else if(type === "error") {
        oscillator.frequency.value = 180;
    }
    else {
        oscillator.frequency.value = 450;
    }

    gain.gain.setValueAtTime(
        0.08,
        audioContext.currentTime
    );

    gain.gain.exponentialRampToValueAtTime(
        0.001,
        audioContext.currentTime + 0.18
    );

    oscillator.start();

    oscillator.stop(
        audioContext.currentTime + 0.18
    );
}


/* -------------------------------------------------
   NAVIGATION
-------------------------------------------------- */

function showSection(id) {

    sound();

    document
        .querySelectorAll(".panel")
        .forEach(panel => {
            panel.classList.remove("active");
        });

    const section =
        document.getElementById(id);

    if(section && section.classList.contains("panel")) {
        section.classList.add("active");

        section.scrollIntoView({
            behavior:"smooth",
            block:"start"
        });
    }
    else {
        document.getElementById(id)
            ?.scrollIntoView({
                behavior:"smooth"
            });
    }
}


/* -------------------------------------------------
   MODAL
-------------------------------------------------- */

let currentType = "";
let currentItem = "";

function openDoctor(name) {

    sound();

    currentType = "doctor";
    currentItem = name;

    document.getElementById("modalTitle")
        .innerText =
        "Book Appointment - " + name;

    document.getElementById("modal")
        .style.display = "flex";
}


function bookBed(hospital) {

    sound();

    currentType = "bed";
    currentItem = hospital;

    document.getElementById("modalTitle")
        .innerText =
        "Reserve Bed - " + hospital;

    document.getElementById("modal")
        .style.display = "flex";
}


function closeModal() {

    document.getElementById("modal")
        .style.display = "none";
}


function confirmBooking() {

    const name =
        document.getElementById("patientName").value;

    const phone =
        document.getElementById("phone").value;

    const time =
        document.getElementById("time").value;

    if(!name || !phone) {

        sound("error");

        showToast(
            "Please enter patient name and phone."
        );

        return;
    }

    fetch("/book", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({

            type: currentType,
            item: currentItem,
            patient: name,
            phone: phone,
            time: time

        })

    })
    .then(response => response.json())
    .then(data => {

        sound("success");

        closeModal();

        showToast(
            "✓ " + data.message
        );

    });

}


/* -------------------------------------------------
   MEDICINE
-------------------------------------------------- */

function orderMedicine(name) {

    sound();

    fetch("/medicine", {

        method:"POST",

        headers:{
            "Content-Type":
            "application/json"
        },

        body:JSON.stringify({
            medicine:name
        })

    })
    .then(response => response.json())
    .then(data => {

        sound("success");

        showToast(
            "💊 " + data.message
        );

    });

}


/* -------------------------------------------------
   EMERGENCY
-------------------------------------------------- */

function emergencyAlert() {

    sound("error");

    showToast(
        "🚨 Demo emergency alert activated."
    );

}


/* -------------------------------------------------
   TOAST
-------------------------------------------------- */

function showToast(message) {

    const toast =
        document.getElementById("toast");

    toast.innerText = message;

    toast.style.display = "block";

    setTimeout(() => {

        toast.style.display = "none";

    }, 3500);

}

</script>

</body>

</html>
"""


# ---------------------------------------------------------
# ROUTES
# ---------------------------------------------------------

@app.route("/")
def home():

    return render_template_string(
        HTML,
        doctors=doctors,
        medicines=medicines,
        hospitals=hospitals
    )


@app.route("/book", methods=["POST"])
def book():

    data = request.get_json()

    booking_id = random.randint(10000, 99999)

    bookings.append({
        "id": booking_id,
        "type": data.get("type"),
        "item": data.get("item"),
        "patient": data.get("patient"),
        "phone": data.get("phone"),
        "time": data.get("time"),
        "created": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    if data.get("type") == "doctor":

        message = (
            f"Appointment booked with "
            f"{data.get('item')} at {data.get('time')}. "
            f"Booking ID: #{booking_id}"
        )

    else:

        message = (
            f"Bed reserved at "
            f"{data.get('item')}. "
            f"Booking ID: #{booking_id}"
        )

    return jsonify({
        "success": True,
        "message": message
    })


@app.route("/medicine", methods=["POST"])
def medicine():

    data = request.get_json()

    medicine_name = data.get("medicine")

    order_id = random.randint(10000, 99999)

    bookings.append({
        "id": order_id,
        "type": "medicine",
        "item": medicine_name,
        "created": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    return jsonify({
        "success": True,
        "message":
            f"{medicine_name} added to your order. "
            f"Order ID: #{order_id}"
    })


@app.route("/api/bookings")
def get_bookings():

    return jsonify(bookings)


# ---------------------------------------------------------
# RUN
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\n====================================")
    print("      MEDISPHERE 3D HEALTHCARE")
    print("====================================")
    print("Website: http://127.0.0.1:5000")
    print("====================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
