# spacy NLP Learning

Must read of https://spacy.io/

```py
import spacy

nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
```

During text processing, spacy does

1. Tokenization i.e. segments it into words, punctuation and so on. More [here](https://spacy.io/usage/spacy-101#annotations-token)

```py
for token in doc:
    print(token.text)
```

2. Part-of-speech tags and dependencies

After tokenization, spaCy can **parse** and **tag** a given Doc. This is where the statistical **model** comes in, which enables spaCy to make a **prediction** of which **tag** or label most likely applies in this context. More [here](https://spacy.io/usage/spacy-101#annotations-pos-deps)

```py
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
```
