import zlib, bz2

def unwrap(data):
    result = ""
    while True:
        if data.startswith('x\x9c'):
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith('BZh'):
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith('\x9cx'):
            data = data[::-1]
            result += '\n'
        else:
            return result


with open('a21/package.pack', 'rb') as f:
    result = unwrap(f.read())
print(result)
