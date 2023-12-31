# Supabase DB Testing App

This is a sample FastAPI project that demonstrates how to use Supabase DB.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.7 or above

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rp4ri/supabasedb-testing-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd supabasedb-testing-app
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a Supabase project and obtain the API URL and API Key.

2. Create a `.env` file in the project root directory and add the following environment variables:

   ```plaintext
   SUPABASE_URL=<your-supabase-api-url>
   SUPABASE_KEY=<your-supabase-api-key>
   ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://localhost:8000` to access the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
