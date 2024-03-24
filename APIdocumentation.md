# Event Management System API Documentation

## Data Creation API

### Endpoint: `/event/`

- **Method**: POST
- **Description**: This endpoint allows users to add events to the system using the details provided in the request body.
- **Request Body**:
  - `event_name` (string): Name of the event.
  - `city_name` (string): Name of the city where the event is located.
  - `date` (string): Date of the event (format: YYYY-MM-DD).
  - `time` (string): Time of the event (format: HH:MM:SS).
  - `latitude` (float): Latitude coordinate of the event location.
  - `longitude` (float): Longitude coordinate of the event location.
- **Response**:
  - If the event is successfully created, returns the details of the created event along with a status code 201 (Created).
  - If there are any validation errors in the request body, returns an error response with a status code 400 (Bad Request).

## Event Finder API

### Endpoint: `/events/find/`

- **Method**: GET
- **Description**: This endpoint lists all events based on the user's latitude, longitude, and specified date. The system returns events occurring within the next 14 days from the specified date.
- **Query Parameters**:
  - `latitude` (float): Latitude coordinate of the user's location.
  - `longitude` (float): Longitude coordinate of the user's location.
  - `date` (string): Date for finding events (format: YYYY-MM-DD).
- **Response**:
  - Returns a list of events sorted by the earliest event after the specified date.
  - Each event in the response includes the following details:
    - `event_name` (string): Name of the event.
    - `city_name` (string): Name of the city where the event is located.
    - `date` (string): Date of the event.
    - `weather` (string): Weather conditions for the event.
    - `distance_km` (float): Distance from the user's location to the event location in kilometers.
  - The response also includes pagination details such as `page`, `pageSize`, `totalEvents`, and `totalPages`.

