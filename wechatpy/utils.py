from __future__ import absolute_import, unicode_literals
import hashlib


class ObjectDict(dict):

    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None

    def __setattr__(self, key, value):
        self[key] = value


def check_signature(token, signature, timestamp, nonce):
    tmparr = [token, timestamp, nonce]
    tmparr.sort()
    tmpstr = ''.join(tmparr)
    digest = hashlib.sha1(tmpstr).hexdigest()
    return digest == signature
