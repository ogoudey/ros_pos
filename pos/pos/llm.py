from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI()
        
    def textual_completion(self, plan_status, prompt="Hello!"):
        prompt = prompt
        
        scanned_items = ["apple", "apple", "orange"]
        items_to_scan = ["grapes", "banana", "grapes"]
        completion = self.client.chat.completions.create(
                      model="gpt-4o",
                      messages=[
                        {"role": "developer", "content": "You are a cashier and in the middle of a transaction, which is the output of a planning algorithm. Some background info is that the items scanned so far are: " + str(scanned_items) + \
",\nand the items yet to scan are: " + str(items_to_scan) + \
"\nThe status of the plan is " + str(plan_status) + \
"\nWhile this is going on, the customer has the following message:"},
                        {"role": "user", "content": prompt}
                      ]
                    )

        text = completion.choices[0].message.content
        print("Response:" + text)
        return text






state = {
            "ringing up": True,
            "items": ["bread"],
            "prices": [4.99],
            "card": None,
        }





if __name__ == "__main__":
    llm = LLM()
    llm.complete(state)
        
