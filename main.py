from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_community.embeddings import HuggingFaceEmbeddings

# Step 1: Load embedding model (CPU-only)
model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {"device": "cpu"}

embedding_model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs
)

# Step 2: Define FastAPI app
app = FastAPI(title="Text Embedding API")

# Step 3: Define input schema
class TextInput(BaseModel):
    text: str

# Step 4: Define route to get embeddings
@app.post("/embed")
async def embed_text(input: TextInput):
    embedding = embedding_model.embed_query(input.text)
    return {"embedding": embedding}
