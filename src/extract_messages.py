import re


def load_transcription(path):
    """
    Loads the transcription from the given file path.

    Parameters:
        path (str): The file path to the transcription file.

    Returns:
        str: The transcription loaded from the file.
    """
    f = open(path, "r")
    f = f.read()
    return f


def extract_messages_case_one(transcription: str) -> list[str]:
    """Extract content of speaker message from transcripion with regex
    Speaker contains the first and last name of person speaking.
    Message is list of sentences spoken by speaker.
    """
    lines = transcription.split("\n")
    messages = []
    for line in lines:
        if line.startswith("**"):
            case1_regex = r"\*\*\d\d:\d\d\*\* [a-zA-Z]+\s[a-zA-Z]+(\-[a-zA-Z]+)*:\s(.*)"
            match = re.search(case1_regex, line)
            if match:
                messages.append(match.group(2))

    return messages
