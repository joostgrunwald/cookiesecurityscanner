import http.cookiejar
import urllib.request
import termcolor

while True:
    url = input("Enter a URL to check the cookies: ")

    if not url.startswith('http'):
        url = f'http://{url}'

    try:
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        r = opener.open(url)
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} {e.reason}")
        print("Please enter a valid URL and try again.\n")
    except urllib.error.URLError as e:
        print("Error: Unable to reach the server.")
        print("Please check your internet connection and try again.\n")
    else:
        break

print(f"Total cookies: {len(cj)}")

for cookie in cj:
    # if starts with __Host- or __Secure-, print green (extra safe)
    if cookie.name.startswith('__Host-') or cookie.name.startswith('__Secure-'):
        print(termcolor.colored(f"\nName: {cookie.name}", 'green'))
    else:
        print(f"\nName: {cookie.name}")

    print(f"Value: {cookie.value}")
    print(f"Domain: {cookie.domain}")
   # TODO:check for loose domains

    if cookie.secure:
        print(termcolor.colored("This cookie is secure", 'green'))
    elif cookie.discard:
        print(termcolor.colored("This session cookie is NOT secure", 'red'))
    else:
        print(termcolor.colored("This cookie is NOT secure", 'yellow'))

    if cookie.has_nonstandard_attr('HttpOnly'):
        print(termcolor.colored("This cookie has httponly attribute", 'green'))
    elif cookie.discard:
        print(termcolor.colored("This session cookie does not have httponly attribute", 'red'))
    else:
        print(termcolor.colored("This cookie does not have httponly attribute", 'yellow'))

    if cookie.has_nonstandard_attr('SameSite'):
        sam = cookie.get_nonstandard_attr('SameSite')
        print(f"Samesite value:{str(sam)}")
        print(termcolor.colored("This cookie has SameSite  attribute", 'green'))
    elif cookie.discard:
        print(termcolor.colored("This session cookie does not have SameSite  attribute", 'red'))
    else:
        print(termcolor.colored("This cookie does not have Samesite  attribute", 'yellow'))

    #print('\n')
