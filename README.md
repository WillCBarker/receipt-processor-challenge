# Receipt-processor-challenge

This is a Django-based API for processing receipts and calculating points based on predefined rules provided in the challenge repo.

## Features

- **Process Receipts**: Submit a receipt in JSON format and get a unique ID.
- **Get Points**: Retrieve the points awarded to a receipt using its unique ID.

## Getting Started

1. Clone the repository:
    ```sh
    git clone https://github.com/WillCBarker/receipt-processor-challenge.git
    ```

2. Navigate to the `/receipt-processor-challenge/` directory

3. Build the image:
    ```sh
    docker build -t receipt-processor-challenge .
    ```

4. Run the container:
    ```sh
    docker run -p 8000:8000 receipt-processor-challenge
    ```

## Endpoints

### Process Receipts

- **URL**: `/receipts/process`
- **Method**: `POST`
- **Payload**: JSON containing receipt details
- **Response**: JSON object containing an ID for the processed receipt

### Get Points

- **URL**: `/receipts/{id}/points`
- **Method**: `GET`
- **Payload**: JSON object containing the number of points awarded
- **Response**: 404 if receipt ID is not found
