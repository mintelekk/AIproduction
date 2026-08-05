

CONTRACTIONS = {'dont': ['do', 'not'],
            'didnt':['did', 'not'],
            'isnt':['is', 'not'],
            'wasnt': ['was', 'not'],
            'cant':	['can', 'not'],
            'arent': ['are','not'],
            'werent':	['were','not'],
            'hasnt':	['has','not'],
            'havent':	['have','not'],
            'hadnt':	['had','not'],
            'cant':	['can','not'],
            'couldnt':	['could','not'],
            'shant':	['shall','not'],
            'shouldnt':	['should','not'],
            'wont':	['will','not'],
            'wouldnt':	['would','not'],
            'mightnt':	['might','not'],
            'mustnt':	['must','not'],
            'oughtnt':	['ought','not'],
            'neednt':	['need','not'],
            'couldve':	['could','have'],
            'shouldve':	['should','have'],
            'wouldve':	['would','have'],
            'mightve':	['might','have'],
            'mustve':	['must','have'],
            'im':	['i','am'],
            'youre':	['you','are'],
            'shes':	['she','is'],
            'hes':	['he','is'],
            'its':	['it','is'],
            'were':	['we','are'],
            'theyre':	['they','are'],
            'ive':	['i','have'],
            'youve':	['you','have'],
            'weve':	['we','have'],
            'theyve':	['they','have'],
            'ill':	['i','will'],
            'youll':	['you','will'],
            'hell':	['he','will'],
            'shell':	['she','will'],
            'itll':	['it','will'],
            'well':	['we','will'],
            'theyll':	['they','will'],
            'id':	['i','would'],
            'youd':	['you','would'],
            'shed': ['she','would'],
            'hed':	['he','would'],
            'itd':	['it','would'],
            'wed': ['we','would'],
            'theyd': ['they','would'],
            'thats': ['that','has'],
            'thatve':['that','have'],
            'thatd':	['that','would'],
            'whichve':	['which','have'],
            'whos':	['who','is'],
            'whore':	['who','are'],
            'whove':	['who','have'],
            'whod':	['who','would'],
            'wholl':	['who','will'],
            'whats':	['what','is'],
            'whatre':	['what','are'],
            'whatll':	['what','will'],
            'wheres':	['where','is'],
            'whered':	['where','did'],
            'whens':	['when','is'],
            'whys':	['why','is'],
            'whyd':	['why','did'],
            'hows':	['how','is'],
            'heres':	['here','is'],
            'theres':	['there','is'],
            'therell':	['there','will'],
            'thered':	['there','would'],
            'someones':	['someone','is'],
            'somebodys':	['somebody','is'],
            'no ones':	['no','one','is'],
            'nobodys':	['nobody','is'],
            'somethings':	['something','is'],
            'nothings':	['nothing','is'],
            'lets':	['let','us'],
            'maam':	['madam'],
            'oclock': ['of','the','clock']}

    
def tokenize(text):
    #Convert to list with spaces as seperation
    text1 = text.split()
    #All words to lowercase
    text1 = [word.lower() for word in text1]
    #Contractions expand to full two words.
    contractionsIndex = []
    #Contractions get marked in above list
    for i, word in enumerate(text1):
        if '\'' in word:
            text1[i] = text1[i].replace('\'', '').replace('\’', '')
            contractionsIndex.append(i)
    #Contractions in text get replaced with matching words.
    for i in contractionsIndex:
        contraction = text1[i]
        if contraction in CONTRACTIONS:
            text1.pop(i)
            words = CONTRACTIONS[contraction]
            for i2,w in enumerate(words):
                text1.insert(i+i2, w)
    return text1