from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


def main() -> None:
    """Generate a simple joke using LangChain's ChatOpenAI."""
    prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}.")
    llm = ChatOpenAI(temperature=0)
    chain = LLMChain(prompt=prompt, llm=llm)
    topic = "penguins"
    print(chain.run(topic))


if __name__ == "__main__":
    main()
