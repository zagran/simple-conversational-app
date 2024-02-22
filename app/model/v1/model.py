from fastapi import APIRouter

from core.model import llm

model_router = APIRouter()


@model_router.get("/{question}")
async def root(question: str) -> dict:
    output = llm.invoke(
        question,
        max_tokens=4096,
        temperature=0.2,
        # nucleus sampling (mass probability index)
        # controls the cumulative probability of the generated tokens
        # the higher top_p the more diversity in the output
        top_p=0.1,
    )
    return {"response": output}
