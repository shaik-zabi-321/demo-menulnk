# MenuLink — AI Restaurant Ordering Assistant

MenuLink is a demo restaurant-ordering experience with a browser-based interface and a FastAPI backend. A customer can choose a sample restaurant and chat with an LLM-powered assistant to browse menu items, build a cart and proceed through a demo checkout flow.

## Features

- List sample restaurants and optionally filter them by city.
- Select a restaurant and reset the current demo cart.
- Chat with an assistant powered by Groq.
- Use tool calling to search menu items, add items to a cart and calculate the order total.
- Collect a delivery address before creating an order.
- Generate a demo UPI payment URI and print a restaurant notification.

## Tech Stack

- Python
- FastAPI and Uvicorn
- Groq API and tool calling
- HTML, CSS and JavaScript
- python-dotenv

## Project Structure

Key backend files include:

- `main.py` — FastAPI endpoints for listing restaurants, selecting a restaurant and chatting.
- `agent.py` — LLM conversation loop and ordered tool execution.
- `tools.py` — tool schemas supplied to the model.
- `handlers.py` — menu search, cart, total, order and notification handlers.
- `menu.py` — sample restaurant and menu data.
- `index.html` — browser interface.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/shaik-zabi-321/demo-menulnk.git
   cd demo-menulnk
   ```

2. Create and activate a Python virtual environment.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:

   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

5. Start the API:

   ```bash
   uvicorn main:app --reload
   ```

6. Open the API documentation at http://127.0.0.1:8000/docs. The browser interface is in `index.html`; serve it locally and configure its API requests to point to the backend if needed.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/restaurants` | List sample restaurants; accepts an optional `city` query |
| POST | `/select-restaurant` | Select a restaurant |
| POST | `/chat` | Send a customer message and receive the assistant reply |

## Demo Limitations

- Restaurant menus are sample data stored in `menu.py`.
- Conversation and cart state are held in memory and reset when the server restarts.
- The order ID and UPI payment URI are demo implementations; this project does not establish a live payment-gateway integration.
- Restaurant notifications are currently printed by the backend rather than delivered through a production notification service.

This repository is a prototype for exploring LLM tool calling and the workflow of conversational commerce.
