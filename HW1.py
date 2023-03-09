name = ["Alchemy Of Soul","Little Women(2019)","Happiness","The disatrous life of Saiki K","Encanto","Tomorrow","Start Up","Run On","DearM","Because this is my first Life","Barbie:Princess and the PopStar","Sweet Home"]

description = ["This is a K-drama about the tales between young mages and has 20 episodes. I love how they potray each characters and also love every single plots of the show. It has season 2 and will be air on December,12. I don't think I can ever get over this drama because it feels like home.", "This is an English film adaption of famous book with the same name'Little Women'. It is about the hardships and relationships between four March sisters with the point of view of Jo March. I relate to the character Jo march so much that this one remain inn my heart.", "This is a zombie K-drama with total of 12 episodes. I love the relationship between mainleads. I also learned how the true nature of human can be when they think they can get away with their crimes when there is no laws. The show gives me so much stress but it was worth learning the lesson.", "This is a comedy anime where the main character has superpowers and use them to live like an ordinary person among the people. It is so cute and funny how he said he doesn't care about his friends but he keeps secretly helping them with everything.","It is a disney cartoon about a family with magic powers. Everyone in the family has individual powers but Mirable didn't get any so she has to find her own fate. It potrays the realistic relationships between family members and the songs even won Oscar. Whenever I feel bored, I always rewatch that cartoon","This is a supernatural movie about Grim Reapers who try to save people from taking their own lives. It contains 16 episodes and each episode potrays different stories of people. All the episode never fails to make me cry and I learned a lot of life lessons from this K-drama","This is a stroy about some youths who wanna start their own business and contains 16 episodes.There are four main characters in the show and it is carzy how I can relate to everyone of them. This K-drama motivates me to never gives up and also want me to start coding.","This is a slow K-drama about four main characters who are trying to keep running on their ways of life. I love the healthy relationships between main leads and the show itself clam me down.","This is a web-drama about the life of University students. But for me this show motivates me to start taking coding classes. I love the story line but I am more interested in Coding.","This is a K-drama of a marriage about a girl who needs home and a boy who needs roommate. This show teaches me that we can makes mistakes and it is okay because this is our first life.","This is a cartoon movie about two girls. You might think it is silly to choose the children movie to be one of my favorite. But it shows sometimes how we wish we were somebody else and we are not satisfied with our life. They both changed their body and found their own goals in life.","This is an apoclypse movie about people turning into monsters. I like how different people react and do the diffrent things for the same situations. People don't like the mastermind guy but I really like him and can understand why he do that in some situations. It was a emotional rollercoaster for me to watch that show."]

quit = "n"

print("My name is 'May'(student id - 0000000). This is the list of my favorite movies, K-dramas, and cartoons. This program will introduce you the details of why I like each movies, K-dramas, and cartoons.")

while quit != "y":

    print("\nMy Favorite Movies, K-Dramas, and Cartoons")
    print("=" *50)

    items = 1
    for items in range(1,13):
        print(items, name[items-1])

    print("=" *50)

    user = input("Choose one from the list you want to know about : ")

    if user == "1" or user == "2" or user == "3" or user == "4" or user == "5" or user == "6" or user == "7" or user == "8" or user == "9" or user == "10" or user == "11" or user == "12":
        user = int(user)
        print("\n",name[user-1],"\n",description[user-1])
    else:
        print("\nWrong Input. The number should be between 1 and 12")

    quit = input("\nDo you like to quit? y/n: ")

    if quit == "y":
        print("\n")
        for i in range(1,11,1):
            print('<3' * (11-i), "Good Bye! See you next time.", '<3' * i)
    
