import requests

wordsite="http://api.wordnik.com:80/v4/words.json/randomWord?hasDictionaryDef=false&minCorpusCount=0&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
word=requests.get(wordsite)
word=word.json()["word"]
print (word)
guessesAllowed = 10
guessedCorrectly= False
guessesMade = 0
wordArray =[]
dashedWord = []

for i in range(0,len(word)):
    wordArray.append(word[i])
    dashedWord.append('-')

def makeGuess():
    guessedCorrectly = 0
    print (''.join(dashedWord))
    print(guessesAllowed-guessesMade)
    guess = str(input('Make a Guess:'))
    for i in range(0,len(word)):
      if guess == word[i]:
          dashedWord[i]=guess
          guessedCorrectly = 1
    return guessedCorrectly


while guessesMade<guessesAllowed and dashedWord!=wordArray:
    guessedCorrectly = makeGuess()
    guessesMade += not guessedCorrectly
    guessedCorrectly = False
    if guessesMade == guessesAllowed:
        print("You lost")

if dashedWord==wordArray:
    print("You Guessed it Correctly!!!")
#This is a github test
#Making changes for github
