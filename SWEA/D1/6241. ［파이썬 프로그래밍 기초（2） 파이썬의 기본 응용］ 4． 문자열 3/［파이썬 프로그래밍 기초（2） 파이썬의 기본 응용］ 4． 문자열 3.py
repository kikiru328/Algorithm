a = "http://www.example.com/test?p=1&q=2"
x = a.split('://')
protocol = x[0]
print(f"protocol: {protocol}")
host = x[1].split('/')[0]
others = x[1].split('/')[1]
print(f"host: {host}")
print(f"others: {others}")