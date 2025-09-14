
## Vulnerability Detection Agent for STRIDE-Based Architectures

![stride](assets/stride.png)
---
This project is a complete solution for threat analysis based on the STRIDE methodology, consisting of a FastAPI (Python) backend and an HTML/CSS/JS frontend with threat visualization using Cytoscape.js.

---

## Features

* Upload of an architecture image and system information input.
* Automatic generation of a STRIDE threat model using Azure OpenAI.
* Interactive graph visualization of the threat model (Cytoscape.js).
* Improvement suggestions for the threat model.
* Button to print/export the generated graph.

## How to Run the Project

### 1. Prerequisites

* Python 3.10+
* Node.js (optional, only if you want to serve the frontend with a local server)
* An Azure OpenAI account and configured deployment (see environment variables)

### 2. Cloning the Repository

```bash
# Clone the project
git clone https://github.com/hanielrolemberg/stride-threat-model-azure.git
```

### 3. Setting up the Backend (FastAPI)

Access the backend folder:

```bash
cd src
```

Create and activate a virtual environment (optional, but recommended):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with the following variables (fill in with your Azure OpenAI data):

```
AZURE_OPENAI_API_KEY=xxxxxx
AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-05-15
AZURE_OPENAI_DEPLOYMENT_NAME=<deployment-name>
```

Run the backend:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

The backend will be available at: [http://localhost:8001](http://localhost:8001)

### 4. Setting up the Frontend

Access the frontend folder:


Simply open the `index.html` file in your browser (double-click or `open index.html`).

If you want to serve it via a local server (optional):

```bash
npx serve .
# or
python -m http.server 8080
```

The frontend expects the backend to be running at [http://localhost:8001](http://localhost:8001).

## Notes and Tips

* **Azure OpenAI**: Make sure your deployment is active and the `.env` variables are correct.
* **CORS**: The backend is already configured to accept requests from any origin, but if you use it in production, adjust the allowed origins.
* **Token limit**: The Azure OpenAI model may have token limits. Adjust `max_tokens` if needed.
* **Graph printing**: The “Print Graph” button exports the current graph view as an image for printing or PDF.
* **JSON format**: The frontend expects the JSON in the format returned by the backend. If you change the backend, adjust the frontend accordingly.
* **Ports**: Make sure ports `8001` (backend) and `8080` (frontend, if using a server) are available.

## Project Structure

```
stride-threat-model-azure/
│
|─── index.html 
|
|── src/
│   ├── main.py
│   ├── requirements.txt
│   └── .env 
│── assets/
│   └── stride.png
|── readme.md
│
└── .gitignore
```

