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

## Improvements/Suggestions
This is a living repo. Feel free to make tickets for improvement.

## License
This repository is licensed under the MIT License. See the `LICENSE` file for details.

## Attribution
see the `attributions.md` file for details.