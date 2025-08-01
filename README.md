# TeamWater Donations API Proxy

This is a simple Python Flask application that proxies and exposes TeamWater/Tiltify donation-related data through custom JSON REST API endpoints.

It fetches data from the official Tiltify GraphQL API and provides easy-to-use endpoints for:

- **Donor Leaderboard** (`/leaderboard`)  
- **Latest Donations** (`/donations`)  
- **Total Amount Raised** (`/total_raised`)  

---

## Features

- Fetch donor leaderboard data with configurable limit
- Fetch latest donation entries with pagination support
- Retrieve total amount raised for a specific fundraising campaign (fact ID)
- Uses GraphQL queries to communicate with Tiltify API
- Simple JSON output for easy integration with frontends or other services
- Accepts optional query parameters for `limit` and `fact_id`

---

## Prerequisites

- Python 3.6+
- [Flask](https://flask.palletsprojects.com/)
- [requests](https://docs.python-requests.org/)

---

## Installation

1. Clone or download this repository or save the Flask app script (`app.py`) to your machine.

2. Create and activate a Python virtual environment (optional but recommended):

    ```
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies via pip:

    ```
    pip install flask requests
    ```

---

## Usage

1. Run the Flask app:

    ```
    python app.py
    ```

2. The server will start on port 5000 by default.

3. Access the API endpoints via your browser, curl, or any HTTP client:

    - **Donor Leaderboard**  
      Retrieve top donors  
      `GET http://localhost:5000/leaderboard?limit=10&fact_id=YOUR_FACT_ID`

    - **Latest Donations**  
      Retrieve recent donations  
      `GET http://localhost:5000/donations?limit=20&fact_id=YOUR_FACT_ID`

    - **Total Amount Raised**  
      Get total funds raised  
      `GET http://localhost:5000/total_raised?fact_id=YOUR_FACT_ID`

   > If `fact_id` is omitted, the default fundraising event ID (`0478358a-c4ff-4ab0-9cc7-5f0b328df9dc`) will be used.

---

## Example Requests

curl "http://localhost:5000/leaderboard?limit=5"
curl "http://localhost:5000/donations?limit=10"
curl "http://localhost:5000/total_raised"

text

---

## Response Example

### `/leaderboard`

[
{
"id": "a0e76ed7-a39d-5e26-9b1c-22756fca0f36",
"name": "Shopify",
"amount": 500000,
"currency": "USD",
"comment": "For the Lorax - but wetter",
"avatar": "https://assets.tiltify.com/assets/default-avatar.png"
},
...
]

text

### `/donations`

[
{
"id": "55695045-aea4-4041-a16f-e6b1a867ea65",
"donor_name": "Aljosa Vukovic",
"donor_comment": "Thank you for keeping the planet ...",
"amount": 1.0,
"currency": "USD",
"completed_at": "2025-08-01T17:13:14.082470Z",
"fact_link": "https://tiltify.com/wateraid-america/teamwater",
"ownership": "WaterAid America"
},
...
]

text

### `/total_raised`

{
"total_raised": "707787.09",
"currency": "USD"
}

text

---

## Notes

- This app does **not** handle authentication. If the upstream API endpoints require API keys or tokens in the future, update the headers accordingly.
- For production usage, consider running the Flask app behind a production server (e.g., Gunicorn, uWSGI) and add proper error handling, logging, and caching.
- Feel free to extend this app with additional endpoints or integrations!

---

## License

This project is provided "as is" without warranty. Use at your own risk.

---

## Contact

If you have any questions or need assistance, feel free to reach out!

---

Enjoy your TeamWater data API! 🚀
