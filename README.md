# novel_parser: description
This Python file, created for a digital humanities assignment in my course Rise of the Novel, takes single novels or corpora of novels as input. The user can choose novels from these files and compare them. The program displays "most frequent words" in each novel and "most distinctive words" in each through comparison. The program also displays the "context" (surrounding words) of any word in the novel. (Ex: input "love" will display every use of the word "love" in the novel). I experimented with removing different stopwords when we returned to this program for my English class.

## For class:
I ran the novel parser on a corpora of Victorian and other early novels. 

## My analysis of the program's results:

I wanted to see if I could make the “most frequent words” feature more informative, so I found the list of stopwords that Voyant uses, then read it into a list in textinfo.py. I then used this list to remove stopwords from the results (after asking the user if they want stopwords or not). My favorite finding: Mary Shelley uses the word “miserable” a lot more than she uses the word “happy” in Frankenstein.)

Looking at these texts in comparison and looking at many at a time seems helpful for drawing the kinds of historical conclusions our critics draw. Habermas, for example, states confidently that literature in the 18th century was concerned with marriage. Looking at these results, it is clear that literature does care a lot about love and motherhood and marriage. 

In "The Rise of Fictionality," literary critic and professor Catherine Gallagher draws a contrast between premodern romances, myths, poems, etc., which “may be described in the modern era as drastically suspending or altogether modifying ‘the referentiability of certain claims’” (338). She writes that societies are fictionally sophisticated when they cease to say that verisimilitude intends to deceive the reader. The grand romances that we have compared Austen to with the CS21 labs make their fictionality transparent by using exaggerated verbs and adjectives and heroic, powerful figures, leaving out small details. 

Austen, in contrast, does not attempt to signal nonreferentiality, as words like “mantelpiece,” “apples” and “handwriting” are the kinds of concrete things that Barthes says remind us of reality. Thus she creates the “mental space of the daily life” of which Jameson writes. When we compare her to Brunton, we see that hers were prosaic words that we continue to use today (“dining,” “remarkably,” “bye,” “thorough,”), while the words that Brunton uses seem very Romantic in comparison (“dreary,” “wretch,” “heartless,” “beseech,” “piety,” etc., etc...).  This trend continues in the comparisons between Austen & the canon and between Austen and Chawton. Austen’s words are light, playful and modern-sounding while those that other authors use are grounded in medieval-period nostalgia. Particularly in Chawton we see class divisions that Austen circumvents, from “domestics” to “lords,” “duchesses,” and “earls.” Other contemporary novels are about “chivalry,” “knights,” “wounds,” “saddle,” — large-scale, over-the-top feudal drama. Austen writes of flirtation and friendliness, the kinds of things that humans do regardless of class or era. 
