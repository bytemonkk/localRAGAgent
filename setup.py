from setuptools import setup, find_packages

setup(
    name="LocalRAGAgent",
    version="1.0.0",
    author="Manoj",
    description="A fully local Retrieval-Augmented Generation (RAG) AI Agent built with Ollama, LangChain, and ChromaDB.",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "langchain",
        "langchain-community",
        "langchain-chroma",
        "langchain-ollama",
        "chromadb",
        "ollama",
        "pypdf",
        "python-dotenv",
        "streamlit"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)