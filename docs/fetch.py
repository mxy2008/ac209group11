import socket
from socket import *
def fetch(host, url):
    sock = socket.socket()
    sock.connect((host, 80))
    request = 'GET {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(url, host)
    print("Request is:\n", request)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response



def http_req(server, path):

    # Creating a socket to connect and read from
    s=socket(AF_INET,SOCK_STREAM)

    # Finding server address (assuming port 80)
    adr=(gethostbyname(server),80)

    # Connecting to server
    s.connect(adr)

    # Sending request
    s.send("GET "+path+" HTTP/1.0\n\n")

    # Printing response
    resp=s.recv(1024)
    while resp!="":
        print(resp)
        resp=s.recv(1024)


if __name__ == "__main__":
    fetched = http_req('www.google.com','/')#'www.google.com/search?q=123&oq=123&aqs=chrome..69i57j0l5.944j0j4&sourceid=chrome&ie=UTF-8')
    #fetched = http_req("birk105.studby.uio.no","/")
#fetch('webservices.amazon.com/onca/xml',"http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&AWSAccessKeyId=[ac209group11-20]&AssociateTag=[ac209group11-20]&Operation=ItemLookup&ItemId=B00008OE6I&IdType=ASIN&Timestamp=[YYYY-MM-DDThh:mm:ssZ]&Signature=[Request Signature]")
    print('--------------', type(fetched))
    print(fetched.decode('ISO-8859-1'))
