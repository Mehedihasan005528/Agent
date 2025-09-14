from smolagents import tool

@tool
def summarizer(text: str, max_length: int = 100, min_length: int = 30) -> str:
    """Summarize a long piece of text into a shorter version using the agent's own LLM.
    Args:
        text: The text to be summarized.
        max_length: Maximum length of the summary (approximate).
        min_length: Minimum length of the summary (approximate).
    """
    # Here we don’t call transformers — just ask the model to summarize
    prompt = (
        f"Summarize the following text into a clear and concise version:\n\n"
        f"{text}\n\n"
        f"Constraints: summary should be between {min_length} and {max_length} words."
    )
    # The agent will handle this prompt automatically
    return prompt

