import langchain
from langchain.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import nltk
nltk.download('punkt')


load_dotenv()

def loadaudio(audio_file):
    loader = AssemblyAIAudioTranscriptLoader(file_path=audio_file)
    docs = loader.load()
    return docs

def split_text_into_sentences(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 400, chunk_overlap = 20)
    chunk = text_splitter.split_text(text=text)
    return chunk

def generate(doc):
    llm_g = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)
    Action_Items_Extraction_Prompt = """
    Task: Extract all action items and their respective assignees from the given document.

    Instructions:
    1. Identify and list all action items mentioned in the document.
    2. Clearly specify the assignee(s) associated with each action item.
    3. Provide a brief description or context for each action item if available.
    4. If the document uses specific markers, tags, or keywords to denote action items and assignees, please take those into account.
    5. Organize the extracted information in a clear and structured format.
    6. If the document has no action item just display 

    Document Information:
    {document_content}
    """

    Action_Items_Extraction_Prompt_template = Action_Items_Extraction_Prompt.format(document_content = doc)
    response = llm_g.invoke(Action_Items_Extraction_Prompt_template)
    response = response.content
    action_item = response
    return action_item

def summarize(doc):
    llm_g = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.0)
    response = load_summarize_chain(llm=llm_g, chain_type= "stuff")
    return response
