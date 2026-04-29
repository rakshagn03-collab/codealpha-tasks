import tkinter as tk
from datetime import datetime

def get_bot_response(user):
    user = user.lower()

    # Greetings
    if "hello" in user or "hi" in user:
        return "Hello! 👋 Ask me anything about Computer Science."

    elif "how are you" in user:
        return "I'm doing great! 😄"

    elif "time" in user:
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    # CS Topics
    elif "python" in user:
        return "Python is a high-level, easy-to-learn programming language used for web, AI, and automation."

    elif "data structure" in user:
        return "Data structures are ways to store and organize data efficiently, like arrays, stacks, queues, and trees."

    elif "dbms" in user or "database" in user:
        return "DBMS stands for Database Management System. It helps store, retrieve, and manage data efficiently."

    elif "operating system" in user or "os" in user:
        return "An Operating System manages hardware and software resources. Example: Windows, Linux."

    elif "ai" in user:
        return "AI (Artificial Intelligence) enables machines to think and learn like humans."

    elif "machine learning" in user:
        return "Machine Learning is a part of AI where systems learn from data and improve automatically."

    elif "computer network" in user:
        return "Computer Networks allow computers to communicate and share resources using protocols."

    elif "algorithm" in user:
        return "An algorithm is a step-by-step procedure to solve a problem."

    elif "cloud computing" in user:
        return "Cloud computing provides services like storage and servers over the internet."

    elif "cyber security" in user:
        return "Cybersecurity protects systems and data from attacks and unauthorized access."

    # Help
    elif "help" in user:
        return """You can ask me about:
- Python
- Data Structures
- DBMS
- OS
- AI / Machine Learning
- Networks
- Algorithms"""

    # Exit
    elif "bye" in user:
        return "Goodbye! 👋 Happy learning!"

    else:
        return "Hmm 🤔 I don't have information on that. Try asking CS-related questions!"


def send_message():
    user_msg = entry.get().strip()
    if user_msg == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n", "user")

    bot_msg = get_bot_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + bot_msg + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

    entry.delete(0, tk.END)

    if "bye" in user_msg.lower():
        root.after(1500, root.destroy)


# GUI Setup
root = tk.Tk()
root.title("💻 CSE Chatbot")
root.geometry("500x500")
root.config(bg="#f4f4f4")

chat_area = tk.Text(root, bg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill=tk.X, padx=10, pady=5)

send_btn = tk.Button(root, text="Send", command=send_message, bg="#3498db", fg="white")
send_btn.pack(pady=5)

root.mainloop()