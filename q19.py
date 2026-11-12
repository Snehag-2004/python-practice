
def smallestSufficientTeam(req_skills, people):
    n = len(req_skills)

    # Assign a bit position to each skill
    skill_index = {skill: i for i, skill in enumerate(req_skills)}

    # Convert each candidate's skills into a bitmask
    people_masks = []

    for person in people:
        mask = 0

        for skill in person:
            if skill in skill_index:
                mask |= (1 << skill_index[skill])

        people_masks.append(mask)

    # All skills are represented by 1s
    target = (1 << n) - 1

    # DP stores the smallest team for each skill combination
    dp = {0: []}

    for i, mask in enumerate(people_masks):
        new_dp = dp.copy()

        for covered, team in dp.items():
            new_covered = covered | mask

            if (new_covered not in new_dp or
                len(team) + 1 < len(new_dp[new_covered])):

                new_dp[new_covered] = team + [i]

        dp = new_dp

    return dp[target]


# Example 1
req_skills = ["Python", "SQL", "MachineLearning", "DataStructures"]

people = [
    ["Python", "SQL"],
    ["SQL", "MachineLearning"],
    ["MachineLearning", "DataStructures"],
    ["DataStructures"]
]

print("Selected Team:", smallestSufficientTeam(req_skills, people))


# Example 2
req_skills = ["Java", "Python", "SQL"]

people = [
    ["Java"],
    ["Python", "SQL"],
    ["SQL"]
]

print("Selected Team:", smallestSufficientTeam(req_skills, people))


# Example 3
req_skills = ["C++", "Python", "DataStructures"]

people = [
    ["C++"],
    ["Python"],
    ["DataStructures"],
    ["C++", "Python", "DataStructures"]
]

print("Selected Team:", smallestSufficientTeam(req_skills, people))
