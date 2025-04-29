def testing():
    print("Hello, Grok!")

def testing_your_boundaries():
    # set the maximum group size and minimum group size
    max_size = 6
    min_size = 2

    # ask for the number of participants in the group. 

    group_size = int(input('How many people are in your group? '))

    # check the input to see if the group size is between
    # the min and max group size

    if group_size < min_size:
        print(f'Group size must be a minimum of {min_size} people.')
    elif group_size > max_size:
        print (f'The maximum group size is {max_size} people.')
    else:
        print(f'I will book {group_size} people for this cycling adventure!')
        print("Get ready to push your boundaries!")
            


if __name__ == '__main__':
    over_and_out()
