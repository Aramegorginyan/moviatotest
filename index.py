films_order = [ 
    {'movieName': 'Interstellar', 'rating': 3, 'genre': 'Fantastic', 'views': 4.500000},
    {'movieName': 'The Godfather', 'rating': 9.77, 'genre': 'Crime', 'views': 12.000000},
    {'movieName': 'Barbie', 'rating': 4.5, 'genre': 'Comedy', 'views': 1.500000}
]

def sort_by_name(films_order):
    result = []

    total = [film["movieName"] for film in films_order]
    sort_total = sorted(total)

    for i in sort_total:
        index = total.index(i)
        result.append(index)

    final_result = [films_order[i] for i in result]
    print(f"Sorted by name: {final_result}")

def sort_by_rating(films_order):
    result = []

    total = [film["rating"] for film in films_order]
    sort_total = sorted(total,reverse=True)

    for i in sort_total:
        index = total.index(i)
        result.append(index)

    final_result = [films_order[i] for i in result]
    print(f"Sorted by rating: {final_result}")

def sort_by_genre(films_order):
    result = []

    total = [film["genre"] for film in films_order]
    sort_total = sorted(total)

    for i in sort_total:
        index = total.index(i)
        result.append(index)

    final_result = [films_order[i] for i in result]
    print(f"Sorted by genre: {final_result}")

def sort_by_views(films_order):
    result = []

    total = [film["views"] for film in films_order]
    sort_total = sorted(total,reverse=True)

    for i in sort_total:
        index = total.index(i)
        result.append(index)

    final_result = [films_order[i] for i in result]
    print(f"Sorted by views: {final_result}")

def main():
    print(films_order)
    print("How do you want to sort the movies")
    print("1. Sort by name")
    print("2. Sort by rating")
    print("3. Sort by genre")
    print("4. Sort by views")
    print("5. Exit")
    exit = True

    while exit:
        sort_method = str(input(">>> "))
        if sort_method.strip() == "1":
            sort_by_name(films_order)
        elif sort_method.strip() == "2":
            sort_by_rating(films_order)
        elif sort_method.strip() == "3":
            sort_by_genre(films_order)
        elif sort_method.strip() == "4":
            sort_by_views(films_order)
        elif sort_method.strip() == "5":
            exit = False
            print("See you soon")
        else:
            print("Type the method of sorting")

main()