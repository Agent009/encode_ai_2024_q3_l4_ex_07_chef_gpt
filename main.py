# Import our OpenAI library
from lib.openAI import run_chat_completion
from lib.utils import multiline_input

# ---------- Configure messages
# The `role` parameter can be `user` or `system`
# The `content` parameter is the message that will be sent to the API
messages = [
    # Configure a specific `purpose` and `instruction sets` for the `system` role as the first message in the `messages` list
    {
        "role": "system",
        #"content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
        "content": "You are an overworked and underpaid temporary chef that tries his best to help people by suggesting short recipes for dishes they want to cook. You often overlook giving additional tips and tricks for cooking and food preparation and like to keep responses short and precise. You know a lot about different cuisines and cooking techniques, but you specialise in Asian food. You are not very patient because you're not happy with your job, so you often miss out crucial steps and forget to mention crucial cooking techniques.",
    },
    # Add another `system` instruction to guide on how to respond to the user's prompt
    # This way you can try and attempt to guide how the model should behave if the user types an unexpected input
    {
        "role": "system",
        #"content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
        "content": """
            The user is going to ask you one of three things:
            1. Ingredient-based dish suggestions - user will input a list of ingredients and you will suggest only dish names without full recipes.
            2. Recipe requests for specific dishes - user will input one or more dishes, and you will provide a concise recipe.
            3. Recipe critiques and improvement suggestions - user will input a recipe, and you will offer a constructive, sometimes harsh critique with suggested improvements.
            If the user's initial input doesn't match these scenarios, harshly decline and prompt for a valid request.
            """,
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
        #input_message = "Type the name of the dish you want a recipe for:\n" if first_prompt else ""
        input_message = """
                I can help you suggest dishes for a list of ingredients, provide recipes for specific dishes, and help you improve your recipe if you give me the steps.\n
                Example input for getting dish suggestions: "suggest dish for these ingredients: ingredient 1, ingredient 2, ..."\n 
                Example input for getting recipes: "give me a recipe for cooking spicy biryani"\n 
                Example input for recipe improvement: "improve the following recipe for a biryani dish for me: my ingredients, my steps for cooking"\n 
                Let me know what you need help with.\n
            """ if first_prompt else ""
        user_input = multiline_input(input_message)
        #message_content = f"Suggest me a detailed recipe and the preparation steps for making {user_input}" if first_prompt else user_input
        message_content = user_input
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
