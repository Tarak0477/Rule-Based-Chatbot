"""
Test script to demonstrate chatbot capabilities
This script shows example interactions without requiring the emulator
"""

from bots.echo_bot import EchoBot


def test_bot_responses():
    """Test various bot responses to demonstrate capabilities"""
    
    bot = EchoBot()
    
    # Test cases with expected behavior
    test_cases = [
        ("help", "Should list capabilities"),
        ("hello", "Should greet user"),
        ("who are you", "Should explain bot identity"),
        ("what's the weather", "Should provide weather info"),
        ("what time is it", "Should tell current time"),
        ("5 + 3", "Should calculate: 8"),
        ("10 * 2", "Should calculate: 20"),
        ("tell me a joke", "Should tell a joke"),
        ("thank you", "Should respond to thanks"),
        ("goodbye", "Should say farewell"),
        ("asdfghjkl", "Should handle unknown input gracefully"),
        ("", "Should handle empty input"),
    ]
    
    print("=" * 70)
    print("CHATBOT CAPABILITY DEMONSTRATION")
    print("=" * 70)
    print()
    
    for i, (user_input, expected) in enumerate(test_cases, 1):
        print(f"Test {i}: {expected}")
        print(f"User: '{user_input}'")
        
        if user_input:
            response = bot._generate_response(user_input.lower(), user_input)
        else:
            response = "I didn't receive any text. Please type something!"
        
        print(f"Bot: {response}")
        print("-" * 70)
        print()


if __name__ == "__main__":
    test_bot_responses()
