def count_negative_accounts(numOfAccounts, balances):
    count = 0
    for balance in balances:
        if balance < 0:
            count += 1
    return count

# Read input
numOfAccounts = int(input())
balances = list(map(int, input().split()))

# Calculate and print the result
negative_count = count_negative_accounts(numOfAccounts, balances)
print(negative_count)
