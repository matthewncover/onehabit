from onehabit import Coach

if __name__ == "__main__":
    coach = Coach()
    # message = "My goal is to have a more regular bedtime. What's a baby step I can take toward that goal?"
    message = """
    The following sentences are notes written by a user after every failure to meet their habit of 'going to bed at 10pm'.
    Your task is to summarize by identifying the common themes. Here are the sentences:
    Smoked some sativa and couldn't fall asleep. Youtube rabbithole Lost track of time.
    Binging netflix. Late night edible. Instagram got the best of me.
    """
    response = coach.respond(message)
    pass