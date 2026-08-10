from services.llm import get_llm

client = get_llm()


def ask_ai(question, vectordb):

    docs = vectordb.similarity_search(
        question,
        k=5
    )

    context="\n".join(
        [doc.page_content for doc in docs]
    )


def ask_ai(question, vectordb):

    docs = vectordb.similarity_search(
        question,
        k=5
    )

    context="\n".join(
        [doc.page_content for doc in docs]
    )


    prompt=f"""
You are a Banking AI Assistant.

Use this transaction data:

{context}

Question:
{question}
"""


    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text