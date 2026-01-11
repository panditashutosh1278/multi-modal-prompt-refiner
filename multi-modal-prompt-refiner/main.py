from prompt_refiner.refiner import refine_prompt

if __name__ == "__main__":


    input_data = {
        "type": "text",
        "content": "I want a simple task management app for my startup team"
    }

    output = refine_prompt(input_data)
    print("\nEXAMPLE 1 OUTPUT:\n")
    print(output)

    input_data = {
        "type": "text",
        "content": "Build a food delivery app for my city"
    }

    output = refine_prompt(input_data)
    print("\nEXAMPLE 2 OUTPUT:\n")
    print(output)

    
    input_data = {
        "type": "text",
        "content": "Need an app to track daily expenses"
    }

    output = refine_prompt(input_data)
    print("\nEXAMPLE 3 OUTPUT:\n")
    print(output)
