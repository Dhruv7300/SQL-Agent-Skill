from src.config.vectorstore_config import index

def search_schema(user_query):

    results = index.search(
        namespace="__default__",
        query={
            "top_k": 10,
            "inputs": {
                "text": user_query
            }
        }
    )

    hits = results["result"]["hits"]
    schema_chunks = [hit["fields"]["content"] for hit in hits]
    schema_context = "\n\n".join(schema_chunks)

    return schema_context