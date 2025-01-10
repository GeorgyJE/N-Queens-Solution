def N_Queens_solution(n):
    answers = []
    if n == 1:
        return [["Q"]] #the only solution to n = 1
    if 1 < n < 4:
        return None #there are no solutions to n = 2 and n = 3

    right_diagonals = set()  # there are two types of diagonals on the board:
    left_diagonals = set()  # first type: diagonals that go down and left. Second type: those that go down and right
    # the two types: (/ and \)

    columns = []
    for i in range(n):
        columns.append(i) # after each queen placement all the attacked columns and diagonals will be updated.

    row = 0

    for c in range(n):
        new_right = right_diagonals.copy()
        new_right.add(c - row)
        new_left = left_diagonals.copy()
        new_left.add(n - 1 - c - row)
        check_row(row + 1, columns[:columns.index(c)] + columns[columns.index(c) + 1:], n, [c], new_right, new_left, answers)

    n = len(answers[0]) - 1
    for sol in answers:
        for num in range(n + 1):
            sol[num] = ("." * sol[num]) + "Q" + ("." * (n - sol[num])) # convert the answer into the leetcode format.

    return answers

def check_row(row, columns, N, answer, right_diagonals, left_diagonals, answers):
    for col in columns:
        if (col-row) not in right_diagonals and (N - 1 - col - row) not in left_diagonals: #see if it is attacked
            if row + 1 == N:
                answers.append(answer + [col])
            else:
                new_right = right_diagonals.copy() #set an updated list of attacked diagonals and columns
                new_right.add(col-row)
                new_left = left_diagonals.copy()
                new_left.add(N - 1 - col - row)
                check_row(row + 1, columns[:columns.index(col)] + columns[columns.index(col) + 1:], N, answer + [col], new_right, new_left, answers)

print(N_Queens_solution(6))