# old school phone system to tell you the times of the movies (aka moviefone)

current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm'
}

print("We are currently showing: ")
for movie in current_movies:
    print(movie)

movie_choice = input("What movie would you like to see the showtime for?\n")
showtime = current_movies.get(movie_choice)

if showtime == None:
    print("We're not currently showing", movie_choice)
else:
    print(movie_choice, "will play at", current_movies.get(movie_choice))