# Case 1: Multi-Modal WhatsApp Hotel Booking Agent 🏨🤖

![Architecture Diagram](./architecture-diagram.png)

A production-grade **n8n workflow** that transforms WhatsApp into a powerful, multi-modal booking concierge. This agent handles everything from voice transcriptions and image analysis to complex calendar scheduling using LangChain-powered intelligence.

---

## 🛑 The Problem
Traditional booking systems suffer from high friction and lost leads. 
- **Slow Response Times**: Manual handling of bookings leads to missed opportunities.
- **Inflexible Inputs**: Customers want to send voice notes or photos of receipts, which standard forms can't handle.
- **Context Loss**: Switching between WhatsApp, Calendars, and Sheets often leads to data fragmentation.

## ✅ The Solution
An autonomous **Multi-Modal AI Concierge** that lives where your customers are: WhatsApp.
- **Voice-to-Action**: Transcribes customer voice notes instantly via OpenAI Whisper.
- **Vision-Powered**: Analyzes payment proof or ID photos using GPT-4o.
- **Intelligent Routing**: Automatically distinguishes between "I want to book," "I have a question," and "I'm just chatting."
- **Persistent State**: Uses Redis to handle message bursts and maintain conversation continuity.

---

## 🏗️ How It Works (Architecture)

### Phase 1: Input Handling & Debouncing
The workflow triggers on every WhatsApp message. To handle rapid-fire messages, it uses a **Redis-backed debouncing logic** that waits for the user to finish typing before the AI responds.

### Phase 2: Intent Classification
A central **LangChain Agent** acts as the brain, determining if the user wants to:
1. **Manage Bookings**: Redirects to the Scheduling Agent.
2. **Retrieve Info**: Fetches FAQ/Price data from Google Sheets.
3. **General Chat**: Maintains a friendly, human-like interaction.

### Phase 3: Action Execution
The **Booking Agent** strictly follows a step-by-step data collection flow (Name → Room Type → Date → Time) and interacts directly with **Google Calendar** to check availability and create events.

---

## 💰 Business Impact
- **24/7 Availability**: Never miss a lead, even at 3 AM.
- **90% Automation**: Handles the entire booking lifecycle without human intervention.
- **Seamless Experience**: Customers book via their preferred medium (Voice/Text/Image) without leaving WhatsApp.

---

## 🚀 Getting Started

1. **Import Workflow**: Download `case-study-1-workflow.json` and import it into n8n.
2. **Credentials**: Link your credentials for:
   - WhatsApp Business API
   - OpenAI (GPT-4o & Whisper)
   - Google Calendar & Sheets
   - Redis
3. **Configuration**: Update the Google Sheet URL and Calendar ID in the respective tools.

---

## 🛠️ Tech Stack
- **n8n**: Workflow Orchestration
- **OpenAI**: GPT-4o (Vision/Logic) & Whisper (Transcription)
- **Redis**: Session Persistence & Debouncing
- **Google Workspace**: Calendar & Sheets as the database
- **WhatsApp Cloud API**: The communication interface

---
*Developed with ❤️ for Professional Automation*
