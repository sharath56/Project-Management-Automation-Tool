import graphviz

def generate_flowchart(sub_tasks):
    dot = graphviz.Digraph()
    dot.node("Start", shape="ellipse")
    
    for i, task in enumerate(sub_tasks):
        dot.node(f"Task{i}", task)
        dot.edge("Start", f"Task{i}")
    
    dot.node("End", shape="ellipse")
    dot.edge(f"Task{i}", "End")
    
    return dot.source
