from dotenv import load_dotenv
load_dotenv()
from langchain_core import __version__ as core_version
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

print(f"LangChain Core Version: {core_version}")

def main() -> None:
    print("Hello from rag-production-level!")


if __name__ == "__main__":
    main()