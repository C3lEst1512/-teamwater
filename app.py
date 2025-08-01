from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TILTIFY_GRAPHQL_URL = "https://api.tiltify.com/"
DEFAULT_FACT_ID = "0478358a-c4ff-4ab0-9cc7-5f0b328df9dc"

# --------- Leaderboard Endpoint ---------
def fetch_leaderboard(limit=5, fact_id=DEFAULT_FACT_ID):
    graphql_query = """
    query get_fact_donor_leaderboard($id: ID!, $limit: Int) {
      fact(id: $id) {
        donorLeaderboard(range: "default") {
          entries(first: $limit) {
            edges {
              node {
                id
                name
                amount { value currency }
                latestComment
                avatar { src alt }
              }
            }
          }
        }
      }
    }
    """
    payload = {
        "operationName": "get_fact_donor_leaderboard",
        "variables": {"id": fact_id, "limit": limit},
        "query": graphql_query,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(TILTIFY_GRAPHQL_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    edges = (
        data.get("data", {})
        .get("fact", {})
        .get("donorLeaderboard", {})
        .get("entries", {})
        .get("edges", [])
    )
    processed = []
    for edge in edges:
        node = edge["node"]
        processed.append(
            {
                "id": node["id"],
                "name": node["name"],
                "amount": float(node["amount"]["value"]),
                "currency": node["amount"]["currency"],
                "comment": node["latestComment"],
                "avatar": node["avatar"]["src"],
            }
        )
    return processed

@app.route("/leaderboard")
def leaderboard():
    try:
        limit = int(request.args.get("limit", 5))
    except ValueError:
        limit = 5
    fact_id = request.args.get("fact_id", DEFAULT_FACT_ID)
    try:
        donors = fetch_leaderboard(limit=limit, fact_id=fact_id)
        return jsonify(donors)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------- Latest Donations Endpoint ---------
def fetch_latest_donations(limit=10, fact_id=DEFAULT_FACT_ID):
    graphql_query = """
    query get_latest_fact_donations_($id: ID!, $limit: Int) {
      fact(id: $id) {
        donations(first: $limit) {
          edges {
            node {
              id
              donorName
              donorComment
              completedAt
              amount { value currency }
              fact {
                id
                link
                ownership { id name }
              }
            }
          }
        }
      }
    }
    """
    payload = {
        "operationName": "get_latest_fact_donations_",
        "variables": {"id": fact_id, "limit": limit},
        "query": graphql_query,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(TILTIFY_GRAPHQL_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    edges = (
        data.get("data", {})
        .get("fact", {})
        .get("donations", {})
        .get("edges", [])
    )
    donations = []
    for edge in edges:
        node = edge["node"]
        donations.append(
            {
                "id": node["id"],
                "donor_name": node.get("donorName"),
                "donor_comment": node.get("donorComment"),
                "amount": float(node["amount"]["value"]),
                "currency": node["amount"]["currency"],
                "completed_at": node["completedAt"],
                "fact_link": node["fact"]["link"],
                "ownership": node["fact"]["ownership"]["name"],
            }
        )
    return donations

@app.route("/donations")
def donations():
    try:
        limit = int(request.args.get("limit", 10))
    except ValueError:
        limit = 10
    fact_id = request.args.get("fact_id", DEFAULT_FACT_ID)
    try:
        donations = fetch_latest_donations(limit=limit, fact_id=fact_id)
        return jsonify(donations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------- Total Amount Raised Endpoint ---------
def fetch_total_raised(fact_id=DEFAULT_FACT_ID):
    graphql_query = """
    query FactById($id: ID!) {
      fact(id: $id) {
        totalAmountRaised { value currency }
      }
    }
    """
    payload = {
        "operationName": "FactById",
        "variables": {"id": fact_id},
        "query": graphql_query,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(TILTIFY_GRAPHQL_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    amount = (
        data.get("data", {})
        .get("fact", {})
        .get("totalAmountRaised", {})
    )
    return amount

@app.route("/total_raised")
def total_raised():
    fact_id = request.args.get("fact_id", DEFAULT_FACT_ID)
    try:
        amount = fetch_total_raised(fact_id=fact_id)
        return jsonify({
            "total_raised": amount.get("value"),
            "currency": amount.get("currency")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
