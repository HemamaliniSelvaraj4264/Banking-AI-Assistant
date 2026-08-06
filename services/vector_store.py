from langchain_chroma import Chroma
from langchain_core.documents import Document

from services.embeddigs import get_embeddings


def create_vector_db(data):

    documents=[]

    for _,row in data.iterrows():

        text=f"""
        Date: {row['Date']}
        Description: {row['Description']}
        Amount: {row['Amount']}
        Category: {row.get('Category','')}
        """

        documents.append(
            Document(page_content=text)
        )


    db = Chroma.from_documents(
        documents,
        embedding=get_embeddings(),
        persist_directory="chroma_db"
    )

    return db