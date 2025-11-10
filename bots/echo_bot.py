# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import re


class EchoBot(ActivityHandler):
    """
    Simple Chatbot using Traditional Approaches
    This bot responds to multiple prompts, provides capabilities list,
    and handles malformed input gracefully.
    """
    
    def __init__(self):
        super().__init__()
        # Define bot capabilities
        self.capabilities = [
            "Greet users and respond to greetings",
            "Answer questions about myself",
            "Provide weather information (simulated)",
            "Tell the current time",
            "Perform basic calculations",
            "Tell jokes",
            "List my capabilities with 'help' or 'what can you do'"
        ]
    
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        """Welcome new users to the conversation"""
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                welcome_message = (
                    "Hello and welcome! 👋\n\n"
                    "I'm a simple chatbot here to assist you.\n"
                    "Type 'help' or 'what can you do' to see what I can do!"
                )
                await turn_context.send_activity(welcome_message)

    async def on_message_activity(self, turn_context: TurnContext):
        """Process incoming messages and generate appropriate responses"""
        user_input = turn_context.activity.text.strip()
        
        # Handle empty or whitespace-only input
        if not user_input:
            await turn_context.send_activity("I didn't receive any text. Please type something!")
            return
        
        # Convert to lowercase for easier matching
        user_input_lower = user_input.lower()
        
        # Generate response based on user input
        response = self._generate_response(user_input_lower, user_input)
        
        await turn_context.send_activity(MessageFactory.text(response))
    
    def _generate_response(self, user_input_lower: str, original_input: str) -> str:
        """
        Generate appropriate response based on user input using traditional rule-based approach
        
        Args:
            user_input_lower: Lowercase version of user input for matching
            original_input: Original user input with preserved case
            
        Returns:
            Response string
        """
        
        # Help and capabilities
        if any(keyword in user_input_lower for keyword in ['help', 'what can you do', 'capabilities', 'commands']):
            return self._get_capabilities_message()
        
        # Greetings
        if any(greeting in user_input_lower for greeting in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']):
            return "Hello! How can I help you today? Type 'help' to see what I can do."
        
        # Farewell
        if any(farewell in user_input_lower for farewell in ['bye', 'goodbye', 'see you', 'farewell']):
            return "Goodbye! Have a great day! Feel free to come back anytime."
        
        # How are you
        if 'how are you' in user_input_lower or 'how do you do' in user_input_lower:
            return "I'm doing great, thank you for asking! I'm here and ready to help. How are you?"
        
        # Bot identity questions
        if any(question in user_input_lower for question in ['who are you', 'what are you', 'your name']):
            return "I'm a simple chatbot built using the Microsoft Bot Framework. I use traditional rule-based approaches to understand and respond to your messages."
        
        # Weather (simulated)
        if 'weather' in user_input_lower:
            return "I can provide simulated weather information! The weather today is sunny with a temperature of 72°F (22°C). Perfect day to go outside! ☀️"
        
        # Time
        if 'time' in user_input_lower and any(word in user_input_lower for word in ['what', 'tell', 'current']):
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."
        
        # Date
        if 'date' in user_input_lower and any(word in user_input_lower for word in ['what', 'tell', 'today']):
            from datetime import datetime
            current_date = datetime.now().strftime("%B %d, %Y")
            return f"Today's date is {current_date}."
        
        # Jokes
        if 'joke' in user_input_lower or 'funny' in user_input_lower:
            return self._get_joke()
        
        # Basic calculations
        calc_result = self._try_calculate(user_input_lower)
        if calc_result:
            return calc_result
        
        # Thank you
        if 'thank' in user_input_lower:
            return "You're welcome! Happy to help. Is there anything else I can do for you?"
        
        # Default response for unrecognized input
        return self._handle_unknown_input(original_input)
    
    def _get_capabilities_message(self) -> str:
        """Return formatted list of bot capabilities"""
        capabilities_text = "Here's what I can do:\n\n"
        for i, capability in enumerate(self.capabilities, 1):
            capabilities_text += f"{i}. {capability}\n"
        capabilities_text += "\nJust type naturally and I'll do my best to help!"
        return capabilities_text
    
    def _get_joke(self) -> str:
        """Return a simple joke"""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the chatbot go to therapy? It had too many issues to resolve! 😄",
            "What's a chatbot's favorite snack? Microchips! 🍪",
            "Why don't chatbots ever get tired? They run on endless loops! 🔄"
        ]
        import random
        return random.choice(jokes)
    
    def _try_calculate(self, user_input: str) -> str:
        """
        Attempt to perform basic calculations from user input
        
        Args:
            user_input: User's message
            
        Returns:
            Calculation result or empty string if no calculation found
        """
        # Look for basic math patterns like "5 + 3" or "what is 10 * 2"
        patterns = [
            r'(\d+\.?\d*)\s*\+\s*(\d+\.?\d*)',  # Addition
            r'(\d+\.?\d*)\s*-\s*(\d+\.?\d*)',   # Subtraction
            r'(\d+\.?\d*)\s*\*\s*(\d+\.?\d*)',  # Multiplication
            r'(\d+\.?\d*)\s*/\s*(\d+\.?\d*)',   # Division
        ]
        
        operators = ['+', '-', '*', '/']
        
        for i, pattern in enumerate(patterns):
            match = re.search(pattern, user_input)
            if match:
                try:
                    num1 = float(match.group(1))
                    num2 = float(match.group(2))
                    
                    if operators[i] == '+':
                        result = num1 + num2
                    elif operators[i] == '-':
                        result = num1 - num2
                    elif operators[i] == '*':
                        result = num1 * num2
                    elif operators[i] == '/':
                        if num2 == 0:
                            return "I can't divide by zero! That would break the universe! 🌌"
                        result = num1 / num2
                    
                    # Format result nicely
                    if result == int(result):
                        result = int(result)
                    
                    return f"The answer is: {result} 🧮"
                except (ValueError, ZeroDivisionError):
                    pass
        
        return ""
    
    def _handle_unknown_input(self, user_input: str) -> str:
        """
        Handle malformed or unrecognized input gracefully
        
        Args:
            user_input: Original user input
            
        Returns:
            Helpful response for unknown input
        """
        responses = [
            f"I'm not sure I understand '{user_input}'. Could you rephrase that?",
            f"Hmm, I don't recognize '{user_input}'. Type 'help' to see what I can do!",
            f"I'm still learning! I don't know how to respond to '{user_input}' yet. Try asking something else or type 'help'.",
        ]
        
        import random
        return random.choice(responses)
