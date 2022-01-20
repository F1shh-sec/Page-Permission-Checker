import requests

import requests
import urllib3
import webbrowser
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cookies = {
}

headers = {
}

sites_200 = []
sites_403 = []
def printPage(response):
    with open('test.html', "w") as output:
        badchars = ['\\n', '\\t', 'b\'']
        responseContent = str(response.content).strip()
        for elm in badchars:
            responseContent = responseContent.replace(elm, "")
        output.write(responseContent)

def test_html_code(response_code, page_url):
    if response_code == 200:
        print(f"{page_url} : Success : {response_code}")
        sites_200.append(page_url)
    elif response_code == 403:
        print(f"{page_url}: Success : {response_code}")
        sites_403.append(page_url)
    elif response_code == 404:
        print(f"{page_url}: Failed : {response_code}")

def write_report():
    with open('success.txt', "w") as output:
        output.write("PAGES THAT 200:\n")
        for elm in sites_200:
            # webbrowser.open(elm)
            output.write(f"{elm}\n")
        output.write("\n\nPAGES THAT 403:\n")
        for elm in sites_403:
            output.write(f"{elm}\n")
def main():
    with open('test.txt', "r") as sites:
        lines = sites.readlines()
        for line in lines:
            page_url = line.strip()
            response = requests.get(page_url, headers=headers, cookies=cookies, verify=False)
            test_html_code(response.status_code, page_url)
    write_report()
if __name__ == '__main__':
    main()