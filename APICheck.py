import pinecone

# Set your Pinecone API key here
PINECONE_API_KEY = "**"

# Initialize Pinecone client
pinecone.init(api_key=PINECONE_API_KEY)

try:
    # Try listing the indexes to see if the API key works
    indexes = pinecone.list_indexes()
    print("Pinecone API key is valid!")
    print("Existing indexes:", indexes)
except pinecone.exceptions.AuthenticationError as e:
    print("Invalid Pinecone API key. Error:", e)
except Exception as e:
    print("An error occurred:", e)
