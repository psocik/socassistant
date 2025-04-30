# 🛡️ SOC Assistant

[![License](https://img.shields.io/badge/license-Free-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Hackathon](https://img.shields.io/badge/hackathon-AI-blueviolet)](#)
[![Open Source](https://img.shields.io/badge/open--source-yes-success)](#)

**SOC Assistant** is a cutting-edge, AI-enhanced automation tool designed for Security Operations Centers. It streamlines threat analysis by integrating real-time CTI enrichment, LLM-driven reasoning, and low-code automation via n8n.

🔬 Built for the AI Hackathon — professional, open, and optimized for sustainable security innovation.

---

## 🖥️ Project Showcase

> 📸 Interface Preview  
> ![OpenWebUI Chat Screenshot](images/ui.png)

> 📊 Workflow Visualization  
> ![n8n Flow Diagram](images/workflow.png)
> 
> 📊 LiteLLM Visualization  
> ![n8n Flow Diagram](images/litellm.png)

---

## 🚀 Key Components

### 🔹 OpenWebUI
Modern web interface for intuitive, chat-style interaction with the SOC Assistant. Analysts input IOCs, ask questions, and view enriched results in real time.

### 🔹 n8n + AI Agent
The heart of the system. A dynamic, AI-powered workflow that handles:

- IOC parsing
- Tool orchestration
- Decision-making based on context
- Report summarization

### 🔹 LiteLLM
Handles routing of prompts to Azure OpenAI endpoints, with built-in cost tracking and fallback logic.

### 🔹 Azure AIFoundry (Azure OpenAI)
Scalable, secure LLM hosting using enterprise-grade models like GPT-4. Ensures data privacy and high performance for security workflows.

---

## 🧠 How It Works

1. **Enter IP/domain in OpenWebUI**
2. **AI agent triggers a custom n8n workflow**
3. **Connected tools perform analysis**:
   - 🔍 **Shodan** – Internet exposure
   - 🧠 **MISP** – Threat intelligence
   - 🧰 **More CTI tools** (extendable)

4. **AI summarizes results**, correlates intelligence, and provides action-oriented insights

---

## 📐 Architecture Diagram

> *(Placeholder – replace with actual system architecture)*  
> ![SOC Assistant Architecture](images/architecture.png)

