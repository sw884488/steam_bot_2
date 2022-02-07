gameAnswerResult = {}


def gameSearchAnswer(l):
    q = 1
    for i in l:
        gameAnswerResult[q] = i
        q += 1
    return gameAnswerResult

