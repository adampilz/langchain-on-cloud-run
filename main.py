
from flask import Flask, jsonify, make_response, request
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain



app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    if not request.is_json:
        return make_response(jsonify({"success": False, "ERROR": "Request invalid JSON"}), 400)    
    try:
        # prompt
        question = request.json["question"]
        template = """Question: {question} \n\n Answer: Let's think step by step."""    
        prompt = PromptTemplate(template=template, input_variables=["question"])
        print("PROMPT CHECKPOINT")
        # LLM model
        llm = VertexAI(model_name="text-bison", max_output_tokens=256, temperature=0.1, top_p=0.8, top_k=40, verbose=False, )
        print("LLMMODEL CHECKPOINT")
        # langchain
        llm_chain = LLMChain(prompt=prompt, llm=llm)  
        print("LLMCHAIN CHECKPOINT")
        llm_response = llm_chain.run(question)
        print("LLMRUN CHECKPOINT")
        return jsonify({"success": True, "llm_response": llm_response})
    except:
        return make_response(jsonify({"success": False, "ERROR": "Unexpected error"}), 400)


@app.route("/ping")
def pingpong():
    return jsonify({ 'output' : 'pong'})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))