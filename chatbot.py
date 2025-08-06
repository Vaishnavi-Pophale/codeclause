import nltk
from nltk.chat.util import Chat, reflections

# Pairs: (pattern, response)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello there!", "Hi!", "Hey! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Vaishnavi."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries."]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "That's great!"]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you. Please tell me your query."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ],
]

# Chatbot name
chatbot = Chat(pairs, reflections)

# Start chat
def start_chat():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chatbot.converse()

start_chat()
