# 🧭 Location-Based Property Search API

This is a Flask-based backend service built for *Moustache Escapes* to help their tele-calling team find the nearest available property based on user input (which may include spelling mistakes or partial information).

The service takes a location query, geocodes it using the Mapbox API, and returns a list of Moustache properties within a 50 km radius.

---

## 🚀 Features

- ✅ Real-time geolocation search
- ✅ Handles small typos or misspellings in input
- ✅ Uses the Haversine formula for accurate distance calculations
- ✅ Mapbox-powered geocoding
- ✅ Returns properties within 50 km radius
- ✅ Response time under 2 seconds

---

## 🧪 Example Use Case

*Input:*
json
{
  "address": "delih"
}


*Output:*
json
{
  "inputLocation": {
    "lat": 28.61,
    "lng": 77.28
  },
  "nearbyLocations": [
    {
      "property": "Moustache Delhi",
      "latitude": 28.61257139,
      "longitude": 77.28423582
    }
  ]
}


---

## 🛠 Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/swayamprakash07/Moustachescapes-Assignment.git


### 2. Create a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


### 3. Install Dependencies
bash
pip install -r requirements.txt


### 4. Add Your .env File
Create a .env file in the root directory:

env
MAPBOX_API_KEY=your_mapbox_access_token_here


---

## ▶ Running the Server

bash
python main.py


The API will be live at:  
**http://localhost:3000/geocode**

---

## 📦 Project Structure


.
├── data.py               # List of Moustache property locations
├── main.py               # Main Flask app with geocoding API
├── requirements.txt      # Python dependencies
├── .env                  # Environment file (not committed)
└── README.md             # You are here


---

## 🧠 How It Works

1. Telecaller types a location (with or without typos).
2. API sends this to Mapbox to get latitude and longitude.
3. The API calculates distances from that point to all properties using the Haversine formula.
4. Any properties within a 50 km radius are returned.

---

## 📌 Requirements

- Python 3.7+
- Mapbox API Key (free account available)

---

## 🛡 Security Notes

- Never commit your .env file!
- Always add .env to your .gitignore.

---

## 👥 Contributors

- [Your Name](https://github.com/your-username)

---

## 📄 License

MIT License — free to use, share, and modify.

---

> Built with ❤ for Formi's SDE Assignment — powered by Flask + Mapbox