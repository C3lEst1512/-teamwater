# TeamWater Flask API

A Flask-based REST API that provides access to Tiltify donation data through GraphQL queries. This application fetches leaderboard data, latest donations, and total amount raised for fundraising campaigns.

## Features

- **Leaderboard Endpoint**: Get top donors for a campaign
- **Latest Donations Endpoint**: Retrieve recent donation activity
- **Total Raised Endpoint**: Get the total amount raised for a campaign
- **Configurable Campaign ID**: Support for multiple fundraising campaigns
- **Error Handling**: Graceful error responses with proper HTTP status codes

## API Endpoints

### 1. Leaderboard

**Endpoint**: `GET /leaderboard`

**Description**: Retrieves the top donors for a specific fundraising campaign.

**Query Parameters**:
- `limit` (optional): Number of donors to return (default: 5, max: configurable)
- `fact_id` (optional): Campaign ID (default: "0478358a-c4ff-4ab0-9cc7-5f0b328df9dc")

**Example Request**:
```
GET /leaderboard?limit=10&fact_id=your-campaign-id
```

**Example Response**:
```json
[
  {
    "id": "donor-id",
    "name": "Donor Name",
    "amount": 100.0,
    "currency": "USD",
    "comment": "Great cause!",
    "avatar": "https://example.com/avatar.jpg"
  }
]
```

### 2. Latest Donations

**Endpoint**: `GET /donations`

**Description**: Retrieves the most recent donations for a campaign.

**Query Parameters**:
- `limit` (optional): Number of donations to return (default: 10)
- `fact_id` (optional): Campaign ID (default: "0478358a-c4ff-4ab0-9cc7-5f0b328df9dc")

**Example Request**:
```
GET /donations?limit=20&fact_id=your-campaign-id
```

**Example Response**:
```json
[
  {
    "id": "donation-id",
    "donor_name": "Donor Name",
    "donor_comment": "Supporting the cause!",
    "amount": 50.0,
    "currency": "USD",
    "completed_at": "2024-01-15T10:30:00Z",
    "fact_link": "https://tiltify.com/campaign-link",
    "ownership": "Campaign Owner"
  }
]
```

### 3. Total Amount Raised

**Endpoint**: `GET /total_raised`

**Description**: Gets the total amount raised for a specific campaign.

**Query Parameters**:
- `fact_id` (optional): Campaign ID (default: "0478358a-c4ff-4ab0-9cc7-5f0b328df9dc")

**Example Request**:
```
GET /total_raised?fact_id=your-campaign-id
```

**Example Response**:
```json
{
  "total_raised": "1500.00",
  "currency": "USD"
}
```

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install flask requests
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

The server will start on `http://localhost:5000` with debug mode enabled.

### Environment Configuration

The application uses the following default configuration:
- **Tiltify GraphQL URL**: `https://api.tiltify.com/`
- **Default Campaign ID**: `0478358a-c4ff-4ab0-9cc7-5f0b328df9dc`
- **Server Port**: 5000

## Usage Examples

### Using curl

```bash
# Get top 5 donors
curl http://localhost:5000/leaderboard

# Get latest 10 donations
curl http://localhost:5000/donations

# Get total amount raised
curl http://localhost:5000/total_raised

# Get top 10 donors for a specific campaign
curl "http://localhost:5000/leaderboard?limit=10&fact_id=your-campaign-id"
```

### Using JavaScript/Fetch

```javascript
// Get leaderboard
fetch('http://localhost:5000/leaderboard?limit=5')
  .then(response => response.json())
  .then(data => console.log(data));

// Get latest donations
fetch('http://localhost:5000/donations?limit=10')
  .then(response => response.json())
  .then(data => console.log(data));

// Get total raised
fetch('http://localhost:5000/total_raised')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- **200**: Successful response
- **500**: Server error (with error details in response body)

Example error response:
```json
{
  "error": "Failed to fetch data from Tiltify API"
}
```

## Technical Details

- **Framework**: Flask
- **HTTP Client**: requests library
- **Data Format**: JSON
- **API Type**: RESTful
- **Backend**: Tiltify GraphQL API

## Development

### Project Structure

```
teamwater/
├── app.py          # Main Flask application
├── donations.py    # Donation-related functionality
├── latest.py       # Latest donations functionality
├── leaderboard.py  # Leaderboard functionality
└── README.md       # This file
```

### Adding New Endpoints

To add new endpoints, follow the pattern established in the code:

1. Create a GraphQL query function
2. Add a Flask route handler
3. Include proper error handling
4. Document the endpoint in this README

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For issues or questions, please create an issue in the repository or contact the development team.
