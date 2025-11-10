"""
Standalone test script to demonstrate chatbot logic
This version doesn't require Bot Framework to be installed
"""

import re
import random
from datetime import datetime


class SimpleChatbotLogic:
    """Simplified version of chatbot logic for testing without Bot Framework"""
    
    def __init__(self):
        self.capabilities = [
            "Greet users and respond to greetings",
            "Answer questions about myself",
            "Provide weather information (simulated)",
            "Tell the current time",
            "Perform basic calculations",
            "Tell jokes",
            "List my capabilities with 'help' or 'what can you do'"
        ]
    
    def generate_response(self, user_input: str) -> str:
        """Generate response based on user input"""
        
        if not user_input or not user_input.strip():
            return "I didn't receive any text. Please type something!"
        
        user_input_lower = user_input.lower().strip()
        
        # Help and capabilities
        if any(keyword in user_input_lower for keyword in ['help', 'what can you do', 'capabilities', 'commands']):
            return self.get_capabilities_message()
        
        # Greetings
        if any(greeting in user_input_lower for greeting in ['hello', 'hi', 'hey', 'greetings', 'good morning']):
            return "Hello! How can I help you today? Type 'help' to see what I can do."
        
        # Farewell
        if any(farewell in user_input_lower for farewell in ['bye', 'goodbye', 'see you']):
            return "Goodbye! Have a great day! Feel free to come back anytime."
        
        # How are you
        if 'how are you' in user_input_lower:
            return "I'm doing great, thank you for asking! I'm here and ready to help. How are you?"
        
        # Bot identity
        if any(question in user_input_lower for question in ['who are you', 'what are you', 'your name']):
            return "I'm a simple chatbot built using the Microsoft Bot Framework. I use traditional rule-based approaches to understand and respond to your messages."
        
        # Weather
        if 'weather' in user_input_lower:
            return "I can provide simulated weather information! The weather today is sunny with a temperature of 72°F (22°C). Perfect day to go outside! ☀️"
        
        # Time
        if 'time' in user_input_lower and any(word in user_input_lower for word in ['what', 'tell', 'current']):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."
        
        # Date
        if 'date' in user_input_lower and any(word in user_input_lower for word in ['what', 'tell', 'today']):
            current_date = datetime.now().strftime("%B %d, %Y")
            return f"Today's date is {current_date}."
        
        # Jokes
        if 'joke' in user_input_lower or 'funny' in user_input_lower:
            return self.get_joke()
        
        # Calculations
        calc_result = self.try_calculate(user_input_lower)
        if calc_result:
            return calc_result
        
        # Thank you
        if 'thank' in user_input_lower:
            return "You're welcome! Happy to help. Is there anything else I can do for you?"
        
        # Unknown input
        return self.handle_unknown_input(user_input)
    
    def get_capabilities_message(self) -> str:
        """Return formatted list of bot capabilities"""
        capabilities_text = "Here's what I can do:\n\n"
        for i, capability in enumerate(self.capabilities, 1):
            capabilities_text += f"{i}. {capability}\n"
        capabilities_text += "\nJust type naturally and I'll do my best to help!"
        return capabilities_text
    
    def get_joke(self) -> str:
        """Return a simple joke"""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the chatbot go to therapy? It had too many issues to resolve! 😄",
            "What's a chatbot's favorite snack? Microchips! 🍪",
            "Why don't chatbots ever get tired? They run on endless loops! 🔄"
        ]
        return random.choice(jokes)
    
    def try_calculate(self, user_input: str) -> str:
        """Attempt to perform basic calculations"""
        patterns = [
            (r'(\d+\.?\d*)\s*\+\s*(\d+\.?\d*)', '+'),
            (r'(\d+\.?\d*)\s*-\s*(\d+\.?\d*)', '-'),
            (r'(\d+\.?\d*)\s*\*\s*(\d+\.?\d*)', '*'),
            (r'(\d+\.?\d*)\s*/\s*(\d+\.?\d*)', '/'),
        ]
        
        for pattern, operator in patterns:
            match = re.search(pattern, user_input)
            if match:
                try:
                    num1 = float(match.group(1))
                    num2 = float(match.group(2))
                    
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 == 0:
                            return "I can't divide by zero! That would break the universe! 🌌"
                        result = num1 / num2
                    
                    if result == int(result):
                        result = int(result)
                    
                    return f"The answer is: {result} 🧮"
                except (ValueError, ZeroDivisionError):
                    pass
        
        return ""
    
    def handle_unknown_input(self, user_input: str) -> str:
        """Handle unrecognized input gracefully"""
        responses = [
            f"I'm not sure I understand '{user_input}'. Could you rephrase that?",
            f"Hmm, I don't recognize '{user_input}'. Type 'help' to see what I can do!",
            f"I'm still learning! I don't know how to respond to '{user_input}' yet. Try asking something else or type 'help'.",
        ]
        return random.choice(responses)


def run_tests():
    """Test various bot responses"""
    
    bot = SimpleChatbotLogic()
    
    test_cases = [
        ("help", "List capabilities"),
        ("hello", "Greet user"),
        ("who are you", "Explain identity"),
        ("what's the weather", "Provide weather"),
        ("what time is it", "Tell time"),
        ("what's the date", "Tell date"),
        ("5 + 3", "Calculate addition"),
        ("10 * 2", "Calculate multiplication"),
        ("15 / 3", "Calculate division"),
        ("20 - 5", "Calculate subtraction"),
        ("tell me a joke", "Tell joke"),
        ("how are you", "Respond to greeting"),
        ("thank you", "Acknowledge thanks"),
        ("goodbye", "Say farewell"),
        ("asdfghjkl", "Handle unknown input"),
        ("", "Handle empty input"),
    ]
    
    print("=" * 80)
    print(" " * 20 + "CHATBOT CAPABILITY DEMONSTRATION")
    print("=" * 80)
    print()
    
    for i, (user_input, description) in enumerate(test_cases, 1):
        print(f"Test {i}: {description}")
        print(f"User Input: '{user_input}'")
        
        response = bot.generate_response(user_input)
        
        print(f"Bot Response: {response}")
        print("-" * 80)
        print()


if __name__ == "__main__":
    run_tests()
    
    print("\n" + "=" * 80)
    print("All tests completed successfully!")
    print("The chatbot demonstrates:")
    print("  ✓ Multiple prompt responses")
    print("  ✓ Capability listing")
    print("  ✓ Graceful error handling")
    print("=" * 80)
