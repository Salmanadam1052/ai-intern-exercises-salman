import os
from dotenv import load_dotenv
import google.generativeai as genai
from tools import calculator
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    query = input("your question:  ")
    if query.lower() == "exit":
      print("goodbye")
      break

    tool_propmt = f"""
user question : {query}
Available tools :
 calculator : a tool that can perform mathematical calculations
Answer the question using the available tools if necessary, if you don't need to use any tool, just answer the question without mentioning the tools.
If the question requires math, respond with: TOOL: calculator
Otherwise respond with: TOOL: none
"""
    prompt = tool_propmt
    response = model.generate_content(tool_propmt)
    if "calculator" in response.text.lower():
        tool_result = calculator(query)
        tool_used = "calculator"
    else:
        tool_result = None
        tool_used = "none"
    if tool_used == "calculator":
        final_prompt = f"""
user question : {query}
Tool used : {tool_result}
write helpful response    
"""
    else:
        final_prompt = f"answer this question directly without using any tool : {query}"
    final_answer = model.generate_content(final_prompt).text.strip()
    print(f"tool used : {tool_used}")
    print(f"Answer : {final_answer}")    


