import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_task(task_description):
    prompt = f"Break down the following task into sub-tasks for different developer levels (intern, junior, senior, solo): {task_description}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert software engineer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
