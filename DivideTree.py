# -*- coding: utf-8 -*-
l⇐1,r⇐|D|
while do
    x ⇐ (l + r)/2
    j⇐1
    for di : D by preorder do
        Assign[i] = j
        if j < k and di+1 で分割可能 and
                プロセス j の頂点数が x 以上 then
            j⇐j+1 
        end if
    end for
    if l=xthen
        goto BREAKWHILE
    end if
    if j = k then
        l ⇐ mid
    else
        r ⇐ mid
    end if
end while
BREAKWHILE:
return Assign