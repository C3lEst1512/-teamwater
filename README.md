# 💧 TeamWater API Wrapper

A simple Flask application that fetches and exposes public Tiltify donation data for the [#TeamWater](https://teamwater.org) campaign — a historic effort to raise $40 million to provide clean water to two million people.

## 🌍 About #TeamWater

> #TeamWater will be the biggest and most impactful campaign for clean water in history. With thousands of the world's top Creators talking about water, we're changing the world, one drop at a time.

---

## 🚀 Features

This app provides three public API endpoints:

- `/leaderboard` – Returns top donors for the campaign.
- `/donations` – Returns the latest donations made to the campaign.
- `/total_raised` – Returns the total amount raised.

All data is fetched from the [Tiltify API](https://tiltify.com) using GraphQL queries.

---

## 📦 Requirements

- Python 3.7+
- `Flask`
- `requests`

### Install dependencies:

```bash
pip install Flask requests
```

---

## ⚙️ Running the App

```bash
python app.py
```

By default, the app will run on `http://localhost:5000`.

---

## 🔌 API Usage

### `/leaderboard`

**Query Parameters:**
- `limit`: *(optional)* number of donors to return (default: `5`)
- `fact_id`: *(optional)* Tiltify fact (campaign) ID

**Example:**

```http
GET /leaderboard?limit=10
```

---

### `/donations`

**Query Parameters:**
- `limit`: *(optional)* number of donations to return (default: `10`)
- `fact_id`: *(optional)* Tiltify fact (campaign) ID

**Example:**

```http
GET /donations?limit=5
```

---

### `/total_raised`

**Query Parameters:**
- `fact_id`: *(optional)* Tiltify fact (campaign) ID

**Example:**

```http
GET /total_raised
```

---

## 🔒 Notes

- The default campaign fact ID is: `0478358a-c4ff-4ab0-9cc7-5f0b328df9dc` (used if `fact_id` is not specified).
- This app uses the public Tiltify API, which does not require authentication for read-only data.

---

## ❤️ Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

MIT — feel free to use and adapt.
