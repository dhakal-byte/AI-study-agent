# AI-study-agent
a ai agent sample model (prototype which is a base for upcoming ai agent in study )
# AI Study Agent 🤖📚

A lightweight Python-based CLI tool designed to help students track their learning progress and identify weak areas in their studies.

## 🚀 Features
- **Interactive Tutoring:** Asks users what they want to study and provides a simplified breakdown.
- **Knowledge Assessment:** Includes a "Quick Test" to verify if the user actually understood the topic.
- **Persistent Memory:** Automatically logs "Weak Topics" into a `memory.txt` file if the user struggles, allowing for focused revision in future sessions.

## 🛠️ How it Works
The agent uses a simple feedback loop:
1. **Input:** User provides a subject and a specific topic.
2. **Explain:** The agent generates a simplified definition.
3. **Test:** The user must provide short answers to test their knowledge.
4. **Log:** If answers are incomplete, the topic is saved to a local "memory" file for later review.

## 📂 File Structure
- `study_agent.py`: The main Python logic.
- `memory.txt`: A local database storing topics that need revision (auto-generated).

## 💻 Getting Started
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-study-agent.git](https://github.com/YOUR_USERNAME/ai-study-agent.git)
