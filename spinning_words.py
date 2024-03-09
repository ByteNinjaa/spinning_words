def spin_words(sentence):
    new_sent = []
    words = sentence.split()
    
    last_word = words[-1]
    for w in words:
        if len(w) >= 5:
            rev_word = w[::-1]
            new_sent.append(rev_word)
        else:
            new_sent.append(w)
        

        
    return ' '.join(new_sent)
