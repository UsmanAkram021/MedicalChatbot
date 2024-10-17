from setuptools import find_packages, setup

setup(
    name="Medical Chatbot",
    version="0.0.1",
    author="Muhammad Usman Akram",
    author_email="m.usman.akram021@gmail.com",
    install_requires=[
        "ctransformers==0.2.25",
        "sentence-transformers==3.1.1",
        "langchain==0.3.0",
        "langchain-community==0.3.0",
        "Flask==3.0.3",
        "pypdf==5.0.0",
        "python-dotenv",
        "pinecone"
    ],
    packages=find_packages()
)