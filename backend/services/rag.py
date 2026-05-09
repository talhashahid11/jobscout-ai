import os
import json

# Temporary lightweight RAG storage

VECTOR_STORE = []


def create_vector_store(cv_text):

    try:

        global VECTOR_STORE

        # Safety check
        if not cv_text:
            print("CV TEXT EMPTY")
            return False

        # Split text into chunks
        chunks = split_text(cv_text)

        # Store chunks
        VECTOR_STORE = chunks

        print("RAG CREATED")

        return True

    except Exception as e:

        print("RAG ERROR:")
        print(str(e))

        return False


def retrieve_relevant_data(query):

    try:

        global VECTOR_STORE

        if not VECTOR_STORE:
            return []

        # Simple keyword retrieval
        results = []

        query_words = query.lower().split()

        for chunk in VECTOR_STORE:

            chunk_lower = chunk.lower()

            for word in query_words:

                if word in chunk_lower:
                    results.append(chunk)
                    break

        return results[:3]

    except Exception as e:

        print("RETRIEVAL ERROR:")
        print(str(e))

        return []


def split_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks