from fastapi import FastAPI

from langchain_community.llms import LlamaCpp

app = FastAPI()

llm = LlamaCpp(
    # model_path="/Users/zagran/workspace/simple-conversational-app/models/synthia-7b-v2.0-16k.Q2_K.gguf",
    model_path="/models/synthia-7b-v2.0-16k.Q2_K.gguf",
    # max tokens the model can account for when processing a response
    # make it large enough for the question and answer
    n_ctx=4096,
    # number of layers to offload to the GPU
    # GPU is not strictly required but it does help
    n_gpu_layers=32,
    # number of tokens in the prompt that are fed into the model at a time
    n_batch=1024,
    # use half precision for key/value cache; set to True per langchain doc
    f16_kv=True,
    verbose=False,
)


@app.get("/{question}")
async def root(question: str) -> dict:
    output = llm.invoke(
        question,
        max_tokens=4096,
        temperature=0.2,
        # nucleus sampling (mass probability index)
        # controls the cumulative probability of the generated tokens
        # the higher top_p the more diversity in the output
        top_p=0.1
    )
    return {"response": output}
