n = int(input())
invitations = {input() for _ in range(n)}

while True:
    invites = input()
    if invites == "End":
        break
    invitations.discard(invites)

print(len(invitations))
print(sorted(invitations))