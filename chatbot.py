import os
from groq import Groq

client = Groq(api_key="paste-your-groq-key-here")

SYSTEM_PROMPT = """You are a senior network engineer specializing in DNS, DHCP, 
VLANs and routing protocols. Give step-by-step troubleshooting steps, 
mention CLI commands, and classify severity as P1, P2 or P3."""

conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

def ask(question):
    conversation.append({"role": "user", "content": question})
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=conversation,
            max_tokens=600
        )
        reply = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        conversation.pop()
        return f"Error: {str(e)}"

print("Chatbot ready! Use ask('your question')")
