import os
from openai import OpenAI
from dotenv import load_dotenv

_INSTRUCTIONS = {
    "PL": "Stwórz opracowanie, grupując najważniejsze informacje w logiczne sekcje, z naciskiem na czytelność i przyswajalność. Przetłumacz fragmenty w innym języku, jeżeli się pojawią.",
    "ENG": "Create an outline by grouping the most important information into logical sections, with an emphasis on readability and digestibility. Translate elements from different languages, if they occur." 
}

def llmRequest(content, selected_response_language):
    load_dotenv()
    api_key = os.getenv('OR_API_KEY')
    base_url = os.getenv('BASE_URL')
    model = os.getenv('MODEL')

    client = OpenAI(
        base_url=f"{base_url}",
        api_key=f"{api_key}",
    )
    stream = client.chat.completions.create(
        model=f"{model}",
        messages=[
            {
                "role": "system", 
                "content": _INSTRUCTIONS[selected_response_language]
            },
            {
                "role": "user", 
                "content": f"{content}"
            }
        ],
        stream=True,
    )
    return stream