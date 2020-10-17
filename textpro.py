def make_sentence(phrase):
    interrogatives = ("how", "what", "why", "when", "where")
    capitalized = phrase.capitalize()

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(make_sentence(user_input))

print(" ".join(results))

