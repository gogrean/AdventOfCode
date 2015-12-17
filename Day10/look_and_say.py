def number_length(old, reps):
    rep = 1
    while rep <= reps:
        i = 0
        new = ''
        while i < len(old):
            count = 1
            while i < len(old)-1 and old[i] == old[i+1]:
                i += 1
                count += 1
            new += str(count) + old[i]
            i += 1
        if count == 1 and i == len(old)-1:
            new += str(count) + old[i]
        old = new
        rep += 1
    return len(new)

number = '1113222113'

print("The length of the number after 40 iterations is ", number_length(number, 40), " characters.")
print("The length of the number after 50 iterations is ", number_length(number, 50), " characters.")

    
        
    
