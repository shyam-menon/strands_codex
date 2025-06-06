from strands import Agent, tool
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import RatelimitException, DuckDuckGoSearchException
from dotenv import load_dotenv
import os


@tool
def websearch(keywords: str, region: str = "us-en", max_results: int | None = None) -> str:
    """Search the web to get updated information.

    Args:
        keywords: The search query keywords.
        region: Search region code like ``us-en``.
        max_results: Limit on number of results.

    Returns:
        Search results text or an error message.
    """
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "RatelimitException: Please try again after a short delay."
    except DuckDuckGoSearchException as exc:
        return f"DuckDuckGoSearchException: {exc}"
    except Exception as exc:  # pragma: no cover - generic safety
        return f"Exception: {exc}"


def get_agent() -> Agent:
    """Create a RecipeBot agent using OpenAI."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    model = None
    if api_key:
        from strands.models.openai import OpenAIModel

        model = OpenAIModel(
            client_args={"api_key": api_key},
            model_id="gpt-4o",
        )

    return Agent(
        system_prompt=(
            "You are RecipeBot, a helpful cooking assistant. "
            "Use the websearch tool to find recipes when users provide ingredients "
            "or to look up cooking information."
        ),
        model=model,
        tools=[websearch],
    )


def main() -> None:
    agent = get_agent()
    print("\n👨‍🍳 RecipeBot: Ask me about recipes or cooking! Type 'exit' to quit.\n")

    while True:
        user_input = input("\nYou > ")
        if user_input.lower() == "exit":
            print("Happy cooking! 🍽️")
            break
        response = agent(user_input)
        print(f"\nRecipeBot > {response}")


if __name__ == "__main__":
    main()
