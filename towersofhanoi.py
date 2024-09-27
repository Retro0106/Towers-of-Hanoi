from stack import Stack  # Ensure this is correct

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks.extend([left_stack, middle_stack, right_stack])

# Set up the Game
while True:
    try:
        num_disks = int(input('\nHow many disks do you want to play with? (Minimum 3)\n'))
        if num_disks >= 3:
            break
        print('Please enter a number greater than or equal to 3.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = 2 ** num_disks - 1
print(f'\nThe fastest you can solve this game is in {num_optimal_moves} moves')

# Get User Input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i, stack in enumerate(stacks):
            print(f'Enter {choices[i]} for {stack.get_name()}')
        user_input = input('').strip().upper()
        if user_input in choices:
            return stacks[choices.index(user_input)]

# Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        print(f'{stack.get_name()}: {stack.get_items()}')  # Assuming get_items() returns stack contents
    
    while True:
        print("\nWhich stack do you want to move from?")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?")
        to_stack = get_input()
        
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
