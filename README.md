# 🏥 MediSphere 3D – Integrated Healthcare Booking Platform

MediSphere 3D is a **3D-style healthcare web application prototype** built with Python and Flask. The platform provides a unified interface where users can explore healthcare services such as **doctor appointments, medicines, and hospital bed availability**.

The project focuses on creating a modern, interactive healthcare experience with animated 3D-style UI elements, responsive design, and browser-based sound effects.

> ⚠️ **Note:** This is an educational/demo prototype. It is not connected to real hospitals, doctors, pharmacies, payment systems, or medical databases.

---

## ✨ Features

### 👨‍⚕️ Doctor Appointment Booking

* Browse available doctors
* View doctor speciality
* Hospital information
* Experience and ratings
* Consultation fee
* Book a demo appointment
* Generate a booking ID

### 💊 Medicine Store

* Browse medicines
* View medicine categories
* Display prices
* Add medicines to a demo order
* Generate an order ID

### 🛏️ Hospital Bed Booking

* View hospitals
* Check available beds
* View ICU bed availability
* Check emergency service availability
* Reserve a demo hospital bed

### 📊 Healthcare Dashboard

* Doctor statistics
* Hospital statistics
* Available bed statistics
* Medicine statistics

### 🚨 Emergency Section

* Dedicated emergency assistance interface
* Demo emergency alert interaction

### 🔊 Sound Effects

The website uses the browser's **Web Audio API** to generate interface sounds for:

* Button clicks
* Successful bookings
* Errors
* Emergency interactions

No external audio files are required.

### 🎨 3D-Style Interface

* Animated medical orb
* Glassmorphism cards
* 3D hover effects
* Smooth animations
* Responsive layout
* Dark healthcare-themed interface

---

## 🛠️ Technologies Used

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| 🐍 Python     | Backend programming                 |
| 🌐 Flask      | Web framework                       |
| HTML5         | Website structure                   |
| CSS3          | UI, animations and 3D-style effects |
| JavaScript    | Frontend interactions               |
| Web Audio API | Sound effects                       |
| JSON          | Frontend/backend data exchange      |

---

## 📂 Project Structure

```text
MediSphere-3D/
│
├── app.py
│
└── README.md
```

The current prototype is intentionally implemented in a **single Python file** for easy demonstration and learning.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/MediSphere-3D.git
```

### 2. Open the project

```bash
cd MediSphere-3D
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```text
http://127.0.0.1:5000
```

---

## 🖥️ How It Works

The application follows a simple architecture:

```text
              USER
                │
                ▼
        ┌─────────────────┐
        │ MediSphere 3D   │
        │   Web Interface │
        └────────┬────────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
   👨‍⚕️ Doctor   💊 Medicine   🛏️ Hospital
    Booking      Order        Bed
       │         │             │
       └─────────┼─────────────┘
                 ▼
          Flask Backend
                 │
                 ▼
        Demo Booking Data
```

---

## 🔄 Booking Flow

### Doctor

```text
Select Doctor
      ↓
Enter Patient Details
      ↓
Select Appointment Time
      ↓
Confirm Booking
      ↓
Booking ID Generated
```

### Medicine

```text
Select Medicine
      ↓
Add to Order
      ↓
Order ID Generated
```

### Hospital Bed

```text
Select Hospital
      ↓
Check Bed Availability
      ↓
Enter Patient Details
      ↓
Reserve Bed
      ↓
Booking ID Generated
```

---

## 🔊 Sound System

MediSphere 3D uses the browser's **Web Audio API** instead of requiring external sound files.

Example interactions include:

```text
Button Click     → Short UI Sound
Successful Action → Success Sound
Invalid Input     → Error Sound
Emergency Button  → Alert Sound
```

This keeps the project lightweight and avoids additional audio assets.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Create a centralized healthcare service interface
* Demonstrate doctor appointment booking
* Demonstrate medicine ordering
* Demonstrate hospital bed reservation
* Build an interactive 3D-style healthcare UI
* Learn Flask-based web development
* Implement frontend/backend communication
* Add interactive sound effects
* Create a foundation for a larger healthcare platform

---

## 🚀 Future Improvements

The current project is a prototype and can be extended with:

* 🔐 User authentication
* 👨‍⚕️ Doctor accounts
* 🏥 Hospital administrator accounts
* 🗄️ MySQL/PostgreSQL database
* 📅 Real appointment scheduling
* 💳 Payment gateway integration
* 💊 Shopping cart and checkout
* 📍 Hospital location/map integration
* 🛏️ Interactive 3D hospital-bed visualization
* 📊 Advanced healthcare analytics
* 🤖 AI-based symptom/triage assistant
* 📱 Progressive Web App support
* ☁️ Cloud deployment
* 🔒 Role-based access control
* 🏥 ABDM/FHIR-compatible architecture for a future production implementation

---

## 📌 Current Limitations

This version is designed for **education, demonstration and portfolio purposes**.

It currently does **not** provide:

* Real doctor appointments
* Real medicine delivery
* Real hospital reservations
* Real payment processing
* Real patient medical records
* Real-time hospital availability
* Production-grade authentication
* Permanent database storage

Booking information is stored temporarily in application memory and is lost when the server restarts.

---

## 📚 Learning Outcomes

Through this project, I explored:

* Python Flask development
* Web application architecture
* REST-style API endpoints
* HTML/CSS/JavaScript integration
* Responsive UI design
* 3D-style CSS transformations
* Browser Web Audio API
* JSON-based frontend/backend communication
* Healthcare technology concepts
* Building a complete prototype from a single Python file

---

## 👨‍💻 Author

**Rehan Raza**

B.Tech Biomedical Engineering
Vidyalankar Institute of Technology

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐ on GitHub.

---

## ⚠️ Disclaimer

MediSphere 3D is an **educational software prototype** created for learning, portfolio and demonstration purposes.

It should not be used to make medical, emergency, prescription, treatment, hospital admission, or healthcare purchasing decisions.
