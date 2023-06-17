import re
import nltk
from nltk.stem.snowball import SnowballStemmer


def extract_salary(text: str):
    pattern_thousands = r"\d+.*(тыс|к|k)"
    thousands = re.findall(pattern_thousands, text)
    pattern = r"(\d+.+\d+).*(\d+.+\d+)"
    raw_salary_range = re.findall(pattern, text, re.IGNORECASE)
    try:
        salary_from, salary_to = raw_salary_range[0]
        salary_from = float(salary_from)
        salary_to = float(salary_to)
    except (IndexError, ValueError) as e:
        print(f"[extract_salary] Error found `{raw_salary_range}`: {e}")
        return None, None
    if thousands:
        salary_to *= 1000
        salary_from *= 1000
    return salary_from, salary_to


def extract_currency(text: str):
    pattern_rub = r"\d+.*(руб|р\.|₽)"
    pattern_usd = r"\d+.*(\$|usd)"
    pattern_eur = r"\d+.*(€|eur|£)"

    currency_rub = re.findall(pattern_rub, text, re.IGNORECASE)
    if currency_rub:
        return "rub"

    currency_usd = re.findall(pattern_usd, text, re.IGNORECASE)
    if currency_usd:
        return "usd"

    currency_eur = re.findall(pattern_eur, text, re.IGNORECASE)
    if currency_eur:
        return "eur"

    return "rub"


def cleanText(string):
    """This function deletes all symbols except Cyrilic and Base Latin alphabet,
    stopwords, functional parts of speech. Returns string of words stem."""
    # Common cleaning
    string = string.lower()
    # string = re.sub(r"http\S+", "", string)
    string = str.replace(string, "Ё", "е")
    string = str.replace(string, "ё", "е")
    prog = re.compile("[А-Яа-яA-Za-z]+")
    words = prog.findall(string.lower())

    # Word Cleaning
    ## Stop Words
    stopwords = nltk.corpus.stopwords.words("russian")
    words = [w for w in words if w not in stopwords]
    ## Cleaning functional POS (Parts of Speech)
    functionalPos = {"CONJ", "PRCL"}
    words = [
        w for w, pos in nltk.pos_tag(words, lang="rus") if pos not in functionalPos
    ]
    ## Stemming
    stemmer = SnowballStemmer("russian")
    return " ".join(list(map(stemmer.stem, words)))
