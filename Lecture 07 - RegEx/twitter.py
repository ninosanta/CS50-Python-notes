# Goal: prompt users for the URL of their Twitter profile and
# infer from that URL, what is the user's username.

import re


def main():
    url = input("URL: ").strip()



def username_group(url):
    return re.search(r"twitter.com/(\w+)/?", url).group(1)



def username_sub(url):
    return re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url)
    # there are still problems here


def username_groups(url):
    if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(\w+)/?", url, re.IGNORECASE):
        return matches.group(3)
    else:
        return ""


# non-capturing version
def username(url):
    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)/?", url, re.IGNORECASE):
        # even though it matches the firts two groups, it discards them
        return matches.group(1)
    else:
        return ""



if __name__ == "__main__":
    main()
