import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))