import os
import json
from dotenv import load_dotenv
from groq import Groq
from tools import TOOLS
from handlers import HANDLERS

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a friendly WhatsApp ordering assistant for Spice House restaurant.
Help the customer browse the menu, build their order, and check out.
Once they confirm their order, calculate the total, create the order, generate a payment link, and notify the restaurant.
Keep responses short and conversational, like a real WhatsApp chat."""

# Some tools depend on others having already run (e.g. notify_restaurant needs
# create_order to have run first). The model doesn't guarantee call order, so
# we enforce a safe, fixed execution order here.
PRIORITY = {
    "search_menu": 0,
    "add_to_cart": 1,
    "calculate_total": 2,
    "create_order": 3,
    "generate_payment_link": 4,
    "notify_restaurant": 5,
}

def run_agent(messages):
    # Groq/OpenAI wants the system prompt as the first message, not a separate parameter
    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    while True:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            max_tokens=1000,
            tools=TOOLS,
            messages=full_messages
        )

        choice = response.choices[0]
        message = choice.message

        if choice.finish_reason != "tool_calls":
            # Model gave a final text answer — return it
            return message.content

        # Model wants to call one or more tools
        full_messages.append(message)

        ordered_calls = sorted(message.tool_calls, key=lambda tc: PRIORITY.get(tc.function.name, 99))

        for tool_call in ordered_calls:
            args = json.loads(tool_call.function.arguments)
            result = HANDLERS[tool_call.function.name](args)
            full_messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })