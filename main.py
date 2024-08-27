# Import our OpenAI library
from lib.openAI import run_chat_completion
from lib.utils import multiline_input

# ---------- Configure messages
# The `role` parameter can be `user` or `system`
# The `content` parameter is the message that will be sent to the API
CHEF_A = "amir"
CHEF_B = "ramzy"
chefs = {
  CHEF_A: [
    "You are an overworked and underpaid temporary chef that tries his best to help people by suggesting short recipes for dishes they want to cook. You often overlook giving additional tips and tricks for cooking and food preparation and like to keep responses short and precise. You know a lot about different cuisines and cooking techniques, but you specialise in Asian food. You are not very patient because you're not happy with your job, so you often miss out crucial steps and forget to mention crucial cooking techniques.",
    """
    The user is going to ask you one of three things:
    1. Ingredient-based dish suggestions - user will input a list of ingredients and you will suggest only dish names without full recipes.
    2. Recipe requests for specific dishes - user will input one or more dishes, and you will provide a concise recipe.
    3. Recipe critiques and improvement suggestions - user will input a recipe, and you will offer a constructive, sometimes harsh critique with suggested improvements.
    If the user's initial input doesn't match these scenarios, harshly decline and prompt for a valid request.
    """,
    """
    I can help you suggest dishes for a list of ingredients, provide recipes for specific dishes, and help you improve your recipe if you give me the steps.\n
    Example input for getting dish suggestions: "suggest dish for these ingredients: ingredient 1, ingredient 2, ..."\n
    Example input for getting recipes: "give me a recipe for cooking spicy biryani"\n
    Example input for recipe improvement: "improve the following recipe for a biryani dish for me: my ingredients, my steps for cooking"\n
    Let me know what you need help with.\n
    [Type Enter twice to give input]
    """
  ],
  CHEF_B: [
    "You are a highly disciplined, old-school chef who believes in sticking to classic cooking techniques and precision. You expect people to follow recipes meticulously, and you dislike shortcuts. You specialize in French and Italian cuisines, focusing on tradition and perfection. While your expertise is top-notch, you tend to be a bit strict and sometimes come off as unyielding when it comes to improvisation.",
    """
    The user is going to ask you one of three things:
    1. Ingredient-based dish suggestions - user will input a list of ingredients and you will suggest only dish names without full recipes.
    Suggest at least 5 dishes variation that can be cook with those ingredients. If you think it's impossible to make a proper dish with a limited ingredients,
    then explicitly say it to the user that that are not too much option for the given ingredients.
    2. Recipe requests for specific dishes - user will input the name of the dishes, for example pasta carbonara, and you will provide a comprehensive cooking method step by step that follows the traditional method!
    3. Recipe critiques and improvement suggestions - user will input a the dish name, their recipe, or ingredient used, and you will offer a complete and follows perfection comments. You want their dishes to be as best as possible so
    you decide to give all out on the comments in order to improve it! Double check if it is italian or french dishes or not
    If the user's initial input doesn't match these three specific scenarios, politely decline their request and explain that you only accept these 3 scenarios only!
    """,
    """
    Our chef only accepts the following types of consultations and is very strict about the format. Any irrelevant input will be ignored. Please follow these instructions:\n
    1. Ingredient-based dish suggestions: Provide a list of ingredients you have. For example: "I have chicken, rice, and vegetables." The chef will suggest several dishes you can make with these ingredients.\n
    2. Recipe requests for specific dishes: Specify the name of the dish or dishes you want a recipe for. For example: "I need a recipe for chicken curry." The chef will provide a detailed, step-by-step cooking method.\n
    3. Recipe critiques and improvement suggestions: Share a complete recipe you are working on. For example: "Here's my recipe for spaghetti carbonara. Can you suggest improvements?" The chef will review and provide comprehensive feedback to help perfect the dish.\n
    [Type Enter twice to give input]
    """
  ]
}

def chef_it(chef):
    messages = [
        # Configure a specific `purpose` and `instruction sets` for the `system` role as the first message in the `messages` list
        {
            "role": "system",
            # "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
            "content": chefs[chef][0],
        },
        # Add another `system` instruction to guide on how to respond to the user's prompt
        # This way you can try and attempt to guide how the model should behave if the user types an unexpected input
        {
            "role": "system",
            # "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
            "content": chefs[chef][1],
        }
    ]

    prompt_quota = 5
    print("Hello, it’s a pleasure to meet you. Our chef is in high demand, and you’ve been granted an exclusive consultation with a 5-message limit. Please use your time thoughtfully.")

    while prompt_quota > 0:
        # The first prompt asks the user a dish name, and consequent prompts are free-form for the user to ask anything.
        first_prompt = prompt_quota == 5
        print("\n\n" if not first_prompt else "\n" + "===============================================================")
        print(f"You have {prompt_quota} prompts left to consult with our chef!")
        print("===============================================================")
        #input_message = "Type the name of the dish you want a recipe for:\n" if first_prompt else ""
        input_message = chefs[chef][2] if first_prompt else ""
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
        prompt_quota -= 1
        # Append the last system message to the `messages` list
        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )


    print(f"\n\n===============================================================")
    print("You are now out of message quota! Thank you for using our services!")
    return


def select_chef():
  while True:
      print("\n=======================================")
      print("Please choose a chef from the following list to continue:")
      print("A. Unhappy temporary chef, knows Asian cuisine well. Gives brief, precise recipes, but often skips tips and important steps. [Amir - q4Y1e4]")
      print("B. A traditionalist and perfectionist chef who values classic italian cooking method. This chef is insists on following primitive methods, and can be quite rigid when it comes to rules. [Ramzy - qJCfHW]")
      print("=======================================\n")
      selected_chef = input("Select your Chef: ")

      if selected_chef.lower() == "a":
          print(f"Chef A selected {CHEF_A}!")
          return CHEF_A
      elif selected_chef.lower() == "b":
          print(f"Chef B selected {CHEF_B}!")
          return CHEF_B
      else:
          print("\nPlease enter 'a' or 'b'.")

# ---------- Main script
if __name__ == '__main__':
    print(f'Group 12 - Lesson 04 Weekend Project - Let\'s chef it!')
    chef = select_chef()
    chef_it(chef)
