import sys
import random
class Hangman():
    #numner of attemps
    NUM_TRIAL = 11
    list_of_words = ['affability', 'kinglinesses', 'papeteries', 'bro', 'ironer', 'kyboshed', 'hoodie', 'settlors', 'stonefish', 'feloniousnesses', 'butyrophenone', 'ensile', 'impartment', 'penalty', 'belatednesses', 'overchilled', 'veery', 'ridglings', 'globe', 'amortised', 'matzohs', 'nonelective', 'jacqueries', 'narratological', 'cacophonous', 'catheterization', 'outdared', 'harpsichordist', 'guttered', 'dekes', 'salutations', 'iterate', 'hegumen', 'transshapes', 'spearmints', 'committals',  'text', 'connecting', 'inkjet', 'minestrones', 'waveform', 'pyrophyllites', 'bullrings', 'unbridling', 'asphyxies', 'partyers', 'judgmatically', 'shirtsleeve', 'ascetically', 'dirl', 'enlightening', 'douma', 'pinkoes', 'sightlessness', 'moulding', 'swingby', 'waveshape', 'intercessional', 'tusses', 'field', 'yeshiva', 'explorational', 'rigour', 'fictivenesses', 'gusto', 'ahoy', 'schmelze', 'whooshed', 'yellower', 'athetoid', 'ordeal', 'monoxide', 'peacockish', 'deadbeat', 'anecdote', 'uncoalesced', 'hackmatack', 'offishness', 'almsgivings', 'effervescence', 'gravel', 'renovative', 'desertifications', 'bamming', 'toepieces', 'gluttonously', 'crams', 'overmedicates', 'commonsense', 'birthdates', 'desorbed', 'psst', 'retrogradation', 'sphygmomanometer', 'barouche', 'unharness', 'correlational', 'martyrologies', 'winglet', 'heptarch', 'spectroscopies', 'oversensitivities', 'immunofluorescence', 'totalities', 'thimbleberry', 'penates', 'slipup', 'oughted', 'oedema', 'preening', 'meropic', 'redialing', 'hyperparathyroidisms', 'flicked', 'buttocks', 'readout', 'whitewashes', 'arioso', 'appeasements', 'preventers', 'snarkier', 'pratfalls', 'surbased', 'excogitative', 'idolators', 'disaccharides', 'rebuy', 'establisher', 'embays', 'extorting', 'apocalyptist', 'emetics', 'microdissection', 'misalters', 'mortalities', 'fuglemen', 'symposiums', 'host', 'prelims', 'sizeable', 'titivated', 'agrarianisms', 'microinjected', 'strobes', 'soymilks', 'scrawnier', 'tapir', 'blowouts', 'overdrink', 'counterviolences', 'cranky', 'bombyx', 'neurophysiology', 'uprightness', 'clownishly', 'guitarfish', 'rump', 'hardset', 'quietened', 'cockiness', 'roquelaures', 'osmoregulatory', 'rune', 'dotardly', 'medallion', 'advertized', 'labored', 'lineality', 'springers', 'counterespionages', 'substratum', 'gauffered', 'summered', 'inevitably', 'dewy', 'outweighing', 'antistrophe', 'denunciative', 'chimbley', 'speculums', 'perniciousnesses', 'tenacities', 'outmaneuvering', 'gimped', 'yardwands', 'hospices', 'electrodesiccations', 'palliates', 'weighmen', 'decentre', 'plasterings', 'smirk', 'exuberating', 'sedulity', 'mild', 'becrawl', 'relit', 'stumble', 'rugose', 'resistants', 'professedly', 'flemishing', 'bibelot', 'pinpricking', 'songwriter', 'hath', 'whists', 'condemners', 'bonnyclabber', 'acreages', 'sanitary', 'hindrances', 'reanimates', 'takeouts', 'coccidiosis', 'lensing', 'norite', 'punkies', 'overstaying', 'aureolae', 'lobsticks', 'cheekinesses', 'outscored', 'judges', 'wops', 'inhumanities', 'defoliations', 'mysticly', 'communicators', 'bagging', 'agapeic', 'intubates', 'afterlife', 'forwards', 'resultant', 'straightjacketing', 'arsenopyrites', 'skirt', 'codiscovering', 'microphyll', 'vicunas', 'radishes', 'tintinnabulations', 'fodders', 'solidaristic', 'dizzily', 'transferrable', 'cookings', 'subdepot', 'antiparasitics', 'synthesist', 'controverted', 'grison', 'rescinders', 'possessive', 'substitutive', 'nucleonics', 'scientific', 'misphrasing', 'serviceberry', 'shipwrecks', 'ferbam', 'ionospheric', 'waitstaff', 'dynamometries', 'ascendant', 'zeroth', 'neuropathologic', 'refocussed', 'craniosacral', 'contractually', 'corrupts', 'poilu', 'openheartedness', 'butterflyers', 'goldfinch', 'wordage', 'provoking', 'deism', 'idolism', 'cunningness', 'greys', 'lithoid', 'thenceforwards', 'darkling', 'woefulness', 'electrolyte', 'cheongsam', 'hypercorrectnesses', 'relets', 'rehems', 'arabic', 'coppered', 'safflower', 'sprats', 'bloodstream', 'elegizing', 'reiving', 'yirred', 'beachcombers', 'derogate', 'arcing', 'honeycombing', 'incensed', 'remorsefulnesses', 'internationalize', 'moles', 'peristaltic', 'reexpresses', 'orthographical', 'allseed', 'heathendoms', 'recruitment', 'talkativenesses', 'hydroplane', 'rouletting', 'dormins', 'purpuras', 'policyholders', 'arbitrable', 'militiaman', 'veinlike', 'nargile', 'pile', 'snuffles', 'fondles', 'laciness', 'filling', 'nonregulated', 'animal', 'vilifiers', 'gerrymandering', 'gentrice', 'rescript', 'lodgments', 'acaudal', 'pointman', 'whaleman', 'genome', 'glassworkers', 'seggar', 'deliriums', 'sibilations', 'hallows', 'euxenites', 'speedwell', 'soling', 'tying', 'promontories', 'gulpy', 'loopiest', 'mailes', 'inbreeding', 'wry', 'fets', 'detoxicants', 'infestation', 'planetaria', 'trindle', 'sonneteerings', 'caid', 'quadrivium', 'avulses', 'washrooms', 'keeper', 'step', 'occipita', 'scheming', 'swale', 'obsessives', 'endeavoring', 'thoroughgoing', 'rotator', 'skimmed', 'methylations', 'bluster', 'atavism', 'birses', 'costermonger', 'emplacing', 'mantas', 'uncock', 'backtracks', 'soil', 'blanch', 'lateens', 'oxidising', 'deface', 'gharials', 'wheeziest', 'sodium', 'subalpine', 'fardels', 'triethyl', 'surceases', 'mantelshelf', 'pedologies', 'chuckled', 'peneplane', 'perry', 'stomachy', 'damped', 'desmosomes', 'curiae', 'flannelettes', 'arisen', 'snowberries', 'saltant', 'filariases', 'lealties', 'abetted', 'doubtful', 'aventails', 'hydrobiology', 'coordinators', 'unlawfulness', 'dethroning', 'septuagenarian', 'subcapsular', 'ta', 'dovishness', 'atemoya', 'spiraeas', 'lycopods', 'incident', 'tsorriss', 'stranding', 'haustorium', 'deerberry', 'screamed', 'podestas', 'sibilances', 'modiste', 'limbing', 'eupatrids', 'mustiest', 'angstrom', 'palace', 'syrphid', 'lepidopterists', 'toilsomenesses', 'jettons', 'conciser', 'tambourine', 'coached', 'unconditional', 'backrooms', 'prototypically', 'fetoscopy', 'sedimentologic', 'genes', 'concessively', 'limonites', 'planless', 'recombing', 'gundog', 'lobations', 'slid', 'eutaxy', 'boodler', 'intercalating', 'photobiologic', 'scorpions', 'noospheres', 'jactitations', 'rhizoctonia', 'exaltation', 'unactorish', 'surtaxing', 'reaccredits', 'valiantnesses', 'cardamums', 'egocentrics', 'discerned', 'bumptiousnesses', 'fearers', 'intersterile', 'demeanours', 'couteaux', 'setback', 'bioelectricities', 'snooded', 'logicising', 'lolled', 'andalusites', 'phenolphthaleins', 'muckraker', 'dalliers', 'noncolored', 'grandsirs', 'becrawls', 'singling', 'swellheads', 'spiks', 'bushidos', 'necropsied', 'pedlary', 'resinifies', 'hyoscines', 'pronunciamentos', 'cremating', 'puttied', 'calcareously', 'bildungsromans', 'readjustment', 'outjump', 'wispish', 'lithified', 'anodizes', 'residuary', 'pewters', 'antimaterialists', 'humerus', 'inventorial', 'antibaryon', 'paleomagnetically', 'gleeds', 'trapesed', 'quintuplicate', 'cuttled', 'feelingly', 'unhair', 'deifical', 'bratwurst', 'journalese', 'teocallis', 'restrooms', 'teniae', 'vexatious', 'citrins', 'eviction', 'noncontemporary', 'busloads', 'onomatopoetic', 'coassumed', 'enframes', 'nincompooperies', 'sousaphones', 'snoopily', 'sociogram', 'dangerous', 'semisynthetic', 'astrophysics', 'phonemicists', 'carabins', 'upraise', 'wrasse', 'harks', 'regretfulnesses', 'semiwild', 'maximization', 'drachmas', 'mountainously', 'isinglasses', 'ulamas', 'purls', 'arboured', 'pregnabilities', 'incomparability', 'overweens', 'groan', 'assiduousness', 'teawares', 'theoretically', 'accentuates', 'spiracle', 'methodises', 'missives', 'tenable', 'warpower', 'prepregs', 'nonutility', 'sambo', 'puttyroot', 'sufferances', 'irreligious', 'autumn', 'outraised', 'jinricksha', 'harborages', 'federalization', 'reformulating', 'pantisocratists', 'hehs', 'metages', 'staccati', 'demulcents', 'overburned', 'odometries', 'smokeable', 'simplenesses', 'zymosan', 'pharmacologists', 'circuses', 'canoness', 'tictocking', 'nucleoplasms', 'profligate', 'oilholes', 'sermonizes', 'drifty', 'wetwares', 'estranger', 'kelsons', 'colligated', 'delocalize', 'denervate', 'grayish', 'polyclonal', 'shuddery', 'tapestried', 'pemphixes', 'portrays', 'ultravirile', 'olivenites', 'nitrating', 'trochanteral', 'indiscriminately', 'kolkhozniks', 'embellish', 'defaces', 'egging', 'qat', 'splats', 'budgerigars', 'whoopie', 'nostalgic', 'benignities', 'endemically', 'coifed', 'redips', 'semigroups', 'vigintillion', 'escalloping', 'postconception', 'swillers', 'anorexies', 'valencias', 'frugivores', 'cozens', 'accouchement', 'planters', 'sprucier', 'immediatenesses', 'dissuasiveness', 'uncharitableness', 'haptens', 'loafing', 'cajoles', 'floccus', 'reshown', 'driveled', 'lapidary', 'princeliest', 'caporal', 'collectivized', 'analogue', 'strangeness', 'prosthodontists', 'pyknics', 'indexation', 'otoliths', 'heartaches', 'weakhearted', 'practised', 'drying', 'diamantes', 'tacitly', 'suttas', 'zorils', 'chillum', 'camouflageable', 'ruptured', 'ventricose', 'dwelt', 'drooping', 'rewrapped', 'octavo', 'jackasses', 'misgrafted', 'forks', 'oarsman', 'wooled', 'keeks', 'unfitnesses', 'audiometries', 'unhousing', 'dermatologists', 'superficiality', 'hypermedias', 'mugged', 'harts', 'sensualities', 'nonclassical', 'groundbreaker', 'weakside', 'scrupulously', 'handwork', 'holdup', 'unavailingness', 'redelivers', 'albinotic', 'reconsolidated', 'buttock', 'lexicality', 'knapsack', 'redefecting', 'tweeted', 'martial', 'primipara', 'mistook', 'gegenscheins', 'shivareeing', 'talcum', 'gestating', 'electrodes', 'whitewashes', 'commutative', 'unravelling', 'logion', 'bauhinias', 'thermostated', 'dados', 'umbonic', 'rhythmist', 'egression', 'restudies', 'laypeople', 'erasures', 'unscrewing', 'sirenian', 'outpace', 'oversuds', 'teetotally', 'asthenics', 'parenteral', 'overshot', 'spale', 'scoriaceous', 'noters', 'inventor', 'pommeling', 'fuehrer', 'disintermediations', 'resegregate', 'mahuang', 'prolocutors', 'insectan', 'machicolation', 'casked', 'leukodystrophy', 'malposition', 'cycled', 'raveners', 'paraphrases', 'counterstrikes', 'nertz', 'stouter', 'cavetti', 'salterns', 'rectification', 'choreographic', 'subaudible', 'newie', 'premodifications', 'truckles', 'wapitis', 'tort', 'showcases', 'romancing', 'thous', 'burnous', 'wore', 'graphite', 'pingoes', 'xu', 'uncrown', 'famousnesses', 'caudate', 'beleaps', 'malarial', 'synonymized', 'dropsy', 'ingulfed', 'alant', 'nosologic', 'usurper', 'reimpression', 'quandary', 'recentrifuge', 'overmixing', 'plumbism', 'insolations', 'cleavable', 'acclaims', 'boosting', 'succinctest', 'bardolater', 'veer', 'sorbitol', 'torched', 'warrants', 'benison', 'willowlike', 'propjet', 'radiobiologies', 'doable', 'greenbug', 'begirding', 'effectualities', 'smogless', 'sockdologers', 'hominesses', 'soroses', 'mizzens', 'hospice', 'tawsing', 'smaragds', 'retries', 'orthopteroids', 'bewilderedly', 'retires', 'zoogeographers', 'dystonic', 'fearlessness', 'germ', 'mycobacterium', 'peacekeeper', 'quantified', 'troubleshooters', 'interferometric', 'nereids', 'ineluctability', 'wayfaring', 'utilizable', 'cyclized', 'uxorious', 'inhumanities', 'tearier', 'amiablenesses', 'turbojet', 'grouter', 'etude', 'adjutancy', 'ribbon', 'anilinguses', 'fashionably', 'latish', 'umbrageousness', 'paroled', 'theorematic', 'hexosans', 'counterthreats', 'learn', 'short', 'layman', 'orphaned', 'gypsophila', 'crumbly', 'boodling', 'carling', 'linear', 'diageneses', 'enemy', 'cheerfulness', 'prolonges', 'frizzed', 'platings', 'diarchy', 'sourdine', 'rooflike', 'mahoe', 'disadvantages', 'atheneum', 'adulterous', 'photodissociation', 'provocatively', 'slot', 'celoms', 'impetuous', 'mitt', 'bejeezus', 'spindlier', 'chiliastic', 'postindependence', 'prudishly', 'summerwoods', 'retear', 'butled', 'indirectnesses', 'manslaughter', 'flagrances', 'bureaucratically', 'overstaffed', 'abattoirs', 'playbooks', 'bogged', 'frized', 'jacinthes', 'cabbageworms', 'becrust', 'mestino', 'inhabiter', 'trochili', 'rancidity', 'outleap', 'sodalities', 'odorizes', 'anticholinergics', 'heptarchs', 'haulms', 'velarized', 'undotted', 'blousiest', 'disestablishment', 'uncaked', 'termed', 'citrated', 'officialeses', 'endbrains', 'conglomerations', 'epilogue', 'destination', 'bourgeoise', 'ulcer', 'hognoses', 'jiggles', 'pallidnesses', 'screeches', 'oriole', 'anatomized', 'homebrews', 'immunoprecipitating', 'spuriously', 'blowfish', 'batts', 'lentigo', 'adorers', 'monetise', 'trimming', 'hypercritic', 'superficialities', 'astrological', 'obstructor', 'driftage', 'scatter', 'inflictions', 'supermales', 'finalities', 'advocating', 'racemic', 'physiography', 'rubeolas', 'bendaying', 'warmongerings', 'inhibit', 'silk', 'autochthons', 'knosp', 'surreys', 'correctors', 'coordinative', 'tailleurs', 'gaen', 'braininesses', 'uneasinesses', 'hydrophobicities', 'orchestra', 'araks', 'scapegoats', 'picoting', 'rieslings', 'horrified', 'lamentedly', 'hyponeas', 'devolved', 'adzes', 'bedstead', 'santo', 'logogriphs', 'reearning', 'pandy', 'spearmen', 'hiking', 'aspirational', 'mosquito', 'careen', 'ruffianism', 'sporocarps', 'profound', 'phalanx', 'subgum', 'curatorships', 'scrimmaging', 'encyclical', 'fatheaded', 'occultism', 'coenamor', 'metamorphisms', 'rashes', 'mus']
    def __init__(self):
        plain_word_capitals = (random.choice(Hangman.list_of_words)).upper()

        self._secret_word = list(plain_word_capitals)
        self._correct_guess = [None]*len(plain_word_capitals) #current guess of the user
        self._available_letters = set(plain_word_capitals) #set of right letters availabe
        self._letters_tried = []
        self._number_of_errors = 0
        self._number_of_trials = 0
        self._finished = False #flag if the game is finished
        self._result = "";

    def play(self):#REQ4.1
        self.print_introduction()
        while(not self._finished):
            guess = input("\nInsert new letter or the final word: ")
            self.try_add_guess(guess)

        if (self._number_of_errors == Hangman.NUM_TRIAL): #REQ4.2
            self._result = "LOST"
            print("\nYOU LOST!!")
            print("The correct word was: ", end="")

            for i in range(len(self._secret_word)):
                print(self._secret_word[i], end="")
            print("");

        else:
            self._result = "WIN"
            print("\nYOU WON!!!")
        print("Total Errors:    ", self._number_of_errors)
        print("Number of trials: ", self._number_of_trials)

    def try_add_guess(self, guess): # main function to check if inserted guess is valid
        if (guess == None or len(guess) == 0): #REQ2.1
            print("Empty (string) input.\nWarning: This game only accepts 2 types of guesses: 1 character or the secret word.\nThis will not count as an error neither as a trial.\nPlease choose another letter")
            return #if no input was given then ask again for an input. This is not considered as an error or trial
        
        elif not(self.strHasOnlyLetters(guess)): #REQ2.2 and REQ3.2
            print("Numbers or special characters are not allowed in this game.\nThis will not count as an error neither as a trial.\nPlease choose another letter")
            return
        
        elif (len(guess) == 1): # if the input is only a character
            guess = guess.upper() #REQ2.7
            
            if (guess in self._letters_tried): # REQ2.5
                print("Character already tried.\nThis won't count as an error or trial.\nPlease choose another letter")
                self.print_hangman() # REQ2.4
                self.print_guess() # REQ2.4
                return
            else:
                if (guess in self._available_letters):
                    for i in range(len(self._secret_word)):
                        if (self._secret_word[i] == guess):
                            self._correct_guess[i] = guess

                    self._letters_tried.append(guess)
                    self._number_of_trials += 1
                    self.print_hangman() # REQ2.4
                    self.print_guess() # REQ2.4
                    self._available_letters.remove(guess)

                    if(len(self._available_letters) == 0):
                        self._finished = True

                    return
                else: #REQ2.3 The secret word doesnt contain the letter given, it will be considered as an error and trial
                    print("The secret word doesnt contain the letter given!")
                    self._letters_tried.append(guess)
                    self._number_of_errors += 1 
                    self._number_of_trials += 1
                    self.print_hangman() # REQ2.4
                    self.print_guess() # REQ2.4
                    if (self._number_of_errors == Hangman.NUM_TRIAL):
                        self._finished = True
                        return

        elif (len(guess) == len(self._secret_word)): #if the guess given has the same size as the secret word
            guess = guess.upper() #REQ3.6

            if(list(guess) == self._secret_word): #if they have the same letters in the same order
                for i in range(len(self._secret_word)):
                    self._correct_guess[i] = self._secret_word[i]
                self._number_of_trials += 1
                self.print_guess() # REQ2.4
                self._finished = True
                return

            else: #REQ3.3
                print("The given guess does not match the secret word")
                self._number_of_errors += 1
                self._number_of_trials += 1
                self.print_hangman()
                self.print_guess() # REQ2.4
                if (self._number_of_errors == Hangman.NUM_TRIAL):
                    self._finished = True
                    return

        else: # REQ3.5 This is not considered as an error neither as a trial
            print("Warning: This game only accepts 2 types of guesses: 1 character or the secret word. \nThis will not count as an error neither as a trial.\nPlease choose another letter")
            return
        
    def print_guess(self): #print current guess
        l = len(self._correct_guess)
        print("Current Guess: ",end = "")
        for i in range(l):
            if (self._correct_guess[i] == None):
                print ("_  ",end = "")
            else:
                print (self._correct_guess[i]+ " ", end="")
        print()
        print("Letters tried : ", end="")
        for i in range(len(self._letters_tried)):
            print(self._letters_tried[i] + "  ", end="")
        print()

    def print_hangman(self): #print the hangman
        print("====================")
        #first line
        if (self._number_of_errors >= 3):
            print("    ______")
        else:
            print("")
        #second line
        if (self._number_of_errors >= 5):
            print("    |/   |")
        elif (self._number_of_errors >= 4):
            print("    |/  ")
        elif (self._number_of_errors >= 2):
            print("    |  ")
        else:
            print("")
        #third line
        if (self._number_of_errors >= 6):
            print("    |    O")
        elif (self._number_of_errors >= 2):
            print("    |    ")
        else:
            print("")
        #fourth line
        if (self._number_of_errors >= 9):
            print("    |  --|--")
        elif (self._number_of_errors >= 8):
            print("    |  --|")
        elif (self._number_of_errors >= 7):
            print("    |    |")
        elif (self._number_of_errors >= 2):
            print("    |  ")
        else:
            print("")
        #fifth line
        if (self._number_of_errors >= 11):
            print("    |   / \\")
        elif (self._number_of_errors >= 10):
            print("    |   / ")
        elif (self._number_of_errors >= 2):
            print("    |")
        else:
            print("")
        #sixth line
        if (self._number_of_errors >= 2):
            print("  __|_________")
        elif (self._number_of_errors >= 1):
            print("  ____________")
        else:
            print("")
        print("====================")

    def print_introduction(self):
        print("\n\n\n\t\t\tWelcome to \n\n")
        print("H    H     AA     N    N     GGGG    MM   MM    AA    N    N   !!")
        print("H    H    A  A    NN   N    G   GG   MMM MMM   A  A   NN   N   !!")
        print("HHHHHH   AAAAAA   N N  N    G        M MMM M  AAAAAA  N N  N   !!")
        print("H    H   A    A   N  N N    G  GGGG  M     M  A    A  N  N N   !!")
        print("H    H   A    A   N   NN     GGGG    M     M  A    A  N   NN   !!")
        print("\n\n\nGuess the word\n")
        self.print_guess()
        
    def strHasOnlyLetters(self, string):
        for c in string:
            if not((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z'))):
                return False
        return True

def main():
    Hangman().play()
    while(1):
        response = input("\nDo you want to play another game(Y/N)? ").upper()
        if(response == "N" or response == "Y"): #REQ5.3
            if(response =="N"):
                return #REQ5.1
            else:
                Hangman().play() #REQ5.2
        else:        
            print("Character not Valid. Please insert Y or N")    

#if __name__ == '__main__':
    #main()
