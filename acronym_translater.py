acronyms = {
    'LOL': 'laughing out loud',
    'IDK': "I don't know",
    'TBH': 'to be honest'
}

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print(translation)