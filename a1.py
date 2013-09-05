orginStr = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dm\
p. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq r\
cvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

frm = "abcdefghijklmnopqrstuvwxyz"
to = "cdefghijklmnopqrstuvwxyzab"

import string
trans = string.maketrans(frm, to)

print(string.translate(orginStr, trans))

    
