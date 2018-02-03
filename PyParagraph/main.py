'''In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

Import a text file filled with a paragraph of your choosing.

Assess the passage for each of the following:

Approximate word count
Approximate sentence count
Approximate letter count (per word)
Average sentence length (in words)
As an example, this passage:

“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

...would yield these results:

Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4'''

import os
import re

def paragraphAnalysis(filename):
    letterCount = 0
    paragraphNumber = 1
    with open('raw_data\\' + filename, newline='', encoding='utf-8') as paragraph:
        
        # Import a text file filled with a paragraph of our choosing
        for textBlock in paragraph:
            # Assess the passage for eaech of the following:
            if len(textBlock) != 1: # Weed out blank paragraphs
                # Approximate word count
                wordCount = textBlock.split(' ')

                # Approximate sentence count
                sentenceCount = re.split('[.!?]+', textBlock)
                # The above adds an empty bit at the end so we'll just snip it off
                sentenceCount.pop(-1)

                # Approximate letter count (per word)
                for word in wordCount:
                    letterCount = letterCount + len(word)
                letterCount = letterCount / len(wordCount)
                
                # Average sentence length (in word)
                for sentence in sentenceCount:
                    swordCount = sentence.split(' ')
                    swordCount = len(swordCount)
                swordCount = swordCount / len(sentenceCount)

                #OUTPUTS#
                print(filename)
                print('Paragraph #' + str(paragraphNumber) + ' Analysis')
                print('-----------------')
                print('Approximate Word Count: ' + str(len(wordCount)))
                print('Approximate Sentence Count: ' + str(len(sentenceCount)))
                print('Average Letter Count: ' + str(letterCount))
                print('Average Sentence Length: ' + str(swordCount) + '\n')
                paragraphNumber = paragraphNumber + 1

paragraphAnalysis('paragraph_1.txt')
paragraphAnalysis('paragraph_2.txt')