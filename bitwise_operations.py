import urllib.request

input = "3, 5, 7, 9"
threshold = "4"
items = input.split(",")
int_list = []

for i in items:
    int_list.append(int(i))
html = "<html>\n<head>\n<title>\nAssignment 7\n</title>\n</head>\n<body>\n"
url = "http://checkip.amazonaws.com"

with urllib.request.urlopen(url) as response:
    public_ip = response.read().decode("utf-8")
html += "Public IP: {}<br>\n".format(public_ip)
html += "Intergers separated by comma: {}\n<br>\n".format(input)
html += "Threshold: {}\n<br>\n".format(threshold)

band = int_list[0]
bor = int_list[0]
bxor = int_list[0]
for i in int_list[1:]:
    band &= i
    bor |= i
    bxor ^= i

greater = []
for i in int_list:
    if i > int(threshold):
        greater.append(i)
msg = ",".join(map(str, greater))

html += "Bitwise AND: {}\n<br>\n".format(band)
html += "Bitwise OR: {}\n<br>\n".format(bor)
html += "Bitwise XOR: {}\n<br>\n".format(bxor)
html += "Numbers grater than threshold: {}\n".format(msg)
html += "</body>\n</html>"

print(html)
