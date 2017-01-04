# -*- coding: utf-8 -*-
max|D|=|Q|+θ
for di : D by post-order do
    if |Di | > max|D| then 
        goto NEXTFOR
    end if
    p = par(di )
    if di は兄を持つ or di は根 or |Dp| > max|D| then
        for j : 0 to |Q| − 1 do
            if qj は兄を持つ or qj は根 then
                TEDCalulation(Di,Qj) 
            end if
        end for
    end if
    if di は根 or |Dp| > max|D| then 
        for k : left(di) to i do
            if dk.TED[|Q|−1]<=θ then
                add k to Result
            end if
        end for
        // we can release buffer
    end if
    NEXTFOR:
end for
return Result