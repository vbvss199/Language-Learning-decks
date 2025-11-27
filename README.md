# Language-Learning-flashcard-decks

All language decks started with a word frequency list built from a variety of sources, eg. Wikipedia, movie subtitles, Twitter, etc... we then applied a combination of rules with Gemini to turn this messy frequency data into proper terms for flashcards. We filtered a lot of terms, reduced words to their base form when it made sense (eg. we got rid of "books" but kept "book" and didn't remove either "people" or "person" as that plural breaks normal pluralization rules, etc. etc.). Generic rules are below.

This free dataset is only made possible due to the current state of LLMs. Curating hundreds of thousands of terms across a dozen languages would have taken years, and many, many people.

Most languages follow rules like this:
```
Rules by Part of Speech:
1. Nouns  
   • Depluralize (unless it changes more than 2 characters)  
   • Convert any non-nominative form to nominative  
   • Remove gender inflection  

2. Verbs  
   • Lemmatize to the infinitive form (V1)  
   • Remove gender inflection  

3. Adjectives & Adverbs  
   • Remove superlative & comparative forms (keep only the base)  
   • Remove gender inflection  
   • Lemmatize remaining forms  

4. Prepositions  
   • Remove completely  

5. Pronouns  
   • Lemmatize to the base form  

6. Numerals, Conjunctions & Interjections  
   • Keep as-is  

General Rules:  
   • Remove “super-cognates” (true cognates are OK)  
   • Discard any words that don’t fit cleanly into the 6 categories above 
```

## Data Schema

All vocabulary files follow a standardized JSON schema. Each entry contains:

**Required Fields:**
- **useful_for_flashcard**: Boolean indicating if suitable for flashcard learning (can be null)
- **cefr_level**: CEFR difficulty level (A1, A2, B1, B2, C1, C2, or Unknown)
- **english_translation**: English translation(s), separated by semicolons if multiple
- **example_sentence_english**: English translation of the example sentence
- **pos**: Part of speech (noun, verb, adjective, adverb, etc.)
- **word_frequency**: Frequency ranking (lower = more common, 0 for unranked)

**Optional Fields:**
- **word**: The vocabulary word in the target language (lemmatized/base form) - some languages use alternative field names
- **example_sentence_native**: Example sentence in the target language
- **romanization**: Romanized/transliterated version (for non-Latin scripts)
- **language_variety**: Language variant/dialect (e.g., brazilian, european for Portuguese)
- **gender**: Grammatical gender (masculine, feminine, neuter)
- **article_with_word**: Word with article (e.g., "le chat" in French)
- Language-specific fields for Arabic, German, Korean, etc.

The formal JSON Schema specification is available in [`tests/vocabulary_schema.json`](tests/vocabulary_schema.json).


## Validation & Testing

This repository includes schema validation tests to ensure data quality and consistency across all language files. The test suite is located in the `tests/` folder.


## Improvements/Suggestions
This is a living repo. Feel free to make tickets for improvement.

## License
This repository is licensed under the MIT License. See the `LICENSE` file for details.

## Attribution
see the `attributions.md` file for details.