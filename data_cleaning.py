from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def clean_url(url: str, hostname_only = True) -> str:
    """remove utm information from urls, this will just keep the hostname, path 
    and in a google books link the id of the book in question.
    There is a boolean to just keep the hostname for simpler analysis """
    
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if hostname_only:
        return parsed_url.hostname
    
    # parameters to kepp
    params_to_keep = [
        "id",
    ]

    # Remove the UTM parameters
    filtered_params = {
        k: v for k, v in query_params.items() if k in params_to_keep
    }

    # Build the new query string
    cleaned_query = urlencode(filtered_params, doseq=True)

    # Construct the new URL and remove fragment from it 
    new_url = urlunparse(parsed_url._replace(query=cleaned_query, fragment=''))

    return new_url


# Quick Test (this should be a unit test)
test_url1 = "https://books.google.com/books?id=-MdFAQAAMAAJ&pg=PA77&lpg=PA77&dq=border&source=bl&ots=b76r3BWrOW&sig=ACfU3U2EOQAabp_Fi9oeGlfvv-TUjee0fg&hl=en&sa=X&ved=2ahUKEwjCm8za2fCDAxWttokEHRxXCf0Q6AF6BQi7ARAD"
test_url2 = "https://www.counseling.org/aca-community/learn-about-counseling/what-is-counseling#:~:text=Counseling%20is%20a%20collaborative%20effort,change%20and%20optimal%20mental%20health."
cleaned_url = clean_url(test_url2)
print(cleaned_url)
