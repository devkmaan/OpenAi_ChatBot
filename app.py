from flask import Flask, render_template, request, jsonify  # Import necessary modules
from spellchecker import SpellChecker  # Import SpellChecker class
from chat import chatbot  # Import chatbot function from chat module

app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define route for the root URL
def hello():
    return render_template('chat.html')  # Render HTML template named chat.html

@app.route("/ask", methods=['POST'])  # Define route for handling POST requests to /ask endpoint
def ask():
    message = str(request.form['messageText'])  # Extract message text from request

    # Handle spelling correction
    spell = SpellChecker()  # Create a SpellChecker instance
    words = message.split()  # Split message into words
    corrected_words = [spell.correction(word) for word in words]  # Correct spelling of each word
    corrected_message = ' '.join(corrected_words)  # Join corrected words back into a message

    # Use the corrected message in the chatbot function
    bot_response = chatbot(corrected_message)  # Get response from chatbot function

    # Capitalize the first word of the bot's response
    bot_response = bot_response.capitalize()

    return jsonify({'status': 'OK', 'answer': bot_response})  # Return JSON response with bot's answer

if __name__ == "__main__":  # Check if script is executed directly
    app.run(debug=True)  # Run Flask application in debug mode
