class Solution:
    def arrangeWords(self, text: str) -> str:
        texts = text.split(" ")
        texts[0] = texts[0].lower()
        texts.sort(key=lambda t: len(t))
        texts[0] = texts[0].capitalize()
        return " ".join(texts)
