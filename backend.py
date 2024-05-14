import openai
import os

API_KEY = os.getenv("CHATGPT_STUDY_KEY")


class Chatbot:
    def __init__(self):
        self.chatbot = openai.OpenAI(api_key=API_KEY)

        openai.api_key = API_KEY

    def get_response(self, user_input):
        response = self.chatbot.completions.create(
            model="davinci-002",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        )
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    test_response = chatbot.get_response("Give me a riddle")
    print(test_response)