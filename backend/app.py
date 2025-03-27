from flask import Flask, request, jsonify
import openai  # OpenAI GPT integration
import os
import pymongo
import graphviz

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# MongoDB setup
mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = mongo_client["developer_tasks"]
tasks_collection = db["tasks"]

# Function to analyze task using OpenAI GPT
def analyze_task(task_description):
    prompt = f"""Break down the following task into sub-tasks for different developer levels (intern, junior, senior, solo):
    Task: {task_description}"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert software engineer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Function to generate flowchart using Graphviz
def generate_flowchart(sub_tasks):
    dot = graphviz.Digraph()
    dot.node("Start", shape="ellipse")
    
    for i, task in enumerate(sub_tasks):
        dot.node(f"Task{i}", task)
        dot.edge("Start", f"Task{i}")
    
    dot.node("End", shape="ellipse")
    dot.edge(f"Task{i}", "End")
    
    return dot.source

@app.route('/analyze_task', methods=['POST'])
def analyze_task_api():
    data = request.json
    task_description = data.get("task_description")
    if not task_description:
        return jsonify({"error": "Task description is required."}), 400
    
    result = analyze_task(task_description)
    flowchart = generate_flowchart(result.split('\n'))
    
    # Store task in MongoDB
    task_entry = {"task": task_description, "sub_tasks": result, "flowchart": flowchart}
    tasks_collection.insert_one(task_entry)
    
    return jsonify({"task": task_description, "sub_tasks": result, "flowchart": flowchart})

if __name__ == '__main__':
    app.run(debug=True)
