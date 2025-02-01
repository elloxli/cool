import matplotlib.pyplot as plt
import openai

def get_user_data():
    print("Welcome to your AI-powered Budget Advisor!")
    income = float(input("Enter your monthly income: "))
    expenses = []
    
    print("Enter your expenses. Type 'done' when finished.")
    while True:
        item = input("Expense category and amount (e.g., Rent 500): ")
        if item.lower() == 'done':
            break
        try:
            category, amount = item.split()
            expenses.append((category, float(amount)))
        except ValueError:
            print("Invalid format. Use 'Category Amount' (e.g., Rent 500).")
    
    return income, expenses


def analyze_expenses(income, expenses):
    total_expenses = sum(amount for _, amount in expenses)
    print(f"\nTotal Income: ${income}")
    print(f"Total Expenses: ${total_expenses}")
    
    if total_expenses > income:
        print("⚠️ You are spending more than your income!")
    else:
        print("✅ Your spending is within your budget.")

    # Categorize expenses
    expense_summary = {}
    for category, amount in expenses:
        if category in expense_summary:
            expense_summary[category] += amount
        else:
            expense_summary[category] = amount
    
    print("\nExpense Breakdown:")
    for category, total in expense_summary.items():
        print(f"{category}: ${total}")
    
    return expense_summary


def give_advice(expense_summary, income):
    print("\nAI Budget Advisor:")
    # Basic advice based on spending
    for category, amount in expense_summary.items():
        if amount > income * 0.3:
            print(f"- Consider reducing spending on {category}. It's over 30% of your income.")
    print("Tip: Save at least 20% of your income for future expenses.")
    
def visualize_expenses(expense_summary):
    categories = list(expense_summary.keys())
    amounts = list(expense_summary.values())
    
    plt.bar(categories, amounts, color='blue')
    plt.title("Expense Breakdown")
    plt.xlabel("Categories")
    plt.ylabel("Amount ($)")
    plt.show()
    
    
def get_ai_advice(expense_summary, income):
    # Set your OpenAI API key
    openai.api_key = "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"

    # Prepare the data for AI
    categories = ", ".join([f"{category}: ${amount}" for category, amount in expense_summary.items()])
    prompt = (
        f"I am a budget advisor AI. My user has a monthly income of ${income}. "
        f"Their expenses are as follows: {categories}. "
        "Provide the following details:\n"
        "1. Identify which categories are too high and suggest specific actions to reduce spending.\n"
        "2. Recommend how they can save at least 20% of their income.\n"
        "3. Provide tips for improving their financial health in a unique and personalized way.\n"
        "4. Suggest long-term strategies for building savings or investments.\n"
        "Make your advice actionable, creative, and specific."
    )

    # Debug: Print the prompt being sent
    print("\nDebug Prompt:")
    print(prompt)

    # Call the OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=800,  # Increase token limit for detailed advice
            temperature=0.7  # Balance creativity and relevance
        )
        advice = response['choices'][0]['text'].strip()

        # Debug: Print the raw response for troubleshooting
        print("\nDebug Raw Response:")
        print(response)

        # Display the advice to the user
        print("\nAI Financial Advice:")
        print(advice)
    except Exception as e:
        print(f"Error using OpenAI API: {e}")


   
        

def main():
    income, expenses = get_user_data()
    expense_summary = analyze_expenses(income, expenses)
    give_advice(expense_summary, income)
    visualize_expenses(expense_summary)
    get_ai_advice(expense_summary, income) 

if __name__ == "__main__":
    main()







