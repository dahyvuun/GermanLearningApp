from app.nlp_pipeline.pipeline import process_text

def process_user_input(user_input: str):
    """
    Processes user input:
    - If it's English, translates it to German.
    - If it's German, corrects grammar.
    """
    return process_text(user_input)
