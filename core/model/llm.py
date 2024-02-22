from langchain_community.llms import LlamaCpp

from core.config import config

llm = LlamaCpp(
    # model_path="/Users/zagran/workspace/simple-conversational-app/models/synthia-7b-v2.0-16k.Q2_K.gguf",
    model_path=config.LLM_MODEL_PATH,
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
