# Search_Engine
A search engine through different text documents.

## Indexation
Currently, the algorithm indexes only text document by following the different steps :  
- Extract words : Remove ponctuation and lower all the letter
- Stemming the text : Take the stem of each word in order to allow a research by synonymous words. - Delete all the meaningless words
- Merge words which are synonymous

## Creation of synonyms
The software calls the api : http://watson.kmi.open.ac.uk/API/ on words present in the dictionary http://www.math.sjsu.edu/~foster/dictionary.txt. This way, it builts an association between a word and its synonymous.  
It replaces all the words in the index by the first synoymous in the alphabetic order.

## Search
Currently, it computes the binary distance. More a text will share words with your query, more it would be close.  
This point will be optimized in the future, in order to take into account the occurence of the given word in your query and in the text.  
The cosinus distance between texts will be implemented.

## Execution
```
python3.5 searchEngine.py (-indexation fileName* |-createSynonyms |-search \"Expression\")
```
First step : Build your synonymous dictionnary  
This task is really long, it is why, the current algorithm does not use synonymous.
However, if you want to compute it, you have to execute :  
```
python3.5 searchEngine.py -createSynonyms
```

Second step : Index files  
```
python3.5 searchEngine.py -indexation File1 File2 ...
```
This command will creates different files in your Indexs directory : different indexes and a reverse index to have faster researchs.

Third step : Search
```
python3.5 searchEngine.py -search "Alice in Wonderland..."
```
You will finally see the result !

## Project structure
Find in Indexation :  
- formatIndex.py : Contains the structure of index files and reverse index.
- indexation.py : Every functions links to the creation of the index.
- synonymousProcessing.py : Functions for downloads and creates the synonyms dictionnary, and to merge the different words.
- wordProcessing.py : Functions for the treatment of words (stemming, erasing ...)  

Directory Indexs contains the different indexs needed for the research.  

Tests/ contains unitary tests.

Texts/ contains two example texts extracted from http://www.gutenberg.org.

## Libraries
#### Standard libraries:
 - json
 - os
 - pickle
 - urllib (request and parse)
#### External libraries: 
See **requirements.txt** for more details
Executed with python3.5
