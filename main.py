# Import our OpenAI library
import openAI
from openAI import run_chat_completion

# ---------- Configure messages
# The `role` parameter can be `user` or `system`
# The `content` parameter is the message that will be sent to the API
messages = [
    # Configure a specific `purpose` and `instruction sets` for the `system` role as the first message in the `messages` list
    {
        "role": "system",
        "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
    },
    # Add another `system` instruction to guide on how to respond to the user's prompt
    # This way you can try and attempt to guide how the model should behave if the user types an unexpected input
    {
        "role": "system",
        "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
    }
]

def chef_it():
    counter = 0
    max_prompts = 5

    while counter < max_prompts:
        # The first prompt asks the user a dish name, and consequent prompts are free-form for the user to ask anything.
        first_prompt = counter == 0
        prompts_remaining = max_prompts - counter
        print(f"\n\nYou have {prompts_remaining} prompts remaining." if not first_prompt else "" + "\n")
        input_message = "Type the name of the dish you want a recipe for:\n" if first_prompt else ""
        user_input = input(input_message)
        message_content = f"Suggest me a detailed recipe and the preparation steps for making {user_input}" if first_prompt else user_input
        messages.append(
            {
                "role": "user",
                "content": message_content
            }
        )
        collected_messages = run_chat_completion(messages)
        # Append the last system message to the `messages` list
        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )
        counter = counter + 1


# ---------- Main script
if __name__ == '__main__':
    print(f'Hello, let\'s chef it!')
    chef_it()
