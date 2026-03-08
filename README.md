# 🤖 Network Troubleshooting Chatbot

An AI-powered network troubleshooting assistant that responds like a 
senior network engineer. Built using Azure OpenAI (GPT-4o-mini) with 
a Groq fallback for development.

## 🏗️ Architecture
```
User Question
      ↓
 Prompt Engineering (System Instructions)
      ↓
 Azure OpenAI GPT-4o-mini
      ↓
 Structured Troubleshooting Response
 (Severity: P1/P2/P3 + CLI Commands)
```

## ✨ Features

- 🔍 Step-by-step network troubleshooting guidance
- 🚨 Automatic incident severity classification (P1 / P2 / P3)
- 💬 Multi-turn conversation memory (remembers context)
- ⚡ Input validation and error handling
- 🔒 Secure API key management via environment variables
- 🔄 Switchable between Azure OpenAI and Groq

## 🛠️ Azure Services Used

| Service | Purpose |
|---|---|
| Azure OpenAI (GPT-4o-mini) | Core AI model for responses |
| Azure AI Foundry | Model deployment and management |
| Groq (Llama3) | Development/fallback LLM |

## 💬 Example Questions
```
"DNS resolution is failing for users on VLAN 10, how do I troubleshoot?"
"What causes DHCP scope exhaustion and how do I fix it?"
"How do I verify if a DNS zone transfer is working correctly?"
"BGP neighbour is stuck in Active state — what are the possible causes?"
```

## 🚀 How to Run

### Prerequisites
- Python 3.x
- Groq API key (free at console.groq.com)
- Azure OpenAI resource (optional)

### Setup
```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/network-troubleshooting-chatbot.git
cd network-troubleshooting-chatbot

# Install dependencies
pip install groq openai python-dotenv

# Add your API key
echo "GROQ_API_KEY=your-key-here" > .env
```

### Run
```bash
python chatbot.py
```

## 🔄 Switching to Azure OpenAI

When Azure OpenAI quota is available, swap these two lines:
```python
# Development (Groq)
from groq import Groq
client = Groq(api_key=os.environ['GROQ_API_KEY'])

# Production (Azure OpenAI)
from openai import AzureOpenAI
client = AzureOpenAI(
    azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'],
    api_key=os.environ['AZURE_OPENAI_KEY'],
    api_version='2024-02-01'
)
```

## 👨‍💻 Author

**Yashas Vishwakarma**  
Network Engineer → AI Engineer  
3.5 years enterprise networking experience (Cisco, Computacenter/Daimler)  
