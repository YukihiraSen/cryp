#ENCODED BY : 
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
