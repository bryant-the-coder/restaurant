def line():
    print("-" * 60)


def get_rating(reviews):
    rating = 5
    if reviews:
        rating = sum(reviews) // len(reviews)
    return "⭐️" * rating
